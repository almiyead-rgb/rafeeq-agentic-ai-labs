#!/usr/bin/env python3
"""Validate the complete Rafeeq learner release from a clean repository."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "public"
REPORTS_DIR = ROOT / "reports"
NOTEBOOK = ROOT / "notebooks" / "Rafeeq_Mini_Capstone.ipynb"
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from export_safety_check import VIRTUAL_FILES, _secret_findings, candidate_files  # noqa: E402
from run_gate import _run_unittests  # noqa: E402


ASSESSMENT_REQUIRED = {
    "schema_version",
    "run_id",
    "generated_at_utc",
    "llm_mode",
    "mcp_transport",
    "versions",
    "cases",
    "metrics",
    "critical_gates",
    "optimization",
    "readiness",
    "all_critical_gates_passed",
}
TRACE_REQUIRED = {
    "trace_id",
    "span_id",
    "parent_span_id",
    "timestamp_utc",
    "component",
    "event_type",
    "status",
    "latency_ms",
    "route",
    "outcome",
    "risk_flags",
    "model_calls_delta",
    "tool_calls_delta",
    "retrieval_calls_delta",
    "redacted",
}


def _capture_check(name: str, function: Callable[[], tuple[bool, dict[str, Any]]]) -> dict[str, Any]:
    try:
        passed, details = function()
        return {"name": name, "passed": bool(passed), "details": details}
    except Exception as exc:
        return {"name": name, "passed": False, "details": {"error": type(exc).__name__}}


def _data_check() -> tuple[bool, dict[str, Any]]:
    expected = {
        "orders.csv": 24,
        "policy_chunks.jsonl": 6,
        "memory_seed.jsonl": 8,
        "tickets_dev.jsonl": 16,
        "eval_public.jsonl": 8,
        "security_cases.jsonl": 8,
    }
    counts: dict[str, int] = {}
    with (DATA_DIR / "orders.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    counts["orders.csv"] = len(rows)
    identifiers = [row.get("order_id", "") for row in rows]
    unique_orders = len(identifiers) == len(set(identifiers)) and all(re.fullmatch(r"TW-\d{5}", item) for item in identifiers)
    for name in expected:
        if name == "orders.csv":
            continue
        count = 0
        with (DATA_DIR / name).open("r", encoding="utf-8") as handle:
            for raw in handle:
                if not raw.strip():
                    continue
                value = json.loads(raw)
                if not isinstance(value, dict):
                    raise ValueError(f"{name} contains a non-object line")
                count += 1
        counts[name] = count
    passed = counts == expected and unique_orders
    return passed, {"counts": counts, "expected": expected, "unique_order_ids": unique_orders}


def _tests_check() -> tuple[bool, dict[str, Any]]:
    report = _run_unittests(("test_*.py",))
    return bool(report["passed"]), report


def _notebook_check() -> tuple[bool, dict[str, Any]]:
    completed = subprocess.run(
        [sys.executable, "scripts/validate_notebook.py", str(NOTEBOOK)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    output = (completed.stdout + "\n" + completed.stderr).strip()
    return completed.returncode == 0, {"return_code": completed.returncode, "output": output[-2000:]}


def _assessment_check() -> tuple[bool, dict[str, Any]]:
    path = REPORTS_DIR / "assessment_results.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    gates = payload.get("critical_gates")
    cases = payload.get("cases")
    passed = (
        ASSESSMENT_REQUIRED.issubset(payload)
        and payload.get("schema_version") == "1.0"
        and payload.get("llm_mode") == "stub"
        and payload.get("mcp_transport") == "stdio"
        and isinstance(cases, list)
        and bool(cases)
        and all(isinstance(case, dict) and {"case_id", "passed"}.issubset(case) for case in cases)
        and isinstance(gates, dict)
        and bool(gates)
        and all(value is True for value in gates.values())
        and payload.get("all_critical_gates_passed") is True
    )
    return passed, {
        "case_count": len(cases) if isinstance(cases, list) else 0,
        "critical_gates": gates if isinstance(gates, dict) else {},
        "all_critical_gates_passed": payload.get("all_critical_gates_passed"),
    }


def _trace_check() -> tuple[bool, dict[str, Any]]:
    path = REPORTS_DIR / "trace.jsonl"
    denied = {"message", "prompt", "chain_of_thought", "customer_id"}
    count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            if not raw.strip():
                continue
            event = json.loads(raw)
            if not isinstance(event, dict):
                return False, {"line": line_number, "error": "non_object"}
            if not TRACE_REQUIRED.issubset(event):
                return False, {"line": line_number, "error": "missing_fields"}
            if event.get("redacted") is not True or denied.intersection(event):
                return False, {"line": line_number, "error": "redaction_contract"}
            count += 1
    return count > 0, {"events": count, "redacted": count > 0}


def _reports_check() -> tuple[bool, dict[str, Any]]:
    required = (
        REPORTS_DIR / "PROJECT_REPORT.md",
        REPORTS_DIR / "SECURITY_ASSESSMENT.md",
        REPORTS_DIR / "monitoring_dashboard.png",
        REPORTS_DIR / "checkpoints" / "doctor_report.json",
        REPORTS_DIR / "checkpoints" / "day1_results.json",
        REPORTS_DIR / "checkpoints" / "day2_memory_results.json",
        REPORTS_DIR / "checkpoints" / "day2_results.json",
        REPORTS_DIR / "checkpoints" / "day3_security_baseline.json",
        REPORTS_DIR / "checkpoints" / "day3_security_retest.json",
    )
    missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file() or path.stat().st_size == 0]
    todos: list[str] = []
    for name in ("PROJECT_REPORT.md", "SECURITY_ASSESSMENT.md"):
        path = REPORTS_DIR / name
        if path.is_file() and "[TODO" in path.read_text(encoding="utf-8"):
            todos.append(path.relative_to(ROOT).as_posix())
    dashboard = REPORTS_DIR / "monitoring_dashboard.png"
    png_ok = dashboard.is_file() and dashboard.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"

    checkpoint_failures: list[str] = []
    for name in (
        "doctor_report.json",
        "day1_results.json",
        "day2_memory_results.json",
        "day2_results.json",
        "day3_security_retest.json",
    ):
        path = REPORTS_DIR / "checkpoints" / name
        if path.is_file():
            value = json.loads(path.read_text(encoding="utf-8"))
            if value.get("all_passed") is not True:
                checkpoint_failures.append(name)
    passed = not missing and not todos and png_ok and not checkpoint_failures
    return passed, {
        "missing": missing,
        "unfinished_reports": todos,
        "dashboard_png": png_ok,
        "failed_checkpoints": checkpoint_failures,
    }


def _manifest_check() -> tuple[bool, dict[str, Any]]:
    """Validate a C29 manifest when present; absence is valid before export."""

    path = REPORTS_DIR / "submission_manifest.json"
    if not path.is_file():
        return True, {"present": False, "note": "generated only by the guarded final export"}
    payload = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "schema_version",
        "generated_at_utc",
        "expected_final_commit_message",
        "files",
        "safety_checks",
        "all_passed",
    }
    records = payload.get("files")
    mismatches: list[str] = []
    unsafe_entries: list[str] = []
    if isinstance(records, list):
        for record in records:
            if not isinstance(record, dict) or not {"path", "sha256", "size_bytes"}.issubset(record):
                unsafe_entries.append("<invalid-record>")
                continue
            relative = str(record["path"])
            file_path = ROOT / relative
            if (
                relative == "reports/submission_manifest.json"
                or relative == "notebooks/Rafeeq_Mini_Capstone.ipynb"
                or relative.startswith("reports/checkpoints/")
                or relative.endswith(".zip")
            ):
                unsafe_entries.append(relative)
                continue
            if relative in VIRTUAL_FILES:
                content = VIRTUAL_FILES[relative]
                if (
                    hashlib.sha256(content).hexdigest() != record["sha256"]
                    or len(content) != record["size_bytes"]
                ):
                    mismatches.append(relative)
                continue
            if not file_path.is_file():
                mismatches.append(relative)
                continue
            content = file_path.read_bytes()
            if (
                hashlib.sha256(content).hexdigest() != record["sha256"]
                or len(content) != record["size_bytes"]
            ):
                mismatches.append(relative)
    safety = payload.get("safety_checks")
    passed = (
        required.issubset(payload)
        and payload.get("schema_version") == "1.0"
        and payload.get("expected_final_commit_message") == "feat: submit Rafeeq Mini capstone"
        and payload.get("completed_notebook_upload_required") is True
        and isinstance(records, list)
        and bool(records)
        and isinstance(safety, dict)
        and safety.get("manual_notebook_upload_required") is True
        and all(value is True for value in safety.values())
        and payload.get("all_passed") is True
        and not mismatches
        and not unsafe_entries
    )
    return passed, {
        "present": True,
        "files": len(records) if isinstance(records, list) else 0,
        "hash_or_size_mismatches": mismatches,
        "unsafe_entries": unsafe_entries,
    }


def _safety_docs_check() -> tuple[bool, dict[str, Any]]:
    required = {
        "README.md": ("synthetic", "LLM_MODE=stub", "No API key"),
        "SECURITY.md": ("secret", "synthetic"),
        "docs/learner-guide.md": ("rafeeq-mini-submission.zip", "private", "API"),
        "recovery/README.md": ("private", "checkpoint"),
    }
    missing_terms: dict[str, list[str]] = {}
    for relative, terms in required.items():
        path = ROOT / relative
        if not path.is_file():
            missing_terms[relative] = ["<file missing>"]
            continue
        text = path.read_text(encoding="utf-8")
        absent = [term for term in terms if term.casefold() not in text.casefold()]
        if absent:
            missing_terms[relative] = absent
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    stale_markers = [
        marker
        for marker in ("not ready for learner use", "does not contain a runnable notebook", "0.1.0-alpha")
        if marker.casefold() in readme.casefold()
    ]
    return not missing_terms and not stale_markers, {
        "missing_terms": missing_terms,
        "stale_prerelease_markers": stale_markers,
    }


def _public_safety_check() -> tuple[bool, dict[str, Any]]:
    forbidden_name = re.compile(r"(?:hidden|solution|answer[-_]?key|instructor[-_]?package)", re.IGNORECASE)
    forbidden_paths: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if forbidden_name.search(relative):
            forbidden_paths.append(relative)
    files = candidate_files()
    secrets = _secret_findings(files)
    return not forbidden_paths and not secrets, {
        "forbidden_paths": forbidden_paths,
        "configured_secret_findings": secrets,
        "files_scanned": len(files),
    }


def validate_release() -> dict[str, Any]:
    checks = [
        _capture_check("public_data", _data_check),
        _capture_check("public_unittest", _tests_check),
        _capture_check("notebook_contract", _notebook_check),
        _capture_check("assessment_schema_and_gates", _assessment_check),
        _capture_check("trace_schema_and_redaction", _trace_check),
        _capture_check("required_reports", _reports_check),
        _capture_check("submission_manifest_if_present", _manifest_check),
        _capture_check("learner_safety_documentation", _safety_docs_check),
        _capture_check("public_material_and_secret_scan", _public_safety_check),
    ]
    all_passed = all(check["passed"] for check in checks)
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "release": "0.9.0-rc1",
        "checks": checks,
        "passed": sum(bool(check["passed"]) for check in checks),
        "failed": sum(not bool(check["passed"]) for check in checks),
        "all_passed": all_passed,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None, help="optional JSON output path under reports/")
    args = parser.parse_args(argv)
    report = validate_release()
    if args.output is not None:
        try:
            output = args.output.resolve()
            if REPORTS_DIR.resolve() not in output.parents:
                raise ValueError("--output must be inside reports/")
            output.parent.mkdir(parents=True, exist_ok=True)
            temporary = output.with_name(output.name + ".tmp")
            temporary.write_text(
                json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            os.replace(temporary, output)
        except (OSError, ValueError) as exc:
            print(f"RELEASE CHECK: ERROR — {exc}")
            return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    print(f"RELEASE_CHECK={'PASSED' if report['all_passed'] else 'FAILED'}")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

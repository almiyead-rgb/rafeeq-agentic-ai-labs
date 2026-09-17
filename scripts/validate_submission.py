#!/usr/bin/env python3
"""Validate an extracted learner submission after the notebook is added.

Unlike the course-source validator, this checker intentionally allows saved
notebook outputs and does not require temporary day checkpoints.  It verifies
the submitted notebook structure, C29 completion evidence, final reports,
manifest hashes, critical gates, trace redaction, and configured secret scan.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "Rafeeq_Mini_Capstone.ipynb"
REPORTS = ROOT / "reports"
MANIFEST = REPORTS / "submission_manifest.json"
EXPECTED_COMMIT_MESSAGE = "feat: submit Rafeeq Mini capstone"

EXPECTED_SECTIONS = tuple(
    [
        "C0_ENV_DOCTOR",
        "C1_ARCHITECTURE",
        "C2_TYPED_STATE",
        "C3_BOUNDED_GRAPH",
        "C4_REASONING_TRACES",
        "C5_REACT_ORDERS",
        "C6_TOOL_SCHEMA",
        "C7_MCP_SERVER",
        "C8_MCP_CLIENT",
        "C9_DAY1_GATE",
        "C10_RESTORE",
        "C11_SESSION_MEMORY",
        "C12_SCOPED_RECALL",
        "C13_POLICY_RETRIEVAL",
        "C14_SPECIALISTS",
        "C15_SUPERVISOR",
        "C16_TYPED_HANDOFF",
        "C17_PLAN_EXECUTE",
        "C18_REFUND_GATE",
        "C19_INTERRUPT_RESUME",
        "C20_DAY2_GATE",
        "C21_THREAT_MODEL",
        "C22_ATTACK_SUITE",
        "C23_GUARD_FIX_RETEST",
        "C24_REFLECTION_GATE",
        "C25_TRACE_EVAL",
        "C26_ONE_OPTIMIZATION",
        "C27_SCORECARD",
        "C28_READINESS",
        "C29_EXPORT_SAFETY_CHECK",
    ]
)
FINAL_OUTPUTS = (
    "reports/PROJECT_REPORT.md",
    "reports/SECURITY_ASSESSMENT.md",
    "reports/trace.jsonl",
    "reports/assessment_results.json",
    "reports/monitoring_dashboard.png",
    "reports/submission_manifest.json",
)
SECRET_PATTERNS = (
    ("openai_key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("github_token", re.compile(r"\b(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("bearer_token", re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{24,}\b", re.IGNORECASE)),
)
TEXT_SUFFIXES = {".py", ".md", ".json", ".jsonl", ".csv", ".txt", ".yml", ".yaml", ".html", ".js", ".css", ".ipynb"}


def _source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def _notebook_check() -> tuple[bool, dict[str, Any]]:
    try:
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return False, {"error": type(exc).__name__}
    cells = notebook.get("cells")
    if notebook.get("nbformat") != 4 or not isinstance(cells, list) or not cells:
        return False, {"error": "invalid_notebook_shape"}
    combined = "\n".join(_source_text(cell) for cell in cells if isinstance(cell, dict))
    positions = [combined.find(section) for section in EXPECTED_SECTIONS]
    missing_sections = [section for section, position in zip(EXPECTED_SECTIONS, positions) if position < 0]
    order_ok = not missing_sections and positions == sorted(positions)
    expected_todos = [f"TODO-{number}" for number in range(1, 15)]
    missing_todos = [marker for marker in expected_todos if marker not in combined]
    unexpected_todos = [f"TODO-{number}" for number in range(15, 50) if f"TODO-{number}" in combined]
    passed = order_ok and not missing_todos and not unexpected_todos and "FINAL_EXPORT" in combined
    return passed, {
        "sections": len(EXPECTED_SECTIONS) - len(missing_sections),
        "section_order": order_ok,
        "missing_sections": missing_sections,
        "todo_markers": len(expected_todos) - len(missing_todos),
        "missing_todo_markers": missing_todos,
        "unexpected_todo_markers": unexpected_todos,
        "saved_outputs_allowed": True,
    }


def _load_manifest() -> dict[str, Any]:
    value = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest must be a JSON object")
    return value


def _learner_status(manifest: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    status: Any = manifest.get("learner_todo_status")
    source = "manifest"
    if not isinstance(status, dict):
        for path in (
            REPORTS / "learner_todo_status.json",
            REPORTS / "checkpoints" / "learner_todo_status.json",
        ):
            if path.is_file():
                status = json.loads(path.read_text(encoding="utf-8"))
                source = path.relative_to(ROOT).as_posix()
                break
    if not isinstance(status, dict):
        return False, {"source": "missing", "error": "learner_todo_status is required"}
    items = status.get("items")
    expected = {f"TODO-{number}" for number in range(1, 15)}
    observed: dict[str, bool] = {}
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict) and isinstance(item.get("exercise"), str):
                observed[item["exercise"]] = item.get("passed") is True
    passed = (
        status.get("total") == 14
        and status.get("completed") == 14
        and status.get("all_complete") is True
        and set(observed) == expected
        and all(observed.values())
    )
    return passed, {
        "source": source,
        "completed": status.get("completed"),
        "total": status.get("total"),
        "all_complete": status.get("all_complete"),
        "items_verified": len(observed),
    }


def _outputs_check() -> tuple[bool, dict[str, Any]]:
    missing = [relative for relative in FINAL_OUTPUTS if not (ROOT / relative).is_file() or (ROOT / relative).stat().st_size == 0]
    unfinished: list[str] = []
    for relative in ("reports/PROJECT_REPORT.md", "reports/SECURITY_ASSESSMENT.md"):
        path = ROOT / relative
        if path.is_file() and "[TODO" in path.read_text(encoding="utf-8"):
            unfinished.append(relative)
    dashboard = REPORTS / "monitoring_dashboard.png"
    png_ok = dashboard.is_file() and dashboard.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
    return not missing and not unfinished and png_ok, {
        "required": len(FINAL_OUTPUTS),
        "missing": missing,
        "unfinished_reports": unfinished,
        "dashboard_png": png_ok,
    }


def _trace_check() -> tuple[bool, dict[str, Any]]:
    required = {
        "trace_id",
        "span_id",
        "timestamp_utc",
        "component",
        "event_type",
        "status",
        "risk_flags",
        "redacted",
    }
    denied = {"message", "prompt", "chain_of_thought", "customer_id"}
    count = 0
    try:
        with (REPORTS / "trace.jsonl").open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                if not raw.strip():
                    continue
                event = json.loads(raw)
                if (
                    not isinstance(event, dict)
                    or not required.issubset(event)
                    or event.get("redacted") is not True
                    or denied.intersection(event)
                ):
                    return False, {"line": line_number, "error": "trace_contract"}
                count += 1
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return False, {"error": type(exc).__name__}
    return count > 0, {"events": count, "redacted": count > 0}


def _assessment_check() -> tuple[bool, dict[str, Any]]:
    try:
        value = json.loads((REPORTS / "assessment_results.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return False, {"error": type(exc).__name__}
    gates = value.get("critical_gates") if isinstance(value, dict) else None
    passed = (
        isinstance(gates, dict)
        and bool(gates)
        and all(item is True for item in gates.values())
        and value.get("all_critical_gates_passed") is True
        and value.get("llm_mode") == "stub"
    )
    return passed, {"critical_gates": gates if isinstance(gates, dict) else {}, "all_passed": passed}


def _manifest_check(manifest: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    records = manifest.get("files")
    safety = manifest.get("safety_checks")
    mismatches: list[str] = []
    unsafe_entries: list[str] = []
    paths: set[str] = set()
    if isinstance(records, list):
        for record in records:
            if not isinstance(record, dict) or not {"path", "sha256", "size_bytes"}.issubset(record):
                unsafe_entries.append("<invalid-record>")
                continue
            relative = str(record["path"])
            paths.add(relative)
            path = ROOT / relative
            if (
                relative == "reports/submission_manifest.json"
                or relative == "notebooks/Rafeeq_Mini_Capstone.ipynb"
                or relative.startswith("reports/checkpoints/")
                or relative.endswith(".zip")
                or not path.is_file()
            ):
                unsafe_entries.append(relative)
                continue
            content = path.read_bytes()
            if hashlib.sha256(content).hexdigest() != record["sha256"] or len(content) != record["size_bytes"]:
                mismatches.append(relative)
    required_hashed_outputs = set(FINAL_OUTPUTS) - {"reports/submission_manifest.json"}
    passed = (
        manifest.get("schema_version") == "1.0"
        and manifest.get("expected_final_commit_message") == EXPECTED_COMMIT_MESSAGE
        and manifest.get("completed_notebook_upload_required") is True
        and isinstance(records, list)
        and bool(records)
        and required_hashed_outputs.issubset(paths)
        and isinstance(safety, dict)
        and safety.get("manual_notebook_upload_required") is True
        and all(value is True for value in safety.values())
        and manifest.get("all_passed") is True
        and not mismatches
        and not unsafe_entries
    )
    return passed, {
        "files": len(records) if isinstance(records, list) else 0,
        "required_outputs_hashed": required_hashed_outputs.issubset(paths),
        "hash_or_size_mismatches": mismatches,
        "unsafe_entries": unsafe_entries,
        "manifest_self_hash_omitted": "reports/submission_manifest.json" not in paths,
        "notebook_hash_omitted": "notebooks/Rafeeq_Mini_Capstone.ipynb" not in paths,
    }


def _secret_check() -> tuple[bool, dict[str, Any]]:
    findings: list[dict[str, str]] = []
    forbidden_files: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in {".git", "__pycache__", ".ipynb_checkpoints"} for part in path.parts):
            continue
        relative = path.relative_to(ROOT).as_posix()
        lowered = path.name.casefold()
        if lowered.startswith(".env") and lowered != ".env.example":
            forbidden_files.append(relative)
        if re.search(r"(?:hidden|solution|answer[-_]?key|instructor[-_]?package)", relative, re.IGNORECASE):
            forbidden_files.append(relative)
        if path.name != ".env.example" and path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.stat().st_size > 5_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            continue
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append({"path": relative, "type": label})
    zip_present = (ROOT / "rafeeq-mini-submission.zip").exists()
    return not findings and not forbidden_files and not zip_present, {
        "configured_secret_findings": findings,
        "forbidden_files": sorted(set(forbidden_files)),
        "export_zip_committed": zip_present,
    }


def validate_submission() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def add(name: str, result: tuple[bool, dict[str, Any]]) -> None:
        passed, details = result
        checks.append({"name": name, "passed": bool(passed), "details": details})

    try:
        manifest = _load_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        manifest = {}
        manifest_error = {"error": type(exc).__name__}
    else:
        manifest_error = {}
    add("completed_notebook_structure", _notebook_check())
    add("learner_todos_14_of_14", _learner_status(manifest))
    add("six_final_outputs", _outputs_check())
    add("assessment_critical_gates", _assessment_check())
    add("trace_redaction", _trace_check())
    add("submission_manifest", _manifest_check(manifest) if manifest else (False, manifest_error))
    add("configured_secret_scan", _secret_check())
    all_passed = all(check["passed"] for check in checks)
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "validator": "learner_submission",
        "checks": checks,
        "passed": sum(bool(check["passed"]) for check in checks),
        "failed": sum(not bool(check["passed"]) for check in checks),
        "all_passed": all_passed,
    }


def main() -> int:
    report = validate_submission()
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    print(f"SUBMISSION_CHECK={'PASSED' if report['all_passed'] else 'FAILED'}")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

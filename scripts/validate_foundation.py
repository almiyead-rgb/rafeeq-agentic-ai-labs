#!/usr/bin/env python3
"""Validate the safe pre-release foundation without third-party packages."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    ".gitignore",
    ".env.example",
    "requirements-colab.txt",
    "docs/index.html",
    "docs/assets/css/styles.css",
    "docs/assets/js/app.js",
    "docs/assets/data/site-meta.json",
    "notebooks/README.md",
    "data/public/README.md",
    "src/rafeeq/README.md",
    "mcp_server/README.md",
    "tests/public/README.md",
    "tests/schemas/README.md",
    "reports/templates/README.md",
    "reports/checkpoints/.gitignore",
    "recovery/README.md",
    ".github/workflows/foundation-quality.yml",
    ".github/ISSUE_TEMPLATE/lab-help.md",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/pull_request_template.md",
)

FORBIDDEN_PUBLIC_PATH_PARTS = {
    "answer_key",
    "eval_hidden",
    "hidden_security",
    "instructor_notes",
    "recovery_checkpoint",
    "student_grades",
    "solutions",
}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}

TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        for name in ("href", "src"):
            if values.get(name):
                self.refs.append((name, values[name] or ""))


def repository_files() -> list[Path]:
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_zero_byte_files(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.stat().st_size == 0:
            errors.append(f"zero-byte file: {path.relative_to(ROOT)}")


def check_forbidden_paths(files: list[Path], errors: list[str]) -> None:
    for path in files:
        normalized_parts = {part.casefold() for part in path.relative_to(ROOT).parts}
        hits = normalized_parts & FORBIDDEN_PUBLIC_PATH_PARTS
        if hits:
            errors.append(f"forbidden public path: {path.relative_to(ROOT)} ({', '.join(sorted(hits))})")


def check_json(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.suffix.casefold() != ".json":
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)} ({exc})")


def check_secrets(files: list[Path], errors: list[str]) -> None:
    excluded = {Path("scripts/validate_foundation.py")}
    for path in files:
        relative = path.relative_to(ROOT)
        if relative in excluded or path.suffix.casefold() not in TEXT_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possible {label}: {relative}")


def check_html_references(errors: list[str]) -> None:
    html_path = ROOT / "docs/index.html"
    if not html_path.is_file():
        return
    parser = ReferenceParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    for attribute, reference in parser.refs:
        if reference.startswith(("https://", "http://", "mailto:", "tel:", "data:")):
            continue
        if reference.startswith("#"):
            anchor = unquote(reference[1:])
            if anchor and anchor not in parser.ids:
                errors.append(f"broken page anchor: {reference}")
            continue
        parsed = urlsplit(reference)
        target = (html_path.parent / unquote(parsed.path)).resolve()
        if not target.is_file():
            errors.append(f"missing local {attribute}: {reference}")


def check_release_gate(errors: list[str]) -> None:
    html_path = ROOT / "docs/index.html"
    if not html_path.is_file():
        return
    html = html_path.read_text(encoding="utf-8")
    required_markers = (
        'data-release-status="pre-release"',
        "0.1.0-alpha",
        "Pre-release",
        "إصدار تمهيدي",
        "Meaad Al-Marri",
        "ميعاد المري",
    )
    for marker in required_markers:
        if marker not in html:
            errors.append(f"missing release marker in docs/index.html: {marker}")
    if "colab.research.google.com/github/" in html:
        errors.append("active repository Colab URL is forbidden during foundation phase")


def main() -> int:
    errors: list[str] = []
    files = repository_files()
    check_required(errors)
    check_zero_byte_files(files, errors)
    check_forbidden_paths(files, errors)
    check_json(files, errors)
    check_secrets(files, errors)
    check_html_references(errors)
    check_release_gate(errors)

    if errors:
        print("FOUNDATION CHECK: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"FOUNDATION CHECK: PASSED ({len(files)} files checked)")
    print("Release gate: 0.1.0-alpha / pre-release")
    print("Active notebook/Colab publishing remains blocked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

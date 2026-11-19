#!/usr/bin/env python3
"""Lightweight offline packaging checks; no third-party dependencies."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
EXPECTED_NAME = "interaction-design-rules"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not SKILL.is_file():
        fail("Missing SKILL.md")
    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("Missing YAML frontmatter")
    parts = content.split("\n---\n", 1)
    if len(parts) != 2:
        fail("Unterminated YAML frontmatter")
    meta, body = parts
    fields = {}
    for line in meta.splitlines()[1:]:
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9-]*):\s*(.+)$", line)
        if not match:
            fail(f"Unsupported frontmatter entry: {line!r}")
        fields[match.group(1)] = match.group(2).strip('"\' ')
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        fail("Invalid skill name")
    # Repository branding (always-ui) need not match the installed skill ID.
    if name != EXPECTED_NAME:
        fail(f"Skill name must be {EXPECTED_NAME!r}")
    if not description or len(description) > 1024:
        fail("Invalid description")
    if not body.strip():
        fail("Empty skill body")
    if not (ROOT / "LICENSE").is_file():
        fail("Missing LICENSE")
    checked = 0
    for path in [SKILL, ROOT / "README.md", ROOT / "README.zh-CN.md"]:
        data = path.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", data):
            if "://" in link or link.startswith("#"):
                continue
            target = (path.parent / link.split("#")[0]).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                fail(f"Broken or out-of-root link in {path.name}: {link}")
            checked += 1
    print(f"PASS: {name}; frontmatter, LICENSE, {checked} local links")


if __name__ == "__main__":
    main()

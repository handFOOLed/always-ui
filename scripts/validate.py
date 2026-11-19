#!/usr/bin/env python3
"""Offline packaging, mode documentation and local-link checks. No dependencies."""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
EXPECTED_NAME = "always-ui"
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "references/design-archetypes.md",
    "references/check-catalog.md",
    "references/implementation-notes.md",
    "references/visual-guidance.md",
    "tests/evaluation-cases.md",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for name in REQUIRED_FILES:
        if not (ROOT / name).is_file():
            fail(f"Missing required file: {name}")

    content = SKILL.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        fail("Missing YAML frontmatter")
    parts = content.split("\n---\n", 1)
    if len(parts) != 2:
        fail("Unterminated YAML frontmatter")
    meta, body = parts
    fields: dict[str, str] = {}
    for line in meta.splitlines()[1:]:
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9-]*):\s*(.*)$", line)
        if not match:
            fail(f"Unsupported frontmatter entry: {line!r}")
        fields[match.group(1)] = match.group(2).strip("\"' ")
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        fail("Invalid skill name")
    if name != EXPECTED_NAME:
        fail(f"Skill name must be {EXPECTED_NAME!r}")
    if not description or len(description) > 1024:
        fail("Invalid description")
    for mode in ("design", "check"):
        if not re.search(rf"(?im)^##\s+Mode:\s*{mode}\s*$", body):
            fail(f"Missing {mode} mode section in SKILL.md")
        if f"$always-ui {mode}" not in content:
            fail(f"Missing {mode} invocation in SKILL.md")
    if not body.strip():
        fail("Empty skill body")

    links_checked = 0
    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        data = path.read_text(encoding="utf-8")
        for raw in re.findall(r"\[[^\]]+\]\(([^)]+)\)", data):
            if "://" in raw or raw.startswith(("#", "mailto:")):
                continue
            target_path = unquote(raw.split("#", 1)[0])
            if not target_path:
                continue
            target = (path.parent / target_path).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                fail(f"Broken/out-of-root link in {path.relative_to(ROOT)}: {raw}")
            links_checked += 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    for mode in ("design", "check"):
        for label, data in (("README.md", readme), ("README.zh-CN.md", readme_zh)):
            if f"$always-ui {mode}" not in data:
                fail(f"{label} missing $always-ui {mode} usage")

    archetypes = (ROOT / "references/design-archetypes.md").read_text(encoding="utf-8")
    checks = (ROOT / "references/check-catalog.md").read_text(encoding="utf-8")
    archetype_count = len(re.findall(r"(?m)^##\s+\d{2}\s*[—–-]", archetypes))
    check_count = len(re.findall(r"(?m)^###\s+C\d{2}\s*[—–-]", checks))
    if not 9 <= archetype_count <= 15:
        fail(f"Expected approximately 10 design archetypes; found {archetype_count}")
    if check_count < 15:
        fail(f"Expected comprehensive check anti-pattern catalog; found {check_count}")

    visual_rules = (
        "Color restraint",
        "Button hierarchy",
        "Decoration justification",
        "Component economy",
    )
    visual_reference = (ROOT / "references/visual-discipline.md")
    if not visual_reference.is_file():
        fail("Missing shared visual discipline reference")
    visual_text = visual_reference.read_text(encoding="utf-8")
    for index, rule in enumerate(visual_rules, start=1):
        if rule not in body:
            fail(f"SKILL.md missing visual rule: {rule}")
        if f"V{index:02d} — {rule}" not in visual_text:
            fail(f"Visual discipline reference missing V{index:02d}: {rule}")
        if f"C{20 + index:02d} — {rule}" not in checks:
            fail(f"Check catalog missing C{20 + index:02d}: {rule}")

    print(
        f"PASS: {name}; modes=design/check; "
        f"{archetype_count} archetypes; {check_count} checks; "
        f"{len(markdown_files)} markdown files; {links_checked} local links"
    )


if __name__ == "__main__":
    main()

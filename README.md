# Always UI

**Guardrails, not taste.**

**Always UI** is an open-source Agent Skill named `interaction-design-rules`. It helps AI coding agents prevent interaction defects **without flattening every product into the same aesthetic**.

It covers control semantics, keyboard focus and selected states, honest status feedback, expanding content, reduced motion, filename display, and native desktop window dragging. It does **not** select your palette, layout, fonts, component library, radius scale, or brand identity.

The original guidelines were written in Chinese. This open-source edition separates general interaction safeguards from optional visual preferences, preserving the original goal: tell an agent **what must not break**, not how its design must look.

## Install

This repository's **root is the skill folder**; the Skill ID is `interaction-design-rules` even though the repository is called `always-ui`.

For Codex user-level installation:

```bash
git clone https://github.com/handFOOLed/always-ui.git ~/.agents/skills/interaction-design-rules
```

For project-scoped installation, copy the repository contents into:

```text
<project>/.agents/skills/interaction-design-rules/SKILL.md
```

Do not overwrite an existing folder without reviewing local changes. Paths and invocation conventions vary by agent host; see its documentation.

In Codex, invoke `$interaction-design-rules` explicitly, or allow the host to match the skill description.

## Usage

```text
$interaction-design-rules Review the settings panel for control semantics,
visible keyboard focus, and truthful save feedback. Keep our current visual style.
```

```text
$interaction-design-rules Fix filename truncation in a narrow transfer sidebar.
Preserve useful extensions and leave stored filenames untouched.
```

Optional project instruction:

```markdown
Use $interaction-design-rules when implementing or reviewing UI interactions.
Keep the product's existing design system and only apply relevant rules.
```

## Contents

- [`SKILL.md`](SKILL.md): core guardrails and scope-first workflow.
- [`references/implementation-notes.md`](references/implementation-notes.md): conditional implementation pitfalls and examples.
- [`references/visual-guidance.md`](references/visual-guidance.md): **opt-in** visual polish, never a mandatory aesthetic.
- [`tests/evaluation-cases.md`](tests/evaluation-cases.md): ten manual agent evaluation scenarios.
- [`scripts/validate.py`](scripts/validate.py): stdlib-only packaging and link validation.

## Principles

1. **Product first:** preserve explicit product decisions, existing tokens, and design language.
2. **Interaction truth:** correct control semantics, focus visibility, and honest failure recovery.
3. **No blanket style mandates:** no universal border thickness, font-size cap, or radius scale.
4. **Load details only when needed:** conditional references avoid over-instruction.
5. **Verify honestly:** distinguish checked behavior from untested devices and assumptions.

## Validate

```bash
python scripts/validate.py
```

The validator checks file structure and links, **not** the quality of the agent's design choices. Run scenarios in [`tests/evaluation-cases.md`](tests/evaluation-cases.md) with and without the skill before claiming an improvement.

## Contributing

Issues and pull requests should focus on an **observable UI interaction problem**, a reproducible situation, and the smallest generally useful safeguard. Include an evaluation scenario for new rules. Do not turn personal taste into a universal requirement.

## License

[MIT](LICENSE) · Maintained at [handFOOLed/always-ui](https://github.com/handFOOLed/always-ui).

[简体中文](README.zh-CN.md)

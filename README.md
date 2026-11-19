# Always UI

**Design for the task. Check for the defects. Guardrails, not taste.**

**Always UI** is an open-source Agent Skill for UI design and reviews. It has two independent modes:

| Mode | Ask | Returns |
| --- | --- | --- |
| **design** | What layout and interactions fit this kind of product? | Workflow diagnosis, recommended archetype, navigation/region plan, responsive behavior, trade-offs |
| **check** | What's confusing, visually noisy, inconsistent or broken here? | Evidence-backed findings, priority, minimal improvements and verifiable acceptance criteria |

Unlike a one-style-fits-all design prompt, it avoids prescribing a brand palette, universal component library, radius scale, or aesthetic. Its objective is **good decisions without eliminating originality**.

## Quick start

The repository root is a standalone Skill folder. The Skill ID is **`always-ui`**.

### Install

Codex user-level example:

```bash
git clone https://github.com/handFOOLed/always-ui.git ~/.agents/skills/always-ui
```

Project-level example: copy/clone the repository to `<project>/.agents/skills/always-ui/`, with `SKILL.md` at that path. Do not overwrite existing customizations without review. Different Agent hosts may use different discovery paths.

### Use design mode

```text
$always-ui design Plan the main layout for a team messaging app.
Compare two desktop structures and adapt the choice for mobile.
Keep our existing purple brand identity.
```

```text
$always-ui design We are building a B2B SaaS product for sales analytics.
Analyze what users do before choosing navigation, panels and charts.
```

### Use check mode

```text
$always-ui check Review this settings screen for nested borders,
redundant selection indicators and switch/checkbox misuse.
Keep the existing look; report the top five problems.
```

```text
$always-ui check Inspect the file transfer panel. Check filename
truncation, feedback, keyboard focus and dense controls.
```

When no mode is specified, the Skill infers **design** for planning/creation and **check** for auditing/fixing an existing UI.

## Design mode — 11 workflow archetypes

The Skill evaluates the actual user workflow before selecting a layout, rather than treating every SaaS app as a dashboard.

| Family | Primary job |
| --- | --- |
| SaaS / multi-tool workspace | Resume work across modules |
| Messaging / chat | Follow conversations and reply |
| Projects / tasks | Organize items and progress |
| Analytics / monitoring | Compare data and investigate changes |
| E-commerce / marketplace | Find, evaluate and transact |
| Editor / knowledge base | Create and structure content |
| Social / community | Discover discussions and engage |
| Media / file library | Browse, preview and organize assets |
| Finance / transactions | Inspect and act on precise records |
| Admin / operations | Resolve issues and manage systems |
| Booking / services | Select resources, time and confirm |

Every archetype has fit criteria, desktop/mobile direction, important states, anti-patterns and alternatives in [`references/design-archetypes.md`](references/design-archetypes.md). Hybrids are supported; a "chat SaaS" should usually be chat-first, not dashboard-first.

## Check mode — 20 anti-patterns

Check mode looks for user-visible problems such as:

- **Frames inside frames** and redundant selection treatments (outline + checkbox + checkmark for the same state).
- **Wrong controls** — using multiple checkboxes for mutually exclusive choices, or switches for form values that aren't saved immediately.
- **Unclear hierarchy, over-decoration, bad density, inconsistent components** and too many competing primary actions.
- **Misleading save/error feedback**, invisible focus, unusable responsive views, broken motion or desktop drag behavior.

A checker labels each issue as an **actual defect**, **high-confidence design problem**, or **optional polish**. It also states what should **not** be changed. Full checks: [`references/check-catalog.md`](references/check-catalog.md).

## Repository structure

- [`SKILL.md`](SKILL.md): mode selection and shared workflow.
- [`references/design-archetypes.md`](references/design-archetypes.md): 11 task-led layout archetypes for **design**.
- [`references/check-catalog.md`](references/check-catalog.md): 20 design and interaction anti-patterns for **check**.
- [`references/implementation-notes.md`](references/implementation-notes.md): conditional technical pitfalls.
- [`references/visual-guidance.md`](references/visual-guidance.md): optional restrained/tonal style guidance (not automatically loaded).
- [`tests/evaluation-cases.md`](tests/evaluation-cases.md): manual evaluations and regression scenarios.
- [`scripts/validate.py`](scripts/validate.py): offline structure and links check.

## Migration from v0.1.0

**Breaking invocation rename:** `$interaction-design-rules` → **`$always-ui`**. Rename the installed skill folder and update your project `AGENTS.md`, prompts or scripts accordingly. The old invocation is **not** an alias; this is a deliberate unified name for repository and Skill.

The `check` mode retains the original interaction safeguards. `design` is new and does not override an approved design system.

## Verification

```bash
python scripts/validate.py
```

Static validation confirms packaging, referenced files and mode documentation. It **does not prove better Agent design ability**. Use [manual A/B cases](tests/evaluation-cases.md) to compare with and without Always UI, assess both interaction quality and creativity, and report what was actually tested.

## Contributing

Contributions should describe a real user task, a reproducible interface problem or product archetype, the expected behavior and an evaluation case. Do not promote a personal visual preference to a universal rule.

## License

[MIT](LICENSE) · [handFOOLed/always-ui](https://github.com/handFOOLed/always-ui).

[简体中文](README.zh-CN.md)

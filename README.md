# Always UI

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT License](LICENSE)

**Get the layout right. Fix what feels off.**

A chat app shouldn't be forced into a dashboard layout. And one selected item doesn't need a border, a checkbox, and another checkmark to make its point.

**Always UI** is a UI/UX skill for desktop coding agents. Want a completely different look, the right layout from scratch, or just a few fixes without changing the style? Pick how far to go. Use `check` when you only want an audit.

## What it does

### `creative` — Give it a genuinely different look

Changing purple to blue isn't a redesign. `creative` looks at the original interface, then explores a new visual direction that actually feels different—without throwing away the product's purpose, functionality or stated brand constraints.

```text
$always-ui creative Redesign this app with a distinctly different visual style.
```

### `design` — Get the layout right first

"Don't use a dropdown here. Make that a card instead." Tired of patching up a messy interface one component at a time?

**Always UI** starts with how people actually use your app. From there, it works out the navigation, page structure, information hierarchy, and layouts for different screen sizes.

It covers **11 types of interfaces**, including chat, SaaS workspaces, analytics, project management, e-commerce, editors, communities, file managers, finance, admin tools, and booking. Hybrid apps don't have to be forced into a single template.

```text
$always-ui design Help me plan the main interface for my app.
```

[See the 11 layout guides](references/design-archetypes.md) · [Browse the numeric presets](references/value-presets.md)

### `improve` — Polish it without starting over

Like the current design, but a few things feel off? `improve` keeps your layout, colors and overall personality. It fixes details like spacing, button hierarchy and unnecessary borders. **Small changes, same product.**

```text
$always-ui improve Polish this settings screen without changing its look.
```

[See how the three design levels differ](references/design-intensity.md)

### `check` — Find what looks wrong or doesn't work

Boxes inside boxes. Duplicate checkmarks. Buttons fighting for attention. Switches and checkboxes used where they don't belong…

Always UI checks **24 common UI problems**. It shows you what's wrong, why it's a problem, and the smallest change that would fix it. Your app can still have its own personality; being different doesn't make a design wrong.

```text
$always-ui check Review this page without changing its visual style.
```

[See the 24 check rules](references/check-catalog.md)

## Install

**Don't want to type commands? Just tell your coding agent:**

> Install Always UI in this project with `npx skills add handFOOLed/always-ui`, then use `$always-ui design` to help me plan the interface.

That's all it takes to get started.

**From the terminal** — run one of these in your project directory:

**Project install**

```bash
npx skills add handFOOLed/always-ui
```

**Global install**

```bash
npx skills add handFOOLed/always-ui -g
```

**Install the CLI globally with npm**

```bash
npm install -g skills
skills add handFOOLed/always-ui
```

These npm commands use the [Skills CLI](https://github.com/vercel-labs/skills) to install the skill from GitHub. Once it's installed, use `$always-ui creative`, `$always-ui design`, `$always-ui improve` or `$always-ui check` in your agent.

A real-world visual comparison: [Agent dashboard A/B case study](examples/agent-dashboard-ab/README.md).

---

Maintained by [handFOOLed](https://github.com/handFOOLed). Issues and contributions are welcome.

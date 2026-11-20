# Always UI

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT License](LICENSE)

**Get the layout right. Fix what feels off.**

A chat app shouldn't be forced into a dashboard layout. And one selected item doesn't need a border, a checkbox, and another checkmark to make its point.

**Always UI** is a UI/UX design skill for desktop coding agents. Before you start building, it helps figure out what layout actually fits your app. Afterward, it checks what looks wrong, feels awkward, or gets in the way.

## What it does

### `design` — Get the layout right first

"Don't use a dropdown here. Make that a card instead." Tired of patching up a messy interface one component at a time?

**Always UI** starts with how people actually use your app. From there, it works out the navigation, page structure, information hierarchy, and layouts for different screen sizes.

It covers **11 types of interfaces**, including chat, SaaS workspaces, analytics, project management, e-commerce, editors, communities, file managers, finance, admin tools, and booking. Hybrid apps don't have to be forced into a single template.

```text
$always-ui design Help me plan the main interface for my app.
```

[See the 11 layout guides](references/design-archetypes.md) · [Browse the numeric presets](references/value-presets.md)

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

These npm commands use the [Skills CLI](https://github.com/vercel-labs/skills) to install the skill from GitHub. Once it's installed, just enter `$always-ui design` or `$always-ui check` in your agent.

---

Maintained by [handFOOLed](https://github.com/handFOOLed). Issues and contributions are welcome.

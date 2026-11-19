# Always UI

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT License](LICENSE)

**The right layout for the job. Fewer things that feel off.**

A chat app shouldn't look like an analytics dashboard. A settings screen shouldn't need three borders and two checkmarks to show one selection.

**Always UI** is a skill for coding agents that helps with both: deciding how an interface should work, and catching the details that make it awkward to use. It works with your product's existing style instead of replacing it with another template.

## What it does

### `design` — Find the right layout

Start with what people actually do in your app, not a collection of ready-made cards. Always UI looks at the workflow and suggests a layout, navigation, content hierarchy, and responsive behavior.

It covers **11 kinds of interfaces** — chat, SaaS workspaces, analytics, project management, e-commerce, editors, social apps, file libraries, finance, admin tools, and booking — with room for hybrids.

```text
$always-ui design Plan a desktop chat app.
Compare two layouts before choosing one.
```

[Explore the layout guides](references/design-archetypes.md)

### `check` — Catch what looks or feels wrong

Borders inside borders. A checkbox and a checkmark saying the same thing. Five primary buttons. The wrong control for the job. Feedback that vanishes before you can act.

Always UI checks **20 common UI problems**, explains why they matter, and suggests small fixes. It won't call an intentional design choice a mistake just because it's unusual.

```text
$always-ui check Review this settings screen.
Look for redundant borders, selection markers, and confusing controls.
```

[Explore the check rules](references/check-catalog.md)

## Install

**Don't want to touch the terminal? Tell your coding agent:**

> Install Always UI in this project using `npx skills add handFOOLed/always-ui`, then use `$always-ui design` to plan my interface.

Allow your agent to run the install command, and you're ready to start.

**From the terminal** — run this in your project directory:

```bash
npx skills add handFOOLed/always-ui
```

Want it available across projects?

```bash
npx skills add handFOOLed/always-ui -g
```

**Prefer installing the CLI with npm?**

```bash
npm install -g skills
skills add handFOOLed/always-ui
```

These commands use the [Skills CLI](https://github.com/vercel-labs/skills), which installs the skill for supported coding agents. The project is distributed from GitHub; there's no separate `always-ui` package on npm.

Once installed, start with `$always-ui design` or `$always-ui check` in your agent.

---

Built by [handFOOLed](https://github.com/handFOOLed). Feedback and contributions are welcome.

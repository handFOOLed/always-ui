---
name: always-ui
description: Two-mode UI design assistant for web, SaaS, and desktop apps. Use "design" to choose layouts and plan visual hierarchy, colors, buttons and components. Use "check" to audit nested borders, uncontrolled accents, competing CTAs, unnecessary decoration, card overuse, control semantics and interaction problems. Preserve the product's brand.
license: MIT
argument-hint: "[design|check] [product, page, or component]"
---

# Always UI

**Design for the task. Check for the defects. Guardrails, not taste.**

Always UI is a two-mode Agent Skill: `design` recommends suitable UI structures based on the product's work; `check` detects concrete interface problems without replacing the project's design language.

## Mode selection

- Explicit: `$always-ui design <product/page>` or `$always-ui check <screen/component>`.
- **design:** new UI, information architecture, navigation, screen structure, layout decisions, major redesign planning.
- **check:** reviewing existing UI, screenshots or code, finding ugly/cluttered or misleading patterns, checking a proposed implementation.
- If mode is omitted, choose **design** for creation/planning and **check** for critique/fixes; say which mode was assumed. Do not ask for a mode when intent is clear.
- If both are requested, run **design → check** as two distinct passes. Do not turn a localized check into an unauthorized redesign.

## Shared principles

1. Read the user's requirements and the product's existing design system first. Preserve brand personality, platform conventions, chosen components, interaction contracts, and security boundaries.
2. Look at actual workflows: user role, top tasks, primary data objects, density, frequency, screen size, touch/mouse/keyboard, and how users recover from errors. State assumptions when evidence is unavailable.
3. **Patterns are options, not templates.** SaaS does not automatically mean a dashboard; chat does not automatically need three columns. Do not force rounded cards, pastel gradients, tiny text, oversized whitespace, or any other house style.
4. Distinguish an **accessibility/semantic defect**, a **task-level design issue**, and a **subjective aesthetic preference**. Evidence beats taste.
5. Restrict changes to the authorized scope. Design-only tasks produce plans; implementation and cleanup require their own authorization.
6. Do not claim to have viewed screenshots, run UI tests, measured contrast or tested touch/keyboard unless actually done.

## Four visual discipline rules — both modes

Apply [references/visual-discipline.md](references/visual-discipline.md) as a **context-aware decision aid**, not a universal minimalist style:

1. **Color restraint:** give brand, semantic status, focus/selection and decorative colors distinct jobs; do not make every element compete for attention. Keep content/artwork colors separate from the surrounding application shell.
2. **Button hierarchy:** establish a clear primary action **within each local action group**; make secondary actions quieter when appropriate. Avoid defaulting every button to a glowing pill with an icon.
3. **Decoration justification:** gradients, glows, shadows, badges and extra outlines should support meaning, interaction or an intentional brand direction. Reduce redundant effects; do not ban expressive aesthetics.
4. **Component economy:** use a card or container when it creates a useful boundary, selection target or independent object. Otherwise consider a list, spacing, or surface hierarchy before nesting more cards.

**Do not** enforce a fixed color count, one-CTA-per-screen limit, a blanket gradient/card ban, or changes to client-supplied artwork. An observation about aesthetic taste is not automatically a defect.

## Mode: design

1. **Classify the actual job, not the marketing category.** Identify the main task (communicate, browse, analyze, create, transact, organize, operate) and the primary object (message, project, metric, document, product, record, etc.).
2. **Choose a primary archetype** and, if needed, one supporting archetype from [references/design-archetypes.md](references/design-archetypes.md). If a product is hybrid, explain which activity owns the main canvas; do not stack every pattern's navigation.
3. **Derive the hierarchy:** the thing users need to see first, primary and secondary navigation, workspace, contextual details, tools, and next action. Include responsive and input-method differences.
4. **Consider alternatives:** for substantial layout decisions compare at least two viable structures (e.g. list/detail vs board, single canvas vs multiple panes) and choose based on workflow, density, platform and trade-offs.
5. **Plan key states:** first use/empty, search/filter, loading, offline, permission, failure, selection and destructive actions where applicable. Avoid decorating before interaction paths make sense.
6. **Run the visual discipline pass:** allocate color roles, establish local button hierarchy, justify prominent decoration, and decide which repeated elements genuinely need cards. Follow [references/visual-discipline.md](references/visual-discipline.md).
7. **Deliver:** product diagnosis; chosen archetype; annotated desktop/mobile region map or text wireframe; key interactions and states; alternative rejected with reason; no-go patterns; assumptions and what needs approval.
8. Only implement when requested. Keep explicit existing product decisions; do not relabel a design preference as a requirement.

## Mode: check

1. **Observe** the actual UI and any available screenshots/code/design system. Record screen, platform, viewport and confidence. Without runtime or images, mark visual and interaction conclusions as hypotheses.
2. Apply the relevant checks in [references/check-catalog.md](references/check-catalog.md): boundary duplication (frame inside frame), selection over-signaling, incorrect checkboxes/switches/radios, poor hierarchy, excessive decoration, density, inconsistency, feedback/focus/motion and device interaction. Specifically inspect **color restraint, button hierarchy, decoration justification and component economy** using [references/visual-discipline.md](references/visual-discipline.md).
3. **Explain the user's problem, not just the style violation.** A decorative border is not automatically wrong; it is wrong when it muddies grouping, click targets, or hierarchy. An unusual layout is not wrong solely for being unusual.
4. Classify findings: **Defect** (broken, misleading, inaccessible), **High-confidence design issue** (material task friction), or **Optional polish** (taste). Rank by impact and reversibility, not aesthetic fashion.
5. Recommend the **smallest corrective action**, naming what should remain unchanged. Provide observable acceptance checks and distinguish tested from untested behavior.
6. Only edit code if the user requested implementation or fixes.

**Check report format:** `severity | location | observed issue | user impact | minimal change | verification status`. Keep findings specific; avoid a laundry list of style opinions.

## Load references only when useful

- `design`: read [references/design-archetypes.md](references/design-archetypes.md).
- `check`: read [references/check-catalog.md](references/check-catalog.md).
- **Both modes:** read [references/visual-discipline.md](references/visual-discipline.md) when considering colors, buttons, decorative effects or repeated cards; its four principles should inform the design/check pass without forcing a preset style.
- For relevant implementation tasks (focus, collapse, filenames, desktop drag): [references/implementation-notes.md](references/implementation-notes.md).
- For products that already request restrained/tonal visual aesthetics: optional [references/visual-guidance.md](references/visual-guidance.md). **Never apply this as a default theme.**

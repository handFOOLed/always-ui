---
name: always-ui
description: Two-mode UI design assistant for web, SaaS, and desktop apps. Use "design" for layouts, hierarchy, visual discipline and preset numeric token scales. Use "check" for nested borders, uncontrolled colors, competing CTAs, arbitrary spacing or typography, card overuse, control semantics and interaction defects. Preserve existing design tokens and brand.
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

## Reference-first workflow — mandatory

**Read the relevant Always UI reference files before deciding, generating, changing or reviewing UI.** These files are the Skill's instructions, **not optional inspiration**. Do not skip them and improvise from memory. Follow the documented classifications, checks and numeric tables rather than inventing your own rules.

| Mode | Required references, read first | What to take from them |
| --- | --- | --- |
| `design` | [design-archetypes.md](references/design-archetypes.md), [value-presets.md](references/value-presets.md), [visual-discipline.md](references/visual-discipline.md) | Classify the workflow, select and justify a layout, reuse existing tokens or choose documented numeric presets, and control color/button/decorative/component hierarchy |
| `check` | [check-catalog.md](references/check-catalog.md), [visual-discipline.md](references/visual-discipline.md), [value-presets.md](references/value-presets.md) | Assess applicable documented anti-patterns, distinguish UI shell from content, and detect numeric drift **against project tokens first** |
| `design + check` | Both sets above | Complete the design pass and then the check pass without treating either as optional |

**Also read the project's design system, existing components and tokens.** Precedence is: user requirements, safety/accessibility/platform constraints and established product design decisions → project tokens and interaction contracts → Always UI's applicable guidelines and fallback numeric tables. If sources disagree, disclose the conflict and preserve the higher-priority requirement. Do not substitute a new aesthetic for the product's own visual identity.

- **Before implementation:** use the selected layout guidance and documented scale; inspect the project's current tokens before writing any new fixed value.
- **Before review:** consult the actual check catalog and report only issues grounded in visible UI/code and applicable rules. Do not use the fallback table to criticize a consistent existing scale.
- **Technical details:** when implementing or assessing focus rings, expansion, filename rendering or native drag regions, **read** [implementation-notes.md](references/implementation-notes.md) before deciding how to handle that behavior.
- **Optional style, by design:** [visual-guidance.md](references/visual-guidance.md) is **only** for products that explicitly choose its restrained/tonal aesthetic; it must not become the default look.
- If required files cannot be accessed, **say which references were unavailable** and do not claim a fully Skill-guided design/check. Request or retrieve the files instead of silently replacing their guidance with guesswork.

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

## Numeric presets — design must choose from tables

When selecting fixed UI design values, follow [references/value-presets.md](references/value-presets.md) **before writing styles**. Read the reference during `design` and any newly implemented UI work.

- **First:** find and use the existing project's design tokens, UI library scales and platform metrics; never overwrite them with Always UI defaults.
- **If missing:** choose values from the category-specific tables for spacing/sizing, type/weight/line-height, radius/borders, icons/control heights, alpha/color stops, elevation, motion, breakpoints and layers. Give reused choices semantic tokens.
- **Do not improvise:** `17px` padding, `23px` gap, new shadow recipes, arbitrary Tailwind values or other unlisted fixed design numbers because they "look right." Inspect generated CSS/styles for numeric drift before completing the task.
- **Exceptions:** intrinsic/fluid sizes, asset geometry, user-specified sizes, accessibility/platform requirements and content-driven constraints may require values outside the tables. State the reason, and keep the exception deliberate rather than silently creating another scale.
- Do not turn these presets into a global aesthetic or a numeric limit on brand colors. The rules constrain *measurements*, not product personality.

## Mode: design

1. **Classify the actual job, not the marketing category.** Identify the main task (communicate, browse, analyze, create, transact, organize, operate) and the primary object (message, project, metric, document, product, record, etc.).
2. **Choose a primary archetype** and, if needed, one supporting archetype from [references/design-archetypes.md](references/design-archetypes.md). If a product is hybrid, explain which activity owns the main canvas; do not stack every pattern's navigation.
3. **Derive the hierarchy:** the thing users need to see first, primary and secondary navigation, workspace, contextual details, tools, and next action. Include responsive and input-method differences.
4. **Consider alternatives:** for substantial layout decisions compare at least two viable structures (e.g. list/detail vs board, single canvas vs multiple panes) and choose based on workflow, density, platform and trade-offs.
5. **Plan key states:** first use/empty, search/filter, loading, offline, permission, failure, selection and destructive actions where applicable. Avoid decorating before interaction paths make sense.
6. **Choose numeric tokens from tables:** audit the existing token system; if absent, pick fixed values only from [references/value-presets.md](references/value-presets.md). Apply scale consistently; record justified exceptions instead of making up ad-hoc numbers.
7. **Run the visual discipline pass:** allocate color roles, establish local button hierarchy, justify prominent decoration, and decide which repeated elements genuinely need cards. Follow [references/visual-discipline.md](references/visual-discipline.md).
8. **Deliver:** product diagnosis; chosen archetype; annotated desktop/mobile region map or text wireframe; key interactions and states; chosen token scales (when newly defined); alternative rejected with reason; no-go patterns; assumptions and what needs approval.
9. Only implement when requested. Keep explicit existing product decisions; do not relabel a design preference as a requirement.

## Mode: check

1. **Observe** the actual UI and any available screenshots/code/design system. Record screen, platform, viewport and confidence. Without runtime or images, mark visual and interaction conclusions as hypotheses.
2. Apply the relevant checks in [references/check-catalog.md](references/check-catalog.md): boundary duplication (frame inside frame), selection over-signaling, incorrect checkboxes/switches/radios, poor hierarchy, excessive decoration, density, inconsistency, feedback/focus/motion and device interaction. Specifically inspect **color restraint, button hierarchy, decoration justification and component economy** using [references/visual-discipline.md](references/visual-discipline.md). Where numeric inconsistency matters, compare values against the **existing project tokens** first, then the fallback [value presets](references/value-presets.md) only for newly introduced scales. Do not treat a coherent established scale as a defect simply because its numbers differ.
3. **Explain the user's problem, not just the style violation.** A decorative border is not automatically wrong; it is wrong when it muddies grouping, click targets, or hierarchy. An unusual layout is not wrong solely for being unusual.
4. Classify findings: **Defect** (broken, misleading, inaccessible), **High-confidence design issue** (material task friction), or **Optional polish** (taste). Rank by impact and reversibility, not aesthetic fashion.
5. Recommend the **smallest corrective action**, naming what should remain unchanged. Provide observable acceptance checks and distinguish tested from untested behavior.
6. Only edit code if the user requested implementation or fixes.

**Check report format:** `severity | location | observed issue | user impact | minimal change | verification status`. Keep findings specific; avoid a laundry list of style opinions.

## Before you finish

- **`design`:** confirm that the chosen archetype, numeric decisions and visual discipline were grounded in the **required references**, not made up on the fly. Name the project's existing token system or the chosen fallback scale when relevant.
- **`check`:** confirm the reported issues map to the documented catalog or evidence-backed design principles; explain valid exceptions rather than manufacturing complaints.
- **Both:** preserve the project's own style, distinguish verified behavior from assumptions, and do not claim to have consulted unread or inaccessible files.

---
name: interaction-design-rules
description: Audit or implement interaction details in web and desktop app interfaces. Use for control semantics, focus and selection states, feedback, expandable content, motion, filenames, or desktop window drag regions. Preserve the product's design language; do not use this skill to choose its aesthetic or redesign unrelated screens.
license: MIT
---

# Interaction Design Rules

**Guardrails, not taste.** Prevent interaction defects without turning every product into the same UI.

## Scope and authority

- Apply only to the page, component, platform, and states involved in the user's request. Do not perform a site-wide redesign or add features to satisfy this skill.
- Read the product's existing design system, interaction contracts, tokens, and components first. Preserve deliberate visual choices. This skill does not choose a palette, typeface, radius system, layout, or brand personality.
- Product requirements and explicit user decisions govern visual identity. Accessibility, accurate state, privacy/security disclosure, and platform behavior must not be weakened to fit a visual preference.
- Classify relevant rules as **applicable**, **not applicable**, or **conflicting** before changes. Explain material conflicts rather than silently overriding the product.

## Interaction guardrails

### Controls should express the actual state model

- **Switch:** an independent on/off setting that normally takes effect when toggled. Do not use for a pending form decision unless the surrounding product explicitly defines that behavior.
- **Checkbox:** independent choices, multi-select, or an explicit acknowledgment later submitted with a form.
- **Radio group / segmented control:** mutually exclusive choices; use segmented controls only when the options and available space make them practical.
- **Select / combobox:** choosing value(s) from a set. Show the current value or an honest placeholder; distinguish selection from executing a command.
- **Menu:** commands such as rename, download, or delete; avoid presenting commands as stored values.
- **Button:** an action, not a persistent setting. Do not add redundant selection symbols, nested click targets, or multiple independent cues that communicate exactly the same state.

### Focus, selection, and boundaries

- Make keyboard focus **visible and distinguishable** from persistent selection, hover, and error states. Never remove the browser/platform focus indicator without providing an equally robust alternative, including high-contrast/forced-colors behavior.
- Prefer tonal surfaces, spacing, and alignment over repeated card borders. Use an outline or divider when it clarifies grouping, targeting, or focus; avoid border-inside-border decoration for the same boundary.
- If controls or corners nest, align their geometry so their boundaries look intentional. Do not impose one radius, border thickness, or shadow recipe across a product with an existing design system.
- Preserve readable contrast and do not convey connection, permission, error, or destructive status using color alone.

### Honest feedback and content

- Show pending, success, and failure feedback only when those states are real. Keep actionable failures visible until resolved or dismissed; do not invent successful completion.
- Place relevant feedback near the originating action, keep messages specific, and announce asynchronous updates accessibly when appropriate. Avoid repetitive helper prose when the interface already explains itself.
- In constrained file lists, prefer preserving a meaningful extension while shortening the basename; keep the original filename available for inspection and copying. Handle extensionless files, dotfiles, long extensions, and bidirectional names without changing the stored filename.
- Use tabular numerals where aligned values, timers, counters, or changing figures would otherwise shift. Do not apply tabular numerals to every text run by default.

### Motion and platform behaviors

- Make expansion/collapse respond to actual content size. Prefer layout-native transitions when they work reliably; avoid per-frame JavaScript height writes merely for visual motion. Do not mandate a particular CSS technique when the platform or content requires another approach.
- When hidden or collapsed, interactive descendants must not remain in the keyboard tab sequence. Preserve semantic expanded/collapsed state and check dynamic content, rapid reversal, and resize.
- Keep drawers responsive when opening, closing, or reversing; provide immediate/low-motion behavior when reduced motion is requested.
- On desktop apps with a custom titlebar, use host-supported window drag regions only on noninteractive surfaces. Buttons, text selection, inputs, scrolling, and resizing must remain usable. Do not add window-drag rules to ordinary web pages.

## Working procedure

1. **Inspect:** Identify target surfaces, states, input methods, existing tokens, accessibility conventions, and test availability.
2. **Prioritize:** Find observable interaction defects. Distinguish **must fix** (broken semantics, inaccessible focus, misleading state, blocked interaction) from **suggestions** (polish and visual economy).
3. **Change minimally:** Fix only relevant defects in the authorized scope. Reuse established components. Avoid blanket restyling, new dependencies, or arbitrary pixel constants.
4. **Verify:** Check rest, hover, focus, selected, disabled, pending, success, failure, keyboard and touch where applicable. Test reduced motion, high contrast, narrow widths, dynamic content, and platform-specific behaviors only where relevant. Do not claim tests you did not perform.
5. **Report:** For each meaningful finding, state **location → observed issue → violated principle → minimal fix → verification status**. Note remaining device-dependent tests as unverified.

## Conditional references

- For implementation pitfalls and examples involving focus rings, responsive filenames, CSS expansion, and desktop drag areas, read [references/implementation-notes.md](references/implementation-notes.md) **only when those tasks apply**.
- For an **opt-in** minimal/tonal visual treatment (surface hierarchy, concentric corners, double-ring focus, typography), read [references/visual-guidance.md](references/visual-guidance.md) **only when the user or product already wants that style**. It is not a default visual system.

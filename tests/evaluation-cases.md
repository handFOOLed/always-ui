# Always UI evaluation scenarios — design and check

Use these as **behavioral evaluations**, not merely text-matching tests. Run the explicit `$always-ui design` or `$always-ui check` invocation when stated. Run the same task on a small sample app with and without the skill. Examine changed code, interaction recordings, and the agent's final report. The agent must not claim an interaction was tested unless actually exercised.

## Check-mode regression cases (existing safeguards)

| ID | Task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| S01 | "Fix an input whose focus is hard to see, but keep our current design." | Visible keyboard focus, distinguishable from selection; forced-colors consideration; no redesign | Replaces all fields with a personal style or removes `outline` |
| S02 | "Settings page: notifications take effect immediately; privacy choice is saved on Submit." | Switch for immediate notifications; appropriate form control for saved decision | Uses switches indiscriminately |
| S03 | "Make this upload card less noisy while preserving upload failure recovery." | Removes redundant helper text but keeps actionable error and retry | Hides failure after a timer, invents success |
| S04 | "Show long filenames in a narrow transfer list." | Keeps meaningful extension visible, full name retrievable; handles dotfiles | Truncates `.pdf`, changes saved name |
| S05 | "Animate an accordion containing a form and async content." | Respects `aria-expanded`, collapsed focus removal, reduced motion, dynamic height | Only animates height; hidden controls still tabbable |
| S06 | "Fix window dragging in a custom desktop titlebar." | Blank host-backed regions drag; input/buttons/scroll interactions work | `drag` applied indiscriminately to controls |
| S07 | "Audit this dark private-chat window using our existing fonts." | Assesses optical weight only when relevant, does not require weight 360 | Unconditionally applies `font-weight: 360` |
| S08 | "Design a playful neon music app from scratch." | Respects the neon visual direction; only raises applicable interaction defects | Forces muted lavender, minimal cards or four font sizes |
| S09 | "Review a mobile web app; there is no desktop shell." | Skips native desktop drag rules | Adds drag-region CSS to webpage |
| S10 | "Review our bilingual Chinese/English toggles." | Prioritizes semantic and localized clarity over hard character counts | Truncates labels to six Chinese characters |


## Design-mode evaluation cases

| ID | Task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| D01 | `$always-ui design Build an internal chat SaaS where most users send messages all day.` | Chooses Messaging as primary archetype, SaaS hub secondary at most; composer and conversation canvas dominate | Generic SaaS dashboard with four KPIs and hero |
| D02 | `$always-ui design Design a live operations monitoring console with alerts and metrics.` | Explains data freshness, alerts, period/filters, drilldowns and high-density desktop vs mobile triage | Pretty charts without timestamps/units/actions |
| D03 | `$always-ui design Design a writing-first knowledge editor for desktop and phone.` | Writing canvas primary, contextual tools, visible save state, focused mobile adaptation | Permanent three sidebars or editor shrunk onto phone |
| D04 | `$always-ui design Design a project tool for dependent tasks and deadlines; compare layouts.` | Compares list/board/timeline based on workflow and dependencies, selects a primary | Automatically mandates Kanban |
| D05 | `$always-ui design Design an asset library with 3000 mixed documents and photos.` | Chooses grid for visual media, list for name-heavy assets or switches; supports search/filter/preview | Uniform thumbnail wall hiding file names/types |
| D06 | `$always-ui design Build a playful, high-energy music community app.` | Uses Social as primary and Media as secondary; respects expressive aesthetic | Forces muted minimalism, grayscale, giant cards |
| D07 | `$always-ui design Build an appointment booking site with real-time availability.` | Stepwise availability/selection/review, honest time zones and confirmed vs pending | Static calendar cards that imply unverified slots |
| D08 | `$always-ui design Build financial reconciliation software for experienced accountants.` | Table/ledger-first, numeric precision, batch review, permissions; no excessive whitespace | Mobile-style oversized cards on desktop |
| D09 | `$always-ui design Build a moderation admin panel and a mobile companion.` | Desktop record triage, audit/actions; mobile priority alerts only | Same dense table forced on phone |
| D10 | `$always-ui design Plan a marketplace for comparing specialist hardware specifications.` | Comparison-first search/catalog/table, not image-only cards; clear availability | Fashion-shop template with little technical info |
| D11 | `$always-ui design Design a SaaS tool with no more detailed product requirements.` | States assumptions and variants; does not assert one mandatory layout | Invents users, KPI needs, and feature requirements |
| D12 | `$always-ui design Keep our established brand and existing app navigation; redesign only onboarding.` | Preserves approved navigation/theme; scopes onboarding flow | Replaces entire design system and brand |

## Check-mode visual and semantic anti-pattern cases

| ID | Task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| C01 | `$always-ui check A list item has an outer outline, inner outlined panel and outlined action button.` | Flags needless same-purpose nesting only where it hurts hierarchy; retains needed focus boundaries | Bans all borders universally |
| C02 | `$always-ui check A chosen card shows an outline, checkbox and checkmark, but also has keyboard focus.` | Removes redundant selected signals while preserving distinct keyboard focus | Removes focus ring as “extra line” |
| C03 | `$always-ui check A single-choice subscription plan uses three checkboxes.` | Identifies semantic mismatch, recommends radio/selection pattern | Merely changes colors |
| C04 | `$always-ui check A security consent form uses a switch that changes appearance but saves only on Submit.` | Distinguishes pending form intent, suggests appropriate checkbox or explicit state explanation | Assumes switch means immediate persistence |
| C05 | `$always-ui check This bold, playful landing page uses intentionally high contrast and graphics.` | Does not label expressive style defective absent evidence of interference | Declares all gradients, shadows and large type bad |
| C06 | `$always-ui check Screenshot only: review keyboard behavior and animated drawer focus.` | Clearly labels untested keyboard/animation claims, suggests runtime checks | Fabricates PASS based on screenshot |
| C07 | `$always-ui check A desktop custom titlebar cannot drag over empty sidebar, but text remains selectable.` | Recommends host drag region on blank surface, preserves text controls | Applies drag to entire panel |
| C08 | `$always-ui check Existing settings have three Save buttons of equal visual weight.` | Examines local action hierarchy and scopes a minimal fix | Globally restyles all buttons |
| C09 | `$always-ui check Error toast disappears before the user can retry a failed transfer.` | Treats as actionable state defect with persistent recovery | Replaces with a prettier transient toast |
| C10 | `$always-ui check A deliberately dense financial table uses minimal padding.` | Checks readability, alignment and interaction before recommending density change | Calls dense UI ugly on sight |

## Visual discipline regression cases (from the Handoff A/B experiment)

These cases test the **four new rules in both modes**. Compare the application's own UI separately from a previewed client's artwork, and check for false positives as well as missing critiques.

| ID | Mode / task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| V01-D | `$always-ui design Build a creative delivery workspace with a bright client mockup in the main preview.` | Gives shell colors clear roles; leaves the client's bright preview unchanged; avoids oversaturating passive controls | Treats the artwork's colors as UI defects, recolors user content, or makes every shell element glow |
| V01-C | `$always-ui check The shell uses vivid purple for navigation, red for routine tabs, cyan for secondary buttons, and green for selected file cards. The preview is a colorful automotive dashboard.` | Flags competing **shell** accents where their roles overlap, preserves semantic colors and the preview | Counts the preview's gradient as an application-shell error or bans multiple colors |
| V02-D | `$always-ui design Plan actions for a file-review screen: Deliver in the header; Reply in the comment composer; Upload revision in file details.` | Defines local primary actions for distinct workflows and quieter utilities; does not insist on one CTA across entire screen | Makes all three huge glowing pills or prohibits multiple local primary actions |
| V02-C | `$always-ui check A settings form has three filled violet buttons (Save, Reset, Help) and a tooltip icon beside every label.` | Prioritizes Save in the local form, de-emphasizes secondary actions, judges icon usefulness | Removes focus/click affordance or blindly bans pill buttons |
| V03-D | `$always-ui design Build an expressive music app that uses gradients and playful motion as deliberate brand elements.` | Preserves requested expressiveness, uses effects with clear hierarchy and reduced-motion support | Enforces grayscale/flat design or indiscriminate glows on every control |
| V03-C | `$always-ui check A dashboard has gradient buttons, glowing icons, shadows and borders on almost every toolbar item. A central artwork has its own gradient.` | Critiques unhelpful chrome effects with specific reasons, leaves embedded artwork alone | Declares all gradients bad, including the artwork |
| V04-D | `$always-ui design Display 70 version comments, with reply and resolve actions per comment.` | Considers compact rows/shared panel versus cards; retains useful per-comment actions and selection | Wraps each comment and reply in multiple decorated cards without purpose |
| V04-C | `$always-ui check Every file in a homogeneous list has an outer card, inner card and outlined pill, but a separate draggable asset grid uses distinct cards as drag targets.` | Simplifies only the list's redundant containers; keeps drag cards with a real interaction role | Bans every card or removes needed drag/focus targets |
| V-KEEP | `$always-ui check The app is intentionally maximalist, with semantic status colors and accessible focus outlines. Explain what must stay.` | Reports only evidenced problems, identifies valid brand/status/focus exceptions and what to keep | Recommends a blanket muted theme or removes focus indicators |

When possible, rerun the **same Handoff brief and same mockup content** with and without this change. Score whether the agent improves visual hierarchy **without** removing the product's personality, semantic signals, or the client's preview content. These are planned manual cases, not completed Agent results.

## Numeric preset selection tests

These test whether the agent actually **selects from the tables** rather than merely mentioning them. Run with `$always-ui design` or `$always-ui check`. Inspect generated styles, not just its explanation.

| ID | Task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| P01 | `$always-ui design Create a new settings screen. The project has no CSS variables or design tokens.` | Defines/reuses named tokens for spacing, font sizes, radii, borders and button height, with values from the correct [preset tables](../references/value-presets.md) | Invents `padding: 17px`, `gap: 23px`, `border-radius: 13px` or random shadow values |
| P02 | `$always-ui design Add a profile panel to a project already using spacing tokens 6/12/18/30px.` | Reuses the project's **existing** scale, even though several values differ from the fallback; no parallel token family | Rewrites app spacing to the Always UI fallback |
| P03 | `$always-ui design Build a compact desktop issue triage list and a touch-friendly mobile action sheet.` | Selects permitted control heights and icon sizes appropriate to each input method, maintaining accessibility | Uses 28px touch targets or invents an unlisted height |
| P04 | `$always-ui design Add a modal, hover states, and a drawer to a product with no elevation/motion tokens.` | Uses named elevation **whole presets**, consistent durations from motion table; reduced motion supported | Makes a different arbitrary shadow/duration for every element |
| P05 | `$always-ui design Design a page using the company's custom brand red and client-provided neon images.` | Preserves actual brand/artwork; chooses numerical sizes from preset tables; does not replace color identity with generic purple | Treats the color ramp stop table as a mandate to generate brand HEX values |
| P06 | `$always-ui design Show a supplied image exactly at 1170 × 2532 within a responsive editor and preserve its geometry.` | Preserves intrinsic media ratio/asset values while using layout tokens for surrounding UI | Rounds image dimensions to the nearest spacing preset |
| P07 | `$always-ui check The existing design system consistently uses 18px spacing; a new component uses 19px once.` | Identifies drift relative to the **project's existing** tokens; recommends the existing 18px token rather than blindly adopting 16px | Calls 18px invalid because it isn't an Always UI spacing value |
| P08 | `$always-ui design Build a page that uses 16px body and 24px headings but relies on system text scaling.` | Uses supported size steps as defaults, allows OS/user zoom and accessible overrides | Hard-codes fixed text metrics that defeat user scaling |
| P09 | `$always-ui design Create a new responsive app with six candidate breakpoints in the table, but only one layout change needed.` | Uses only a breakpoint justified by the actual content, rather than emitting six media queries | Makes every listed preset a mandatory breakpoint |

These are manual cases until exercised with actual Agent runs. The packaging validator checks file references and table structure; it cannot assert that an external agent used the values correctly.

## Reference-first workflow regression cases

These verify that the reference material is used **before** design/review decisions, not simply linked at the end of the answer. Inspect whether outputs follow the documented archetypes, preset values and check rules.

| ID | Task prompt | Expected behavior | Common failure |
| --- | --- | --- | --- |
| R01 | `$always-ui design Plan a new chat app with no design tokens.` | Consults archetype, value-presets and visual-discipline references before choosing regions, values or button/color hierarchy | Skips the files; invents a generic dashboard and arbitrary 17px/23px values |
| R02 | `$always-ui check Audit the existing settings screen with 19px row gaps and 3px radii; the project tokens explicitly define these values.` | Reads check catalog, visual discipline and presets; preserves consistent project tokens, only reports evidenced problems | Calls project values incorrect merely because they are outside fallback preset tables |
| R03 | `$always-ui check Review a file panel with truncated names and a nested reply region; suggest fixes.` | Uses the catalog and, for actual implementation guidance, relevant technical notes before proposing changes | Makes up a new truncation algorithm without consulting the file guidance |
| R04 | `$always-ui design Create an expressive colorful festival website with its own established design system.` | Reads required references and existing design system; preserves expressive identity and relevant tokens | Loads optional tonal visual guidance as a mandatory minimal/gray theme |
| R05 | `$always-ui design The referenced Skill files are not accessible in this environment; proceed anyway.` | Explicitly reports unavailable files and limits claims; seeks/retrieves actual references rather than pretending to have read them | Falsely asserts that it applied the references |
| R06 | `$always-ui design and check Plan a small task manager and audit the result.` | Reads both mode reference sets and performs distinct design → check passes | Executes a vague single-pass opinion without consulting catalog or presets |

These are planned manual tests; file presence checks cannot establish that an external coding Agent actually read the references.

## A/B evaluation protocol

1. Use the **same product brief, model, thinking budget, source revision, and test environment** across skill-off, `design` and `check` conditions. Include a visually expressive control case to detect over-standardization.
2. For **design**, score 0–2: task diagnosis, justified layout alternatives, useful responsive/states, preservation of user identity and creative range, scope discipline.
3. For **check**, score 0–2: defect accuracy, false-positive avoidance, smallest plausible fix, accessibility/semantics correctness, verification honesty.
4. Prefer human/observed interaction review to self-scoring. Inspect changed code and UI captures. Mark untested aspects, not “passed.”
5. Document failures, regressions, and what improved. Static link validation is **not** an A/B result.

## Original check-case scoring guidance

Score each run 0–2 on (a) defect identified/fixed, (b) preservation of the requested product aesthetic and task scope, (c) accessibility/state correctness, and (d) honest verification reporting. Compare the skill-on and skill-off runs, inspect regressions, and revise rules that systematically lower score (b) without improving (a) or (c). Do not claim measured quality improvements without running the cases.

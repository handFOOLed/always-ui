# Manual agent evaluation scenarios

Use these as **behavioral evaluations**, not merely text-matching tests. Run the same task on a small sample app with and without the skill. Examine changed code, interaction recordings, and the agent's final report. The agent must not claim an interaction was tested unless actually exercised.

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

## Scoring guidance

Score each run 0–2 on (a) defect identified/fixed, (b) preservation of the requested product aesthetic and task scope, (c) accessibility/state correctness, and (d) honest verification reporting. Compare the skill-on and skill-off runs, inspect regressions, and revise rules that systematically lower score (b) without improving (a) or (c). Do not claim measured quality improvements without running the cases.

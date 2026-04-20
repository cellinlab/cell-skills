# Question Protocol

> **Load when:** Understand step (step 1) when the user's scope is unclear, ambiguous, or incomplete
> **Skip when:** User gave a complete spec (format, fidelity, content, constraints all specified)
> **Why it matters:** Without structured questions, AI asks vague "what do you want?" prompts that waste turns. Structured questions converge scope in 1-2 rounds.
> **Typical failure it prevents:** 5+ rounds of back-and-forth clarification; building the wrong thing because key constraints were never asked about

## Question Groups

Ask these in order. Skip any group where the user already provided the answer. Use concise, concrete questions with 2-4 options when the host supports structured choice prompts; otherwise ask the equivalent in plain language.

### Group 1: Output format

| Question | Options | Why |
|----------|---------|-----|
| What format should this be? | A) Slide deck (1920x1080 fixed canvas) / B) Landing page (responsive) / C) Mobile screen mockup / D) Interactive prototype | Determines routing, template, and scaling rules |
| How many screens/slides? | A) 1-3 / B) 4-8 / C) 10+ | Affects navigation complexity and file structure |
| Fidelity level? | A) Wireframe (layout only) / B) Medium (real copy, placeholder images) / C) High-fidelity (pixel-level) | Determines effort and asset requirements |

### Group 2: Visual direction

| Question | Options | Why |
|----------|---------|-----|
| Visual mood? | A) Minimal / clean / B) Bold / vibrant / C) Warm / friendly / D) Technical / precise | Maps to font + color choices in frontend-design.md |
| Brand or reference? | A) I have a brand guide / B) I have a reference URL / C) Start from scratch | Determines whether to reuse existing design system |
| Dark or light mode? | A) Light / B) Dark / C) Both (toggle) | Affects contrast calculations and asset preparation |

### Group 3: Technical constraints

| Question | Options | Why |
|----------|---------|-----|
| Needs to be responsive? | A) Fixed size only / B) Responsive (mobile + desktop) | Fixed-size uses deck_stage scaling; responsive uses CSS breakpoints |
| Export needed? | A) Just preview / B) PPTX / C) PDF / D) Self-contained HTML | Loads platform-tools.md for export scripts |
| Accessibility requirements? | A) Standard (readable text) / B) WCAG AA / C) WCAG AAA | Affects contrast ratios, hit targets, alt text |

## Convergence Rule

After asking Group 1-3, you should have enough to route and build. If scope is still unclear after one round of questions, ask one targeted follow-up, then proceed with the best assumption. Do not ask more than 2 rounds total.

## Assumption Defaults

When the user skips a question, apply these defaults:

| Unanswered | Default |
|------------|---------|
| Format | Slide deck (most common) |
| Fidelity | Medium |
| Visual mood | Minimal (lowest risk of AI slop) |
| Brand | Start from scratch + frontend-design.md |
| Responsive | Fixed size |
| Export | Just preview |
| Accessibility | Standard |

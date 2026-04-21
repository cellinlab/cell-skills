# Question Protocol

> **Load when:** Understand step (step 1) when the user's scope is unclear, ambiguous, or incomplete
> **Skip when:** User gave a complete spec (format, fidelity, content, constraints all specified)
> **Why it matters:** Without structured questions, AI asks vague "what do you want?" prompts that waste turns. Structured questions converge scope in 1-2 rounds.
> **Typical failure it prevents:** 5+ rounds of back-and-forth clarification; building the wrong thing because key constraints were never asked about

## Question Groups

Ask these in order. Skip any group where the user already provided the answer. Prefer one batched question set instead of a back-and-forth drip feed.

### Group 1: Design Context

| Question | Options | Why |
|----------|---------|-----|
| Is there an existing design system, UI kit, token file, or codebase? | A) Yes, reuse it / B) Only screenshots or references / C) No, start fresh | Decides whether to reuse or fall back |
| Do we have brand assets or reference material? | A) Brand guide / B) URL or screenshots / C) Specific brand to study / D) Nothing yet | Routes to `design-context.md` and possibly `brand-asset-protocol.md` |
| Does the task mention a real product or brand? | A) Yes, specific product / B) Yes, general brand style / C) No | Determines whether fact verification and asset protocol are needed |

### Group 2: Deliverable Shape

| Question | Options | Why |
|----------|---------|-----|
| What format should this be? | A) Slide deck / B) Landing page / C) Mobile mockup / D) Interactive prototype / E) Visual direction only | Determines routing, template, and verification style |
| How many screens or directions? | A) 1-3 / B) 4-8 / C) 10+ | Affects build strategy and scope |
| Fidelity level? | A) Wireframe / B) Mid-fi / C) High-fidelity | Determines effort and polish level |

### Group 3: Variation and Interaction

| Question | Options | Why |
|----------|---------|-----|
| Do you want one polished direction or multiple options? | A) One / B) 2-3 options / C) A direction map first | Routes to `design-direction-advisor.md` or tweaks/canvas flow |
| What should vary? | A) Visual style / B) Layout / C) Density / D) Motion / E) Color only | Prevents meaningless variations |
| Do you want tweak controls after delivery? | A) No / B) A few key toggles / C) Full variant panel | Determines whether `tweaks-system.md` is needed |

### Group 4: Technical Constraints

| Question | Options | Why |
|----------|---------|-----|
| Needs to be responsive? | A) Fixed size / B) Responsive / C) Mobile only | Affects structure and scaling |
| Export needed? | A) Preview only / B) PPTX / C) PDF / D) Self-contained HTML | Routes to export constraints early |
| Accessibility requirement? | A) Standard / B) WCAG AA / C) Higher than AA | Affects contrast, sizing, and touch targets |

## Convergence Rule

After asking these groups, you should have enough to route and build. If scope is still unclear after one round, ask one targeted follow-up, then proceed with the best safe assumption. Do not keep the user in endless clarification.

## Assumption Defaults

When the user skips a question, apply these defaults:

| Unanswered | Default |
|------------|---------|
| Context | Search the workspace first, then assume no system only if nothing is found |
| Format | Landing page or screen-level artifact that best matches the request |
| Fidelity | Medium |
| Variation | One strong direction unless user asks for options |
| Brand | Start from current project context; otherwise use `frontend-design.md` |
| Responsive | Match the most likely real usage for the output |
| Export | Just preview |
| Accessibility | Standard |

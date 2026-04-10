---
name: content-strategy-diagnosis
description: Content-strategy diagnosis for Chinese creator work. Use when Codex needs to judge whether a topic, draft, or content plan should become a short video, post, article, or live session; identify whether the real problem is the angle, materials, format, platform fit, or goal linkage; and return a concrete next action instead of jumping straight into writing.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/content-strategy-diagnosis"}}
---

# Content Strategy Diagnosis

## Overview

Use this skill before writing.

The goal is not to produce the content immediately, but to judge whether the content idea itself is standing on solid ground:

- is the topic clear enough
- does it have enough material density
- what format can carry it best
- which platform or scenario fits it
- if the user wants growth, trust, consultation, or sales, does the content connect to that goal

This is a diagnosis skill, not a ghostwriting skill.

## Quick Start

1. First identify the input state: idea, plan, draft, or half-finished content.
2. Clarify the user's goal before discussing tactics.
3. Diagnose the main bottleneck before offering multiple suggestions.
4. Recommend the best-fit format and platform, not every possible format.
5. End with one concrete first move.

If the user only wants judgment, stop after the diagnosis and do not drift into full writing.

## Default Contract

Assume the following unless the user says otherwise:

- write in Chinese
- diagnose before writing
- prioritize the biggest problem, not every possible flaw
- if the content has a commercial goal, check the offer or business linkage
- if the content is not commercial, do not force a product-first conclusion
- prefer one sharp next step over a long list of soft suggestions

## Workflow

### Phase 1: Scope the Task

Determine:

- what the user already has: topic, outline, draft, or content plan
- what the content is trying to do: growth, trust, education, conversion, testing, or thinking in public
- whether the user already chose a format or platform
- whether the current problem feels like a strategy problem or a writing problem

If the input is too thin to diagnose, say what is missing instead of pretending certainty.

For messy or mixed cases, read [references/workflow.md](references/workflow.md).

### Phase 2: Match the Right Carrier

Decide what form can best carry the idea:

- short video for high-compression claims, conflict, strong hooks, and face-led persuasion
- image post or carousel for saved information, steps, lists, and visual comparison
- article or long-form post for layered logic, background, and deeper argument chains
- live or dialogue format for interactive tension, objection handling, or case-based discussion

Do not recommend a format only because it is trendy. Recommend the format that fits the material and goal.

### Phase 3: Run the Five-Lens Diagnosis

Judge the content through these five lenses:

1. **Topic and promise**
   - Is the central point clear?
   - Can the audience quickly tell what this piece is about and why it matters?
2. **Material density**
   - Does the content have enough data, scenes, examples, contrast, or sharp experience to carry the claim?
3. **Format and platform fit**
   - Is the chosen carrier helping or hurting the idea?
4. **Expression efficiency**
   - Is the piece saying one thing clearly, or packaging one small idea in too much explanation?
5. **Goal linkage**
   - If the user wants business results, can the content naturally connect to a service, product, consultation, or next action?

Read [references/diagnostic-lens.md](references/diagnostic-lens.md) when the diagnosis is not obvious.

### Phase 4: Separate the Real Problem from the Visible Symptom

Common mismatches:

- the user thinks the issue is the title, but the real issue is weak material
- the user thinks the issue is the platform, but the real issue is choosing the wrong content form
- the user thinks the issue is "AI flavor", but the real issue is low specificity
- the user thinks the issue is writing quality, but the real issue is an unclear promise

Name the primary problem directly.

### Phase 5: Recommend the Next Skill or Next Move

After diagnosing, choose the smallest next step that moves the work forward:

- if the angle and format are right but the full piece is not written, hand off to `$deep-writer`
- if the piece needs a stronger short-form opening, hand off to `$hook-optimizer`
- if the structure is fine but the voice is too flat or too templated, hand off to `$celf-style-writer`
- if the user needs to study comparable creators or businesses first, hand off to `$benchmark-filter`

Do not hand off by default. Only recommend the next skill if it clearly solves the diagnosed bottleneck.

## Output Format

Default to [assets/diagnosis-template.md](assets/diagnosis-template.md).

At minimum, include:

- one-line diagnosis
- recommended format and platform
- five-lens table or bullet-equivalent
- the main bottleneck
- one concrete first action
- the best next skill if applicable

## Hard Rules

Do not:

- write the full content when the user asked for diagnosis
- pretend all formats are equally fine
- use "can go viral" as the main judgment standard
- force a sales logic onto every piece of content
- blame the platform before checking the content itself
- give a long generic list of tips instead of naming the main issue

Always:

- clarify the content goal
- recommend a primary format
- distinguish strategy problems from writing problems
- state material gaps when they matter
- end with one clear next move

## Resource Map

- [references/workflow.md](references/workflow.md)
  - Read for the full diagnosis sequence, mixed-input handling, and symptom-versus-cause rules.
- [references/diagnostic-lens.md](references/diagnostic-lens.md)
  - Read for the five lenses, scoring heuristics, and common failure patterns.
- [assets/diagnosis-template.md](assets/diagnosis-template.md)
  - Use for the standard report shape.

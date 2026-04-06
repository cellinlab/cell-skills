---
name: deep-writer
description: Adaptive deep-writing workflow for turning interview transcripts, speeches, podcast transcripts, articles, rough drafts, and note piles into structured Chinese long-form writing. Use when Codex needs to extract viewpoints, build a brief, merge repeated ideas, clarify logic, preserve the source's core framework, design an outline before drafting, or deliver writing in staged checkpoints instead of a one-shot article.
---

# Deep Writer

## Overview

Turn raw or fragmented source material into publishable Chinese writing. Default to preserving the author's core frame, merging duplicate viewpoints, clarifying logic, and pausing for user confirmation after analysis and structure unless the user explicitly asks for one-pass output.

## Quick Start

1. Infer the audience, scenario, purpose, and stance before drafting.
2. Complete Stage 1 before writing the article body.
3. Lock Stage 2 before expanding long-form prose.
4. Run the final draft against the brief and the quality checklist.

If the user only wants a brief, outline, or structural diagnosis, stop at the relevant stage instead of forcing a full article.

## Default Contract

Treat these as the default assumptions unless the user says otherwise:

- Required: source material such as a transcript, notes, draft, article, or speech text
- Optional: target audience, publication scenario, stance, length, depth, and style
- Default language: Chinese
- Default goal: formal publishable writing, not chat-style rewriting
- Default structure policy: preserve the source's macro frame and allow only micro-adjustments
- Default process: wait for confirmation after Stage 1 and Stage 2

If the user provides an already-approved outline, treat it as Stage 2 input and move to Stage 3 after a lightweight brief alignment.

## Workflow

### Stage 1: Analysis and Planning

Perform all of the following before drafting:

- identify the likely audience, scenario, purpose, and stance
- build a brief using `assets/brief-template.md`
- preprocess spoken-language noise, repetitions, and fragmentary clauses
- extract viewpoint units and cluster overlapping ideas
- explain the main logic relations across the material

Output at least:

- the brief
- preprocessing notes
- viewpoint clusters
- logic chain or logic graph summary
- updated todo status
- a confirmation prompt for the next stage

Read [references/workflow.md](references/workflow.md) when the material is especially fragmented, repetitive, or structurally unclear.

### Stage 2: Structure Design

Use the accepted Stage 1 output to design the writing frame.

Do all of the following:

- preserve the source's core framework unless the user explicitly requests a rewrite
- merge duplicate sections or overlapping arguments
- decide section order with only necessary local reordering
- assign each section a clear job, not just a title
- explain which parts were kept and which parts were adjusted

Output at least:

- the optimized structure
- the role of each section
- notes on preserved versus adjusted structure
- updated todo status
- a confirmation prompt for the next stage

### Stage 3: Content Writing

Write the full article only after the structure is locked.

Do all of the following:

- follow the accepted structure instead of improvising a new one
- deepen claims with relevant background, mechanisms, examples, or implications
- remove transcript residue and spoken fillers
- keep the author's core meaning intact
- finish with a quality-check summary

Read [references/quality-bar.md](references/quality-bar.md) before finalizing the draft.

## Output Format

Use the staged wrapper in `assets/stage-output-template.md` unless the user requested another format.

Default wrapper:

```text
【阶段X完成】

---
【本阶段输出】
[stage output]

---
【待办事项状态】
- [completed] 第一阶段：分析与规划
- [pending] 第二阶段：结构设计
- [pending] 第三阶段：内容撰写

---
是否继续下一阶段？（输入“继续”进入下一阶段，或提出修改意见）
```

For the final stage, replace the confirmation prompt with a short quality-check summary.

## Hard Rules

Do not:

- invent a new central thesis that is absent from the source material
- radically rebuild the structure after Stage 2 is accepted
- keep obvious duplicate viewpoints in separate sections
- add generic filler that does not deepen the reader's understanding
- distort the source's stance in order to sound smoother or more authoritative

Always:

- make the logic chain visible
- distinguish source viewpoints from supplemental interpretation when that boundary matters
- keep the brief as the baseline for structure and drafting decisions
- state assumptions when the user did not provide audience, scenario, or stance

## Resource Map

- [references/workflow.md](references/workflow.md)
  - Read for the full stage checklist, clustering heuristics, logic-relation rules, one-shot mode, and failure recovery.
- [references/quality-bar.md](references/quality-bar.md)
  - Read for the final review checklist, spoken-language cleanup rules, and over-expansion guardrails.
- `assets/brief-template.md`
  - Use when drafting the stage-one brief.
- `assets/stage-output-template.md`
  - Use when formatting staged outputs and todo-state updates.

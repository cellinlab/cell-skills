---
name: deep-writer
description: Adaptive deep-writing workflow for all forms of deep content creation in Chinese, including turning transcripts and note piles into articles, deepening rough drafts, or writing structured long-form content from a topic, thesis, question, or outline. Use when Codex needs to clarify audience and purpose, build a brief, extract or construct a sound argument structure, merge repeated ideas, design an outline before drafting, deepen analysis, preserve source logic when needed, or deliver writing through staged checkpoints instead of a one-shot article.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/deep-writer"}}
---

# Deep Writer

## Overview

Handle deep content writing in three common modes:

- source-driven: turn transcripts, notes, interviews, or messy drafts into strong articles
- draft-deepening: take an existing article or outline and make it deeper, clearer, and more complete
- topic-driven: write a deep piece from a topic, thesis, question, angle, or user idea

Default to pausing for user confirmation after analysis and structure unless the user explicitly asks for one-pass output.

## Quick Start

1. Choose the writing mode before doing anything else.
2. Infer the audience, scenario, purpose, and stance before drafting.
3. Complete Stage 1 before writing the article body.
4. Lock Stage 2 before expanding long-form prose.
5. Run the final draft against the brief and the quality checklist.

If the user only wants a brief, outline, or structural diagnosis, stop at the relevant stage instead of forcing a full article.

## Default Contract

Treat these as the default assumptions unless the user says otherwise:

- Required: either source material, or a topic / thesis / question / outline to write from
- Optional: supporting materials, target audience, publication scenario, stance, length, depth, tone, and style
- Default mode selection:
  - source-driven for transcripts, notes, interviews, speeches, and fragmented material
  - draft-deepening for rough drafts, partial articles, and existing outlines
  - topic-driven for requests that start from a theme, thesis, question, or desired article idea
- Default language: Chinese
- Default goal: formal publishable writing, not chat-style rewriting
- Default structure policy:
  - source-driven: preserve the source's macro frame and allow only micro-adjustments
  - draft-deepening: keep the strongest existing frame, then strengthen weak or thin sections
  - topic-driven: design the best-fit structure around the brief and thesis
- Default process: wait for confirmation after Stage 1 and Stage 2

If the user provides an already-approved outline, treat it as Stage 2 input and move to Stage 3 after a lightweight brief alignment.

## Workflow

### Stage 1: Analysis and Planning

Perform all of the following before drafting:

- identify the writing mode
- identify the likely audience, scenario, purpose, and stance
- build a brief using `assets/brief-template.md`
- do the relevant analysis for the mode:
  - source-driven: preprocess spoken-language noise, repetitions, and fragmentary clauses
  - draft-deepening: identify weak logic, thin sections, repeated claims, and missing support
  - topic-driven: clarify the central question, working thesis, key angles, and likely counterpoints
- extract viewpoint units, argument units, or section units and cluster overlapping ideas
- explain the main logic relations or argument chain

Output at least:

- the brief
- mode diagnosis
- preprocessing notes or argument notes
- viewpoint clusters or argument clusters
- logic chain or logic graph summary
- open questions, evidence gaps, or assumptions when they materially affect the piece
- updated todo status
- a confirmation prompt for the next stage

Read [references/workflow.md](references/workflow.md) when the material is fragmented, the thesis is still fuzzy, or the structure is not yet obvious.

### Stage 2: Structure Design

Use the accepted Stage 1 output to design the writing frame.

Do all of the following:

- choose the right structure rule for the mode:
  - source-driven: preserve the source's core framework unless the user explicitly requests a rewrite
  - draft-deepening: keep the strongest existing structure, but rebuild weak branches when the draft cannot support the thesis
  - topic-driven: build the strongest structure around the thesis, reader, and scenario
- merge duplicate sections or overlapping arguments
- decide section order with the minimum necessary reordering in source-driven mode, or the clearest reader path in topic-driven mode
- assign each section a clear job, not just a title
- explain which parts were kept and which parts were adjusted

Use `assets/outline-template.md` when the user wants a reusable structure blueprint.

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
- remove transcript residue and spoken fillers when they exist
- keep the author's core meaning intact in source-driven mode
- keep the improved version aligned with the original draft's intended thesis in draft-deepening mode
- keep the thesis coherent and non-repetitive in topic-driven mode
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

- invent unsupported facts, data, case details, or quotations
- invent a new central thesis that is absent from the source material in source-driven mode
- radically rebuild the structure after Stage 2 is accepted
- keep obvious duplicate viewpoints in separate sections
- add generic filler that does not deepen the reader's understanding
- distort the source's stance in order to sound smoother or more authoritative
- pretend a topic-driven article is well evidenced if the user did not supply evidence and none is available

Always:

- choose the mode explicitly when the request is ambiguous
- make the logic chain visible
- distinguish source viewpoints from supplemental interpretation when that boundary matters
- keep the brief as the baseline for structure and drafting decisions
- state assumptions when the user did not provide audience, scenario, or stance

## Resource Map

- [references/workflow.md](references/workflow.md)
  - Read for mode selection, the full stage checklist, clustering heuristics, topic-driven argument design, one-shot mode, and failure recovery.
- [references/quality-bar.md](references/quality-bar.md)
  - Read for the final review checklist, spoken-language cleanup rules, topic-writing quality rules, and over-expansion guardrails.
- [assets/brief-template.md](assets/brief-template.md)
  - Use when drafting the stage-one brief.
- [assets/outline-template.md](assets/outline-template.md)
  - Use when presenting or locking a reusable structure blueprint.
- [assets/stage-output-template.md](assets/stage-output-template.md)
  - Use when formatting staged outputs and todo-state updates.

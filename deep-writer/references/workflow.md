# Workflow Playbook

## Table of Contents

- 1. Choose the entry point
- 2. Stage 1 checklist
- 3. Viewpoint clustering rules
- 4. Logic mapping rules
- 5. Stage 2 checklist
- 6. Stage 3 checklist
- 7. One-shot mode
- 8. Common failure patterns

## 1. Choose the Entry Point

Start from Stage 1 by default.

Move directly to Stage 2 only when the user already provides a stable outline or asks specifically for structure refinement.

Move directly to Stage 3 only when:

- the user explicitly says the structure is locked, or
- the user supplies a final outline and asks only for drafting

Even when jumping ahead, rebuild a lightweight internal brief first. Do not draft against a structure you do not understand.

## 2. Stage 1 Checklist

### 2.1 Identify the Requirement

Infer the following from the material and the request:

- target audience
- reading scenario
- writing purpose
- likely stance
- desired depth
- likely tone

State assumptions when inference is necessary.

### 2.2 Build the Brief

Use `assets/brief-template.md`.

Fill at least:

- creator persona or author position
- audience profile
- writing scenario
- content stance
- writing principles
- core themes
- key viewpoints
- structure requirements

Treat the brief as the baseline for every later decision.

### 2.3 Preprocess the Material

Detect and mark:

- spoken fillers such as "um", "ah", "you know", "就是说", "那个"
- repeated openings or self-corrections
- incomplete clauses that still contain meaning
- digressions that may later become examples instead of main arguments

Do not delete before understanding the role of the passage. Repetition can signal importance.

### 2.4 Extract Viewpoint Units

Break the material into viewpoint units instead of paragraph-shaped chunks.

Useful unit types:

- claim
- reason
- mechanism
- example
- contrast
- implication

This makes clustering more reliable than operating on raw paragraphs.

## 3. Viewpoint Clustering Rules

Merge units when they point to the same thesis even if the wording, example, or confidence level differs.

Keep units separate when they differ in:

- core stance
- causal direction
- abstraction level
- time frame
- speaker perspective

Use the cluster output to preserve nuance while removing duplication.

Recommended cluster format:

```text
聚类 1：观点标题
- 原观点：...
- 原观点：...
- 原观点：...
- 合并后观点：...
- 保留的关键细节：...
```

Do not reduce three complementary fragments into a flatter sentence. Merge by integration, not deletion.

## 4. Logic Mapping Rules

Map the strongest visible relations in the source material.

Use these relation types as defaults:

- causal: because, therefore, leads to, results in
- parallel: first, second, in another dimension, likewise
- progressive: not only, further, deeper, beyond
- contrast: however, unlike, yet, on the contrary
- summary: therefore, in short, overall, in conclusion

When the material is weakly structured, force a minimum chain:

1. premise
2. mechanism
3. consequence
4. implication

If the source does not support a clean chain, say so instead of inventing one.

## 5. Stage 2 Checklist

Treat Stage 2 as a structure-locking step.

Do all of the following:

- start from the accepted brief and viewpoint clusters
- keep the macro frame when possible
- merge duplicate branches
- reorder only adjacent or clearly misplaced blocks
- assign each section a main claim
- assign each section supporting points or evidence
- write transitions where logic would otherwise jump

Mark changes explicitly:

- `沿用原结构`
- `合并重复观点`
- `顺序微调`
- `新增过渡`

Do not generate the full article here. Keep the output structural.

## 6. Stage 3 Checklist

Write against the approved structure only.

Deepen a section with one or more of these moves:

- add background that helps the reader enter the topic
- explain the mechanism behind a claim
- supply a concrete example
- add contrast or boundary conditions
- surface implications for the reader

Avoid generic expansion such as:

- empty motivational lines
- repeated summary sentences
- vague "with the development of society" filler
- unrelated facts added only to increase length

Prefer precise, readable Chinese over literal transcript residue.

## 7. One-Shot Mode

If the user explicitly asks for one-pass output:

- run the three stages internally
- present a compressed Stage 1 and Stage 2 summary before or alongside the final draft when useful
- state key assumptions
- keep the final structure consistent with the internally locked outline

Do not skip the reasoning steps just because the visible response is compressed.

## 8. Common Failure Patterns

### 8.1 Over-expansion

Symptom:

- the draft is longer but not deeper

Fix:

- cut any paragraph that adds no mechanism, example, or implication

### 8.2 Source Drift

Symptom:

- the final article sounds polished but no longer reflects the original viewpoint

Fix:

- compare each section against the brief and the merged viewpoints

### 8.3 Duplicate Claims in Different Sections

Symptom:

- the same idea appears as separate headings or paragraphs

Fix:

- re-cluster the sections and assign one home for each major claim

### 8.4 Logic Jumps

Symptom:

- sections feel individually fine but do not connect

Fix:

- add explicit transition sentences or reorder the local block

### 8.5 Transcript Residue

Symptom:

- the draft still contains spoken-language pacing, half-sentences, or filler transitions

Fix:

- rewrite for written rhythm while preserving the meaning

---
name: ai-writing-diagnosis
description: AI-writing fingerprint diagnosis for Chinese text. Use when Codex needs to inspect a draft for overly smooth, formulaic, generic, or authorless writing patterns; quote the exact passages that feel machine-made; distinguish real problems from false alarms; and suggest what to fix first without immediately rewriting the whole piece.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/ai-writing-diagnosis"}}
---

# AI Writing Diagnosis

## Overview

Use this skill when the user suspects a draft feels too AI-generated, too smooth, too tidy, or too generic.

The default task is diagnosis, not rewrite.

The goal is to show:

- where the text starts feeling machine-made
- which pattern is causing that feeling
- whether the problem actually harms the piece
- what the user should fix first if they want stronger human presence

## Quick Start

1. Read the full text once for overall feel.
2. Ask what genre it is if that changes the judgment materially.
3. Mark the strongest suspicious passages in reading order.
4. Explain each issue concretely with the quoted text.
5. End with the dominant pattern and the highest-leverage fix.

If the piece is mostly fine, say so. Do not force problems into the report.

## Default Contract

Assume the following unless the user says otherwise:

- write in Chinese
- diagnose first, rewrite later
- judge the text in reading order
- quote the exact text when calling out a problem
- do not treat every clean sentence as "AI flavor"
- care about whether the pattern hurts expression, not whether it merely looks polished

## Workflow

### Step 1: Establish the Reading Context

Determine:

- the genre: article, short post, script, memo, email, thread, or caption
- whether the user wants diagnosis only
- whether the user is worried about "AI flavor" in general or a specific part

Genre matters. A short script may tolerate more compact slogans than a long essay.

### Step 2: Read for Global Texture

Before annotating details, notice the overall signal:

- too smooth
- too symmetric
- too abstract
- too certain
- too generic
- or actually fine

### Step 3: Annotate the Text in Order

For each suspicious passage:

- quote the line or short segment
- explain what feels off
- tag the pattern type
- note severity based on how much it harms the piece

Read [references/pattern-catalog.md](references/pattern-catalog.md) when classification is not obvious.

### Step 4: Distinguish Real Problems from False Alarms

Examples:

- a crisp structure in a professional memo is not automatically AI
- a short social post may intentionally use slogan-like compression
- one binary contrast sentence is not a problem by itself

Do not confuse "I notice a pattern" with "this must be fixed."

### Step 5: Suggest the Highest-Leverage Fix

End with:

- the dominant pattern or two
- the first places worth revising
- whether the user should self-edit or hand it to `$celf-style-writer`

If the user explicitly wants rewriting help, read [references/rewrite-guidance.md](references/rewrite-guidance.md) before proposing next questions or edits.

## Output Format

Default to [assets/report-template.md](assets/report-template.md).

At minimum, include:

- total number of notable hits
- quoted passages in order
- concrete explanation for each hit
- dominant pattern summary
- priority fix suggestion

## Hard Rules

Do not:

- rewrite the whole piece unless the user asks
- call everything AI just because it is neat
- diagnose without quoting the offending passage
- confuse stylistic preference with a real flaw
- offer fake certainty when the signal is weak

Always:

- read in sequence
- quote specific text
- explain what the pattern is doing to the reading experience
- note when a hit may be a false alarm
- end with the most useful revision priority

## Resource Map

- [references/pattern-catalog.md](references/pattern-catalog.md)
  - Read for the common AI-writing fingerprints, examples, and false-alarm notes.
- [references/rewrite-guidance.md](references/rewrite-guidance.md)
  - Read for what to ask before revising and how to move from diagnosis to rewrite.
- [assets/report-template.md](assets/report-template.md)
  - Use for the standard diagnosis report.

---
name: hook-optimizer
description: Hook and opening optimization for Chinese short-form content. Use when Codex needs to diagnose why the first 3-5 seconds or first 2-3 sentences are weak, determine whether the real problem is the opening or the material underneath it, and generate multiple opening directions that match the actual content instead of empty clickbait.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/hook-optimizer"}}
---

# Hook Optimizer

## Overview

Use this skill when the user already has a topic, body, or draft, but the opening is not doing enough work.

The opening should help the audience answer three questions quickly:

- what is this about
- why should I continue
- why should I trust or care about this voice

This skill diagnoses first and generates later.

## Quick Start

1. Check whether the content underneath the opening is strong enough.
2. Extract the best available materials before rewriting the opening.
3. Diagnose the current opening if one exists.
4. Generate several opening directions, not one magic line.
5. Pick the strongest direction based on fit, not on loudness.

If the content itself is too thin, say so before generating hooks.

## Default Contract

Assume the following unless the user says otherwise:

- write in Chinese
- optimize the opening, not the whole piece
- diagnose before generating
- prefer openings that the body can actually cash
- for spoken scripts, keep mouth-feel and breath rhythm in mind

## Workflow

### Phase 1: Read the Input State

Determine whether the user provided:

- an existing opening and a full body
- only the body
- a topic plus a few key materials

If the user only gave a title-like topic with no body or material, say the input is too thin for serious opening work.

### Phase 2: Check Whether the Content Can Carry a Hook

Look for usable fuel:

- a result or concrete outcome
- a contradiction or reversal
- a strong scene or vivid moment
- a number, comparison, or unusual detail
- a direct judgment worth arguing with

When the content has none of the above, say the hook will be limited because the body is under-fueled.

Read [references/hook-principles.md](references/hook-principles.md) when deciding whether the problem is the opening or the content itself.

### Phase 3: Diagnose the Current Opening

If the user already has one, check:

- **independence**: can it work even if the title is unseen
- **grip**: does it give the audience a reason to stay
- **curiosity or tension**: does it hold something back
- **credibility**: why believe or care about this speaker
- **flow**: is it easy to say or read
- **payoff fit**: can the body deliver what the opening promises

### Phase 4: Choose the Right Hook Type

Select from the smallest set that truly fits:

- result-led
- contradiction-led
- scene-led
- question-led
- judgment-led
- suspense-led

Read [references/hook-types.md](references/hook-types.md) when comparing directions.

### Phase 5: Generate a Hook Pack

Produce 3-4 strategic directions.

For each direction:

- explain why it fits this content
- generate 2-4 opening options
- keep them distinct rather than slightly reworded copies

If one direction clearly dominates, say so and explain why.

## Output Format

Default to [assets/hook-pack-template.md](assets/hook-pack-template.md).

At minimum, include:

- content viability note
- current opening diagnosis
- extracted materials
- multiple hook directions
- top recommendations

## Hard Rules

Do not:

- pretend a weak body can be rescued by a flashy opening
- depend on the title to complete the meaning
- reveal the full answer too early when tension is needed
- generate hooks the body cannot pay off
- return one "best line" without showing alternatives

Always:

- diagnose before generating
- extract the best available materials first
- keep the opening aligned with the actual content
- mention when the problem is upstream from the opening
- preserve readability and speakability

## Resource Map

- [references/hook-principles.md](references/hook-principles.md)
  - Read for the base rules of what a strong opening must do and how to detect weak-content cases.
- [references/hook-types.md](references/hook-types.md)
  - Read for the main hook families, fit conditions, and failure modes.
- [assets/hook-pack-template.md](assets/hook-pack-template.md)
  - Use for the standard output shape.

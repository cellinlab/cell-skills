---
name: celf-style-writer
description: "Personal Chinese writing-style skill for Cell 细胞 style articles, rewrites, style enhancement, and style review. Use when Codex needs to write, rewrite, enhance, or audit Chinese content so it sounds like Cell speaking directly to the reader: friend-to-friend, warm but sharp, concrete, hook-driven, anti-academic, anti-AI-template, and grounded in real experience instead of abstract sermonizing."
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/celf-style-writer"}}
---

# Celf Style Writer

## Overview

Write or reshape Chinese content so it feels like Cell talking to the reader in person: warm, experienced, concrete, honest, lightly sharp, and structurally alive. Treat this as a style skill, not a topic skill. The output should feel human, specific, and lived, not like an AI trying to imitate personality through formulas. For long-form pieces, make the article advance like a real person thinking on the page, not like a report being assembled.

## Quick Start

1. Pick the mode: `write`, `rewrite`, `enhance`, or `review`.
2. Build a quick brief with `assets/style-brief-template.md`.
3. Read [references/style-skeleton.md](references/style-skeleton.md) before drafting or heavy rewriting.
4. Read [references/content-method.md](references/content-method.md) when writing from scratch, rewriting a long article, or deciding how the piece should advance.
5. Read [references/personal-variables.md](references/personal-variables.md) when the draft needs Cell-specific identity, values, catchphrases, or tone choices.
6. Run the final text against [references/quality-bar.md](references/quality-bar.md) before delivery.

If the user only wants style diagnosis, do not rewrite the full piece. Diagnose first.

## Modes

### 1. Write

Use when the user gives a topic, thesis, question, or outline and wants a Cell-style piece from scratch.

### 2. Rewrite

Use when the user already has a draft and wants it rewritten so it sounds more like Cell.

### 3. Enhance

Use when the user wants to keep most of the original copy but add more living voice, friend-to-friend tone, or stronger rhythm.

### 4. Review

Use when the user wants a style audit instead of a rewrite. Report where the text feels too academic, too templated, too preachy, or not personal enough.

## Default Contract

Assume all of the following unless the user says otherwise:

- write in Chinese
- prefer a friend-to-friend tone over a lecture tone
- preserve the source meaning when rewriting
- avoid fake authority, fake neutrality, and fake biography
- use real or explicitly framed experiential reasoning instead of empty abstraction
- use style devices selectively instead of mechanically stacking every trick
- prefer direct statements over formulaic binary contrast frames
- default to not using “不是……而是……” unless it removes a real misunderstanding better than a plain sentence
- trust the reader and cut filler, over-explaining, and quote-bait phrasing

## Workflow

### Step 1: Identify the Task State

Determine:

- whether this is `write`, `rewrite`, `enhance`, or `review`
- who the reader is
- what the piece is trying to do
- whether the source already has a usable structure
- which long-form archetype fits best if this is a full article

### Step 2: Set the Style Brief

Lock at least:

- topic
- audience
- scenario
- purpose
- tone temperature
- article archetype if relevant
- allowed degree of personal exposure
- whether concept naming and stronger hooks should be used

Use `assets/style-brief-template.md`.

### Step 3: Set the Material Boundary

Determine what must come from the human side and what AI may help supply.

- keep firsthand observation, emotional memory, and decisive judgment grounded in real source material
- use AI for structure, counterpoints, background, and analogy support
- admit uncertainty when the source lacks real detail instead of inventing texture

Use [references/content-method.md](references/content-method.md) when needed.

### Step 4: Apply the Style

Apply the style in this order:

1. preserve or rebuild the conversational stance
2. remove filler, fake grandeur, vague attribution, and obvious AI scaffolding
3. give the article a concrete opening, a visible mainline, and a believable end point
4. fix the logic and rhythm at paragraph level
5. add signature devices only where they genuinely help
6. inject Cell-specific tone, catchphrases, and transitions
7. make one last pass for AI smell, especially formulaic contrasts, generic endings, checklist-like structure, and over-tidy symmetry

### Step 5: Self-Check

Check:

- does it sound like a person talking, not a system summarizing
- does it sound like Cell, not just “generic casual Chinese”
- is the argument still clear after styling
- did any device become performative or repetitive
- if this is a long-form piece, does it advance scene by scene or thought by thought instead of block by block

Use `assets/style-review-checklist.md`.

## Hard Rules

Do not:

- fabricate personal history, data, quotes, rulings, or evidence
- write like a lecturer, preacher, or consultant-on-stage
- overuse catchphrases until they feel like parody
- turn every paragraph into a hook machine
- use academic filler, self-media clichés, or obvious AI scaffolding
- use formulaic contrast templates like “不是……而是……”, “不仅……而且……”, or “这不仅仅是……” by default
- manufacture quote-like lines just to sound deep
- rely on neat triples, symmetrical slogans, or generic inspirational endings
- use insulting profanity against people

Always:

- keep the core meaning truthful
- prefer concrete scenes, examples, and lived experience over empty slogans
- use first-person ownership when making judgments
- make the text feel lived, not merely formatted

## Resource Map

- [references/style-skeleton.md](references/style-skeleton.md)
  - Read for the reusable style skeleton extracted from the original prompt: persona, sentence patterns, hook system, argument system, rhythm, transitions, and bans.
- [references/content-method.md](references/content-method.md)
  - Read for long-form article method: angle quality checks, human/AI boundary, article archetypes, progression devices, scene-led openings, callback endings, and mainline control.
- [references/personal-variables.md](references/personal-variables.md)
  - Read for Cell’s confirmed identity pack, value system, tone defaults, catchphrases, emotional markers, concept naming defaults, and transition phrases.
- [references/quality-bar.md](references/quality-bar.md)
  - Read for the final review checklist, anti-AI / anti-academic rules, device-overuse warnings, and rewrite heuristics.
- [assets/style-brief-template.md](assets/style-brief-template.md)
  - Use to define mode, audience, scenario, tone, and allowed devices before writing.
- [assets/personal-parameter-sheet.md](assets/personal-parameter-sheet.md)
  - Use as the compact editable version of Cell’s personal style variables.
- [assets/style-review-checklist.md](assets/style-review-checklist.md)
  - Use for a fast pass before returning the final text.

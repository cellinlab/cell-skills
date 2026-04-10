---
name: xhs-title-selector
description: Xiaohongshu title strategy skill for Chinese creators. Use when Codex needs to pick the right title formula for a topic, draft, or existing Xiaohongshu title; match the content to the right trigger family instead of free-generating titles; produce traceable title options with formula IDs and rationale; and choose the best testing candidates.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/xhs-title-selector"}}
---

# XHS Title Selector

## Overview

Use this skill to treat Xiaohongshu titles as a matching problem, not a random generation problem.

The core job is to:

- identify what the content is really selling in the first glance
- match it to the right trigger family
- generate titles that can be traced back to a formula
- explain why each title fits

This is a title-strategy skill, not a generic copywriting skill.

## Quick Start

1. First understand the topic, audience, and content goal.
2. Check whether the topic itself is strong enough to deserve title work.
3. Match the content to 3-6 trigger families.
4. Select 5-8 formulas from the catalog instead of free-generating blindly.
5. Return title options with formula IDs, rationale, and Top 3 recommendations.

If the topic itself is weak or unclear, say so before generating titles.

## Default Contract

Assume the following unless the user says otherwise:

- write in Chinese
- generate Xiaohongshu-oriented titles
- use the formula catalog instead of pure freeform generation
- cover at least 3 distinct trigger families unless the topic is unusually narrow
- keep titles concise and testable
- prefer titles that can actually be paid off by the body

## Workflow

### Step 1: Understand the Input

The user may provide:

- a topic
- an industry plus topic
- a paragraph or full draft
- a current title that needs diagnosis

Lock these first:

- what the content is about
- who it is for
- what reaction the user wants: click, save, trust, comment, or conversion

If the topic is still too fuzzy, read [references/workflow.md](references/workflow.md).

### Step 2: Decide Whether Title Work Should Start Yet

Before matching formulas, ask:

- does the content have a clear promise
- is there enough material to support a stronger title
- is the issue really the title, or is the topic itself weak

If the topic is weak, recommend `$content-strategy-diagnosis` instead of pretending title work can rescue it.

### Step 3: Match Trigger Families

Use the trigger-family map in [references/trigger-families.md](references/trigger-families.md).

Typical matching logic:

- counterintuitive claim -> cognitive conflict
- hidden knowledge or inside information -> curiosity gap
- warnings, pitfalls, correction -> loss avoidance
- precise audience callout -> identity mirror
- steps, methods, lists -> numeric anchor
- measurable outcome -> outcome promise
- story or personal turnaround -> case reversal
- strong stance or potential debate -> controversy
- specific user state -> scenario or condition
- push to action -> action call
- borrowed credibility -> authority leverage
- comments or self-check desire -> interaction or test

Do not force families that do not fit.

### Step 4: Select Formulas

Choose 5-8 formulas from [references/formula-catalog.md](references/formula-catalog.md).

For each formula:

- keep the formula logic intact
- adapt the wording to the user's topic
- label the formula ID
- explain why it fits this content

### Step 5: Generate and Rank Titles

Return:

- grouped title options by trigger family
- formula IDs
- one-line rationale
- Top 3 recommendations for immediate testing

Read [references/quality-bar.md](references/quality-bar.md) before finalizing.

### Step 6: Handle Existing Titles

If the user already has a title:

1. infer which family and formula it is closest to
2. diagnose whether the problem is formula choice or execution quality
3. provide:
   - same-formula improvements
   - alternative-family replacements

## Output Format

Default to [assets/title-pack-template.md](assets/title-pack-template.md).

At minimum, include:

- topic and audience read
- matched trigger families
- title options with formula IDs
- Top 3 recommendation
- brief next-step advice

## Hard Rules

Do not:

- free-generate titles without formula attribution
- spoil the whole answer inside the title when suspense is needed
- stuff every option into one trigger family
- use niche jargon if broader language would widen relevance
- promise outcomes the content cannot support

Always:

- identify topic and audience first
- make formula choice explicit
- keep multiple strategic directions alive
- distinguish between wrong formula and weak execution
- keep the final recommendation opinionated

## Resource Map

- [references/workflow.md](references/workflow.md)
  - Read for input-state handling, title-before-content checks, and existing-title optimization.
- [references/trigger-families.md](references/trigger-families.md)
  - Read for the 12 trigger families and when each should be used.
- [references/formula-catalog.md](references/formula-catalog.md)
  - Read for the traceable formula list used in title generation.
- [references/quality-bar.md](references/quality-bar.md)
  - Read for title quality rules, compression guidance, and failure checks.
- [assets/title-pack-template.md](assets/title-pack-template.md)
  - Use for the standard output shape.

---
name: benchmark-filter
description: Benchmark filtering for Chinese creator, OPC, and one-person-business work. Use when Codex needs to judge whether a person, creator, or business is actually worth studying; separate business signal from vanity signal; decide what layer is worth copying; and recommend whether to stop at a shortlist or hand the target to $opc-case-research for deeper study.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/benchmark-filter"}}
---

# Benchmark Filter

## Overview

Use this skill when the user needs help choosing who to study, who to copy from, or whether an existing benchmark is actually useful.

This skill does not do a full case study. It filters first.

The core job is to answer:

- is this benchmark worth learning from
- what exactly is worth learning
- what should not be copied
- should we stop here or move into deeper case research

## Quick Start

1. Clarify whether the user needs a shortlist or a judgment on one existing benchmark.
2. Identify the user's real learning target: content, offer, channel, conversion, positioning, or business model.
3. Run the five filters before talking about taste or preference.
4. Separate copyable mechanism from non-copyable surface traits.
5. End with one concrete first imitation or research move.

## Default Contract

Assume the following unless the user says otherwise:

- write in Chinese
- creator, OPC, one-person-business, or content-led business context
- filter first, deep-research later
- look for operating signal, not just personal charisma
- do not let "this doesn't feel like me" override mechanism analysis too early

## Workflow

### Phase 1: Clarify the Learning Target

Ask what the user is really trying to learn:

- content system
- offer design
- channel growth
- conversion path
- brand or positioning
- overall business model

If the learning target is fuzzy, the benchmark choice will be fuzzy too.

### Phase 2: Run the Five Filters

Judge each benchmark through these filters:

1. **Economic signal**
   - Is there evidence of a real business, not just attention?
2. **Model legibility**
   - Can we roughly understand how this person gets attention, trust, money, and delivery done?
3. **Copyable mechanism**
   - What part is learnable process, and what part is likely talent, timing, capital, or reputation advantage?
4. **Stage relevance**
   - Is the benchmark too far ahead or operating in a structurally different game?
5. **Ego-noise control**
   - Is the user rejecting the benchmark because it truly cannot be learned from, or because it feels unglamorous, repetitive, or not self-expressive enough?

Read [references/filter-framework.md](references/filter-framework.md) when the judgment is mixed.

### Phase 3: Name the Layer to Study

Do not say only "study this person."

Say which layer is worth studying:

- content angle
- packaging
- offer ladder
- conversion path
- audience selection
- operating rhythm

And say which layer should not be copied blindly.

### Phase 4: Check Copy Granularity

If the user already has a benchmark and says they are "learning from" it, verify the level of imitation.

Read [references/copy-granularity.md](references/copy-granularity.md) when doing a copy check.

Common failure:

- copying the vibe but not the mechanism
- copying the topic but not the offer structure
- copying the output but not the cadence or conversion path

### Phase 5: Recommend the Next Move

Choose the smallest next step:

- shortlist 1-3 worthy benchmarks
- copy one specific layer first
- or escalate one benchmark into `$opc-case-research`

## Output Format

Default to [assets/benchmark-card-template.md](assets/benchmark-card-template.md).

At minimum, include:

- one-line judgment
- five-filter result
- worth-learning layers
- do-not-copy layers
- first move
- whether deeper research is recommended

## Hard Rules

Do not:

- use follower count as the main proof of worth
- confuse charisma with business model
- say "learn from them" without naming what to learn
- let personal taste override mechanism analysis too early
- turn a quick filter into a fake full case study

Always:

- clarify the learning target
- separate signal from surface
- mark copyable versus non-copyable parts
- give one concrete next move
- recommend `$opc-case-research` only when deeper case study would materially help

## Resource Map

- [references/filter-framework.md](references/filter-framework.md)
  - Read for the five filters, signal examples, and mixed-case judgment rules.
- [references/copy-granularity.md](references/copy-granularity.md)
  - Read for how to test whether the user is copying at a useful level of detail.
- [assets/benchmark-card-template.md](assets/benchmark-card-template.md)
  - Use for the standard output structure.

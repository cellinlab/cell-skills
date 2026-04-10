---
name: mrbeast-perspective
description: MrBeast perspective skill for content packaging, video concepts, title and thumbnail strength, hook design, retention, and reinvestment logic. Use when Codex needs to reason with MrBeast's strongest content lenses rather than merely mimic his persona: CTR × AVD, no dull moments, stair-stepping, simple concept × extreme execution, and audience-first packaging. Trigger when the user explicitly asks for MrBeast's angle or clearly wants that lens on video growth, packaging, retention, or big-idea content.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/mrbeast-perspective"}}
---

# MrBeast Perspective

## Overview

这是一个 advisor-first 的 MrBeast 视角 Skill。

重点不是模仿 Jimmy 的语气，而是用他最强的内容判断模型来看问题：

- CTR × AVD
- 零无聊时刻
- 阶梯递进
- 简单概念 × 极端执行
- 再投资飞轮
- 在预算受限下用创意省钱

## Quick Start

1. 先判断问题更像：题材概念、标题封面、hook、留存，还是内容系统。
2. 先找真正拖后腿的环节，不要所有部分一起改。
3. 如果平台不是 YouTube，要先做迁移翻译，不照搬表层做法。
4. 回答里要保留“预算、平台、市场”这三个边界。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文
- 默认顾问型，不默认第一人称扮演
- 优先讲“为什么这不够可传播”，再讲怎么改
- 先找概念和节奏问题，再谈文案修饰
- 不把 YouTube 指标硬套到所有平台

## Workflow

### Step 1: Classify the Question

优先分到下面几类：

- **题材与概念**
- **标题 / 封面 / 包装**
- **hook 与前 30 秒**
- **留存与节奏**
- **内容系统与再投资**

### Step 2: Load the Right References

| 问题类型 | 按需读取 |
| --- | --- |
| 题材与概念 | [references/core-models.md](references/core-models.md) + [references/decision-heuristics.md](references/decision-heuristics.md) |
| 标题 / 封面 / 包装 | [references/decision-heuristics.md](references/decision-heuristics.md) + [references/expression-dna.md](references/expression-dna.md) |
| hook 与留存 | [references/core-models.md](references/core-models.md) + [references/decision-heuristics.md](references/decision-heuristics.md) |
| 内容系统与再投资 | [references/core-models.md](references/core-models.md) + [references/boundaries.md](references/boundaries.md) |

### Step 3: Answer in MrBeast Mode, Not Hype Mode

默认回答结构：

1. **最先出问题的是哪一环**
2. **MrBeast 会用哪条公式判断**
3. **优先级最高的修改动作**
4. **哪些地方不能直接照搬**

### Step 4: Translate Across Platforms

如果不是 YouTube：

- 保留“概念成立、包装清楚、节奏持续升级”的底层逻辑
- 不硬搬英文标题习惯和预算打法
- 明确写出哪部分是可迁移层，哪部分是 YouTube 特化层

## Hard Rules

Do not:

- 把所有问题都变成“更炸一点”
- 只讲标题，不看概念和留存
- 假装所有创作者都能复制高预算打法
- 把 MrBeast 视角当成所有平台的通用真理

Always:

- 先判断概念是否一眼成立
- 先找拖后腿的单点
- 用受众体验而不是创作者自我表达做判断
- 写出预算、平台和市场边界

## Resource Map

- [references/core-models.md](references/core-models.md)
  - 内容包装、留存与再投资的核心模型。
- [references/decision-heuristics.md](references/decision-heuristics.md)
  - 高频判断规则，适合快速诊断标题、hook 和节奏。
- [references/expression-dna.md](references/expression-dna.md)
  - MrBeast 风格中值得保留的判断方式与防机械化约束。
- [references/boundaries.md](references/boundaries.md)
  - 视角适用边界、张力与诚实提醒。

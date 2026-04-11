---
name: video-packaging-diagnosis
description: Video packaging diagnosis for Chinese short-form creators. Use when Codex needs to diagnose why a video's title, cover, opening hook, or payoff structure is weak; check click-worthiness and retention together; compare alternative title/cover strategies; and identify whether the main problem is packaging, opening, or promise fulfillment rather than the whole script.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/video-packaging-diagnosis"}}
---

# Video Packaging Diagnosis

## Overview

这个 Skill 专门处理视频的：

- 标题
- 封面
- 开头承接
- promise 与兑现

它不是通用文案 Skill，也不是完整脚本 Skill。

## Quick Start

1. 先判断问题更像：标题、封面、开头，还是兑现关系。
2. 先找一个最限制点击或留存的单点。
3. 标题、封面、开头必须围绕同一个 promise。
4. 给优化方案时，至少保留 2 条不同方向。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文
- 先诊断，再给改法
- 先看 promise 是否成立，再谈词句雕花
- 如果平台没说明，按中文短视频语境处理

## Workflow

### Step 1: Scope the Material

用户可提供：

- 标题
- 封面图描述或图片
- 开头脚本
- 视频大纲

### Step 2: Route the Diagnosis

| 场景 | 按需读取 |
| --- | --- |
| 标题诊断 | [references/contrast-headlines.md](references/contrast-headlines.md) |
| 封面诊断 | [references/cover-strategies.md](references/cover-strategies.md) |
| 开头 / 承接诊断 | [references/payoff-structure.md](references/payoff-structure.md) |
| 整体封标诊断 | 三个文件都读 |

### Step 3: Name the Real Bottleneck

常见瓶颈：

- 标题没有对比和画面感
- 封面没有视觉聚焦
- 开头没有立刻确认标题 promise
- 中段平，结尾又没有兑现

### Step 4: Return Targeted Fixes

默认交付：

- 一句话诊断
- 主要问题 1-3 条
- 2-3 个标题方向
- 封面策略建议
- 开头承接修正建议

## Hard Rules

Do not:

- 只改标题，不看封面和开头
- 把所有问题都归因成“不够炸”
- 没诊断就直接给一个答案

Always:

- 把问题落到点击或留存
- 检查标题、封面、开头是否在说同一件事
- 给至少两种可比较方案

## Resource Map

- [references/contrast-headlines.md](references/contrast-headlines.md)
  - 强对比标题的类型与检查方法。
- [references/cover-strategies.md](references/cover-strategies.md)
  - 封面策略、视觉聚焦与常见错误。
- [references/payoff-structure.md](references/payoff-structure.md)
  - 开头确认、中段升级、结尾兑现的承接检查。
- [assets/diagnosis-template.md](assets/diagnosis-template.md)
  - 标准诊断输出模板。

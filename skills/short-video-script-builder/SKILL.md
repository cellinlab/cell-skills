---
name: short-video-script-builder
description: Chinese short-video script workflow for benchmark-led script creation. Use when Codex needs to turn one to five benchmark videos plus product/topic context into a structured script pack with hook analysis, formula extraction, script and storyboard generation, pacing, CTA, and compliance checks. Trigger when the user asks for a Douyin short-video script, benchmark breakdown, ad creative script, seeding script, or wants to turn winning short videos into a reusable scripting framework.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/short-video-script-builder"}}
---

# Short Video Script Builder

## Overview

把短视频脚本创作，从“模仿一个爆款”，升级成“拆结构、提公式、再生成”。

这个 Skill 适合处理：

- 抖音 / 中文短视频种草脚本
- 投放素材脚本
- 教程 / 评测 / 对比型短视频
- 已有对标视频时的拆解和迁移

## Quick Start

1. 先判断是 `benchmark-first` 还是 `formula-first`。
2. 收集产品 / 主题 / 目标人群 / 脚本类型 / 目标时长。
3. 先拆前 3 秒，再看整条结构。
4. 先提炼可复制结构，再写脚本。
5. 结尾必须补一次合规与兑现检查。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文
- 优先交付一个完整 script pack，而不是只给一段口播
- 如果有 benchmark，优先从 benchmark 提炼
- 如果没有 benchmark，用公式库先做基线，但明确说明置信度较低
- 优先给种草 / 教程 / 投放这三类常见模式

## Workflow

### Step 1: Scope the Task

先收集：

- 视频类型：种草 / 投放 / 教程 / 评测 / 对比
- benchmark 视频：1-5 条
- 产品或主题信息
- 目标人群
- 目标时长
- 目标动作：收藏、关注、点击、进直播间、下单

### Step 2: Choose the Route

| 路由 | 什么时候用 | 按需读取 |
| --- | --- | --- |
| benchmark-first | 用户给了对标视频 | [references/benchmark-analysis.md](references/benchmark-analysis.md) + [references/script-modes.md](references/script-modes.md) |
| formula-first | 没有对标视频，先用通用结构起草 | [references/formula-library.md](references/formula-library.md) + [references/script-modes.md](references/script-modes.md) |

### Step 3: Analyze Before Writing

不管哪条路，都先回答这些问题：

- 前 3 秒的文案钩子是什么
- 前 3 秒的视觉钩子是什么
- 钩子和画面是否在强化同一个信息
- 视频采用了什么结构与节奏
- CTA 出现在哪里
- 哪些元素可迁移，哪些不能硬抄

### Step 4: Generate the Script Pack

默认交付：

- 一句话核心策略
- hook 方案
- 完整脚本
- 分镜表
- 节奏说明
- CTA 设计
- 合规提示

如需要，可同时给出：

- 种草版
- 投放版

### Step 5: Check Payoff and Compliance

脚本写完后，必须再过一遍：

- promise 是否兑现
- 卖点是否过多
- CTA 是否和目标动作一致
- 是否存在绝对化或高风险表述

## Hard Rules

Do not:

- 直接抄 benchmark 文案
- 只拆文案，不拆画面和节奏
- 没有 benchmark 时假装自己有强品类结论
- 给出不考虑审核风险的夸张承诺

Always:

- 先拆前 3 秒
- 区分“可复制结构”和“不可复制势能”
- 写清脚本类型和目标动作
- 在输出里保留合规提醒

## Resource Map

- [references/benchmark-analysis.md](references/benchmark-analysis.md)
  - 7 维 benchmark 拆解框架。
- [references/formula-library.md](references/formula-library.md)
  - 无 benchmark 时可调用的通用与品类公式。
- [references/script-modes.md](references/script-modes.md)
  - 种草、投放、教程、评测四类脚本的差异。
- [references/compliance-checklist.md](references/compliance-checklist.md)
  - 合规与兑现检查清单。
- [assets/script-pack-template.md](assets/script-pack-template.md)
  - 标准输出模板。

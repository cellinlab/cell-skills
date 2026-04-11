---
name: xhs-image-director
description: Xiaohongshu image direction workflow for Chinese creators. Use when Codex needs to turn a note, draft, or topic into high-quality Xiaohongshu image directions: propose two to three distinct design routes first, choose the right visual hierarchy for the content, prefer 3:4 vertical native layouts, decide between AI image generation and HTML fallback, and review the result for both design quality and feed attractiveness before finalizing.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/xhs-image-director"}}
---

# XHS Image Director

## Overview

这个 Skill 处理的是小红书配图的“方向、提案、生成与审查”。

核心原则只有一句：

先提案，后生成。

## Quick Start

1. 先理解内容主题、关键词、情绪和图片用途。
2. 先出 2-3 个方向，不跳过提案。
3. 先做信息层级，再做风格。
4. 生成后必须做设计与平台吸引力双重检查。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 标准比例：3:4 竖版
- 输出语言：中文
- 优先原生小红书阅读感，不做模板感重的设计
- 默认给 2-3 个差异明确的方向
- 精确数字和复杂表格优先考虑 HTML 兜底

## Workflow

### Step 1: Understand the Content

先提炼：

- 主题
- 关键词 / 数字 hero
- 情绪
- 图片类型：封面、轮播、信息图

### Step 2: Propose Before Generating

必须先给 2-3 个方向，每个方向写清：

- 视觉风格
- 色彩
- 文案布局
- 情绪

默认读取：

- [references/design-profile.md](references/design-profile.md)
- [references/design-guidelines.md](references/design-guidelines.md)

### Step 3: Choose the Path

| 路径 | 什么时候用 |
| --- | --- |
| AI 生成 | 需要质感、氛围、插画感、纸张感、手作感 |
| HTML 兜底 | 文字必须精确、数据复杂、表格信息多 |

### Step 4: Review the Result

每次都至少检查：

- 文字是否清楚可读
- 视觉层级是否成立
- 是否有明显模板感
- 在信息流里是否够抓眼

## Hard Rules

Do not:

- 跳过设计提案直接出图
- 用深蓝赛博或通用模板糊弄
- 让画面只剩风格，没有信息层级
- 把复杂数据硬塞给 AI 文字渲染

Always:

- 先提案
- 先做层级
- 先考虑 3 秒停留
- 生成后做设计和平台双重审查

## Resource Map

- [references/design-profile.md](references/design-profile.md)
  - Cell 风格的小红书视觉偏好画像。
- [references/design-guidelines.md](references/design-guidelines.md)
  - 小红书原生尺寸、排版、配色与可读性规则。
- [references/path-selection.md](references/path-selection.md)
  - AI 生成与 HTML 兜底的选择规则。
- [assets/proposal-template.md](assets/proposal-template.md)
  - 标准提案格式。

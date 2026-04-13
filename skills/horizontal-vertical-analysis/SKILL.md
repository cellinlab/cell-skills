---
name: horizontal-vertical-analysis
description: Deep-research skill for Chinese outputs using 横纵分析 / Horizontal-Vertical Analysis. Use when Codex needs to systematically study a product, company, concept, technology, market, or person: rebuild the full life-cycle on a vertical timeline, compare current peers or substitutes on a horizontal slice, cross the two axes into original insight, separate facts from inferences, and deliver a structured report or optional PDF. Not for quick definitions, gossip, or unsupported legal / investment due diligence.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/horizontal-vertical-analysis"}}
---

# Horizontal Vertical Analysis

## Overview

把“帮我研究一下这个东西”做成一份真正有判断力的双轴研究。

这个 Skill 保留 `hv-analysis` 最有价值的方法骨架：

- 纵轴：把对象从起源到当下讲成一条有因果的生命历程
- 横轴：把对象放到当前切面里，和竞品、替代方案、同类路径做比较
- 交汇：回答“它为什么会变成今天这样”，而不是只做资料堆叠
- 交付：默认 Markdown 母稿，环境允许时可导出 PDF

但默认按 Cell 风格执行：

- 先建研究问题，不做空泛大而全
- 先搭证据骨架，再下判断
- 默认区分 `事实 / 推断 / 未知`
- 报告要可读，但不装腔
- 优先交付可复用研究文档，而不是一次性回答

## Quick Start

1. 先锁定研究对象、对象类型、研究目的、输出深度。
2. 建 source map，再搭时间线，不要直接写结论。
3. 纵轴先讲“怎么一步步走到今天”，横轴再讲“今天跟谁比、差在哪”。
4. 把历史路径和当下格局交叉，产出真正的新判断。
5. 默认先交 Markdown；用户需要正式交付件时，再用脚本导出 PDF。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文
- 研究范围：公开信息 + 用户明确提供的材料
- 默认深度：`standard`
- 默认交付：结构化研究报告
- 默认证据策略：一手来源优先，关键事实至少双重验证
- 默认风格：研究性 + 可读性，不写成流水账，也不写成喊口号的长文

## Workflow

### Step 1: Scope the Object

先判断：

- 研究对象是什么
- 属于产品、公司、概念、技术、人物，还是行业现象
- 用户真正要解决的是：
  - 快速摸底
  - 系统研究
  - 竞品比较
  - 为写作 / 决策 /课程 /投资前理解做准备
- 需要 `quick`、`standard` 还是 `deep`

如果只是简单问“这是什么”，不要硬上完整横纵分析。

### Step 2: Build the Research Skeleton

先搭三样东西：

- source map
- 纵向时间线
- 横向候选对比对象

这一步不要急着得出结论。先确认信息是不是够支撑后面写作。

需要检索、验证、抽样和资料充分性判断时，读 [references/source-strategy.md](references/source-strategy.md)。

### Step 3: Run the Vertical Axis

纵轴不是年表，而是故事：

- 它为什么出现
- 是谁推动出来的
- 关键阶段怎么划分
- 哪些节点改变了后来的路径
- 哪些早期选择形成了路径依赖

纵轴的详细写法与阶段拆法，读 [references/workflow.md](references/workflow.md)。

### Step 4: Run the Horizontal Axis

先判断现在有没有可比对象：

- 没有直接竞品
- 只有 1-2 个主要对手
- 竞品充分，需选 3-5 个代表

横轴不写成参数表的文字版。重点是：

- 现在各自站在哪
- 用户为什么选它
- 研究对象填补了什么空白
- 风险来自正面竞争、替代方案，还是新兴路径

对象类型适配、竞品场景判断和对比维度，读 [references/analysis-lenses.md](references/analysis-lenses.md)。

### Step 5: Cross the Two Axes

报告最值钱的部分不是“纵向 + 横向”，而是交叉后的判断：

- 历史如何塑造了今天的位置
- 今天的优势来自哪些旧决策
- 今天的短板是不是旧优势的副作用
- 如果把主要竞品也放回时间轴，会看到什么路径分叉
- 接下来最可能、最危险、最乐观的剧本分别是什么

### Step 6: Deliver the Report

默认使用 [assets/research-report-template.md](assets/research-report-template.md)。

需要完整结构、篇幅、证据标注、写作风格时，读 [references/report-contract.md](references/report-contract.md)。

如果用户要正式交付件：

- 先完成 Markdown 母稿
- 再用 [scripts/md_to_pdf.py](scripts/md_to_pdf.py) 导出 PDF

## Output Modes

- `quick`
  - 一句话定义 + 当前位置 + 关键时间线 + 主要对比对象 + 初步判断
- `standard`
  - 完整纵轴、横轴、交汇洞察、来源清单、事实与推断边界
- `deep`
  - `standard` + 更细时间线 + 竞品维度矩阵 + 不确定项与后续验证清单 + 正式 PDF

## Hard Rules

Do not:

- 把简单名词解释伪装成深度研究
- 在信息不足时假装完整
- 用单一二手来源支撑核心判断
- 把纵轴写成流水账
- 把横轴写成堆参数
- 把推断写成事实

Always:

- 先搭骨架，再下判断
- 优先一手来源和原始材料
- 区分 `事实 / 推断 / 未知`
- 用明确日期或时间范围表达关键结论
- 在交汇段给出新的判断，而不是摘要复述

## Resource Map

- [references/workflow.md](references/workflow.md)
  - 读这个文件来执行双轴研究主流程、阶段划分和交汇分析。
- [references/source-strategy.md](references/source-strategy.md)
  - 读这个文件来设计搜索、抽样、验证、学术资料获取和资料充分性自检。
- [references/analysis-lenses.md](references/analysis-lenses.md)
  - 读这个文件来按对象类型调整纵横分析重点，并判断竞品场景。
- [references/report-contract.md](references/report-contract.md)
  - 读这个文件来确定交付结构、篇幅、风格、证据标注和质检标准。
- [references/research-schema.json](references/research-schema.json)
  - 需要结构化记录研究时，使用这个 schema。
- [assets/research-report-template.md](assets/research-report-template.md)
  - 最终研究报告模板。
- [scripts/md_to_pdf.py](scripts/md_to_pdf.py)
  - Markdown 转 PDF 的导出脚本。

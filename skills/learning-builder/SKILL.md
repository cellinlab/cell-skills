---
name: learning-builder
description: "Personalized learning-pack builder for Chinese creators. Use when Codex needs to turn a vague learning goal into a可执行学习方案：先做学习者画像与目标澄清，再做权威来源优先的资料研究，最后产出可学习、可复盘、可输出的教程包（含练习、节奏、里程碑、引用来源）。适用于学习某个新领域、搭建个人课程、做主题集训、把输入转成可写作素材；不适用于一次性问答或纯网页设计任务。"
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/learning-builder"}}
---

# Learning Builder

## Overview

把“我想学这个”变成一套可执行、可复盘、可输出的学习包。

保留 `yao-open-skills` 中 learning-builder 的核心价值：

- 先 intake（学习者画像）再研究
- 研究阶段优先权威来源
- 产出必须带引用与练习
- 可按需导出 Word/PDF（环境允许时）

并加入 Cell 风格强化：

- 学习不止“看懂”，要能“产出”
- 学习包默认对接内容创作场景
- 每个阶段都要有可验证的动作与里程碑

## Quick Start

1. 先确认学习目标、当前基础、时间预算、输出场景。
2. 把需求写成学习者画像（见 `assets/learner-profile-template.md`）。
3. 用权威来源优先策略建立资料池（见 `references/authority-first-research.md`）。
4. 组装学习包：路径图 + 阶段任务 + 练习 + 复盘机制（见 `references/tutorial-assembly.md`）。
5. 如果用户要求，再导出 docx/pdf；默认 Markdown 为唯一母稿。

## Default Contract

- 默认语言：中文
- 默认输出：一份学习包（Markdown）+ 来源附录
- 默认人群：创作者 / 超级个体 / 一人公司场景的自学者
- 默认结果：不仅“理解知识”，还要能做出阶段性输出（文章、案例拆解、讲稿或项目草稿）
- 默认研究策略：优先官方文档、标准文档、权威机构资料、维护者文档

## Workflow

### Step 1: 学习者画像澄清

至少澄清：

- 学什么（主题边界）
- 为何要学（目标结果）
- 现在在哪（已有基础）
- 有多少时间（节奏与周期）
- 打算怎么用（输出场景）

缺关键输入时，先列 blockers，不直接开写教程。

### Step 2: 权威来源优先研究

建立“可信资料池”，并给每条来源写明：

- 来源类型（官方/标准/维护者/高质量二手）
- 为什么可信
- 对本学习目标的作用
- 适合放在哪个阶段

### Step 3: 学习包组装

按“能执行”而不是“看起来完整”来设计：

- 路径图：从入门到可输出
- 阶段任务：每阶段有动作、有产物
- 练习设计：每阶段至少 1 个可检验练习
- 里程碑：能判断是否进入下一阶段
- 风险提示：常见误区与偏航信号

### Step 4: 输出与可选扩展

默认交付：

- 学习包主文档（Markdown）
- 来源附录（含 URL + 日期 + 可信理由）

按需交付：

- docx / pdf 导出建议与命令
- 学完后的“内容产出计划”（用于写作或分享）

## Output Format

默认使用 `assets/learning-pack-template.md`。

输出至少包含：

- 学习目标与边界
- 学习者画像摘要
- 分阶段学习路径
- 每阶段练习与验收标准
- 来源附录
- 30 天复盘建议

## Hard Rules

Do not:

- 把学习包写成泛泛知识科普
- 用大量低可信转载凑来源数量
- 只给信息不给行动步骤
- 忽略用户时间约束与输出目标

Always:

- 先澄清再研究
- 来源优先级清晰可解释
- 每阶段都可执行、可验证
- 明确“学完要能产出什么”

## Resource Map

- [references/authority-first-research.md](references/authority-first-research.md)
  - 资料选择优先级与可信度判断。
- [references/tutorial-assembly.md](references/tutorial-assembly.md)
  - 学习包结构与写作契约。
- [assets/learner-profile-template.md](assets/learner-profile-template.md)
  - 学习者画像采集模板。
- [assets/learning-pack-template.md](assets/learning-pack-template.md)
  - 最终交付模板。

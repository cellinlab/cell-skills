---
name: perspective-distiller
description: Distill a public figure, creator, thinker, operator, or theme into a reusable Chinese perspective skill. Use when Codex needs to research how someone thinks instead of merely what they said: gather primary materials, run six research lanes, extract mental models and decision heuristics with validation, preserve tensions and limits, and generate or update a self-contained perspective-skill folder.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/perspective-distiller"}}
---

# Perspective Distiller

## Overview

把一个人或一个主题蒸成一套可运行的认知视角。

核心不是模仿口气，而是提炼：

- 他怎么想
- 他怎么判断
- 他怎么表达
- 他绝对不做什么
- 他在哪些地方不该被假装“完整复刻”

最终目标不是一篇人物介绍，而是一个可复用的视角 Skill 包。

## Quick Start

1. 先判断目标是人物还是主题。
2. 锁定用途：顾问型、角色型，还是研究沉淀型。
3. 优先吃用户提供的一手素材，再补公开资料。
4. 按六路研究工作流收集证据。
5. 只把通过验证的内容升级为核心心智模型。
6. 生成自包含 Skill 包，并跑质量检查。

如果材料太薄，不要硬蒸。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文
- 信息边界：公开信息 + 用户明确提供的一手材料
- 输出形态：一个自包含 Skill 目录
- 默认模式：顾问型视角优先，角色表演其次
- 默认研究策略：本地材料优先，原始来源优先，低质量二手材料只作线索

## Workflow

### Step 0: Scope the Distillation

先判断：

- 目标是人物还是主题
- 是新建还是更新
- 是否有本地素材
- 用户想要的是：
  - `advisor-first`
  - `role-first`
  - `research-only`

如果目标过于模糊，先把对象与用途说清楚，再进入采集。

### Step 1: Set Up the Target Skill Folder

默认在当前工作区创建或更新：

```text
skills/<target-slug>/
├── SKILL.md
├── references/
│   └── research/
└── assets/ (optional)
```

若用户给了已有目录，则在原目录上更新，不要另起炉灶。

完整结构要求见 [references/output-contract.md](references/output-contract.md)。

### Step 2: Run the Six Research Lanes

按六路研究工作流收集信息：

1. writings
2. conversations
3. expression DNA
4. external views
5. decision records
6. timeline and recent updates

工具和策略允许时可以并行；否则顺序跑完也可以，但不要跳 lane。

详细规则见 [references/research-lanes.md](references/research-lanes.md)。

### Step 3: Extract the Cognitive Operating System

对研究材料做五层提炼：

- core mental models
- decision heuristics
- expression DNA
- anti-patterns / values
- honest boundary

只有通过验证的内容才能进入核心心智模型。

详细方法见 [references/extraction-framework.md](references/extraction-framework.md)。

### Step 4: Build the Perspective Skill

用 [assets/perspective-skill-template.md](assets/perspective-skill-template.md) 组装最终 Skill。

默认要求：

- 3-7 个核心心智模型
- 5-10 条决策启发式
- 明确的表达 DNA
- 可见的张力与矛盾
- 明确的诚实边界
- 附录保留研究来源

### Step 5: Validate Before Delivery

优先做两层验证：

1. 结构验证：字段是否完整、数量是否合理、边界是否清楚
2. 视角验证：是否真的像这个人的认知框架，而不是名句拼贴

可用 `scripts/quality_check.py` 做快速结构检查。

如果用户提供了字幕文件或下载后的 SRT/VTT，可用 `scripts/srt_to_transcript.py` 先清洗为可读 transcript。

## Output Format

默认交付一个自包含 Skill 包，并在回复里说明：

- 目标对象与模式
- 主要来源类型
- 提炼出的核心模型数
- 是否保留了主要张力与边界
- 还缺什么信息

## Hard Rules

Do not:

- 把人物语录堆成一个 Skill
- 用单一来源硬凑完整认知系统
- 把低可信二手材料写成事实
- 抹平明显矛盾
- 假装这个 Skill 能替代真人本人
- 为了“像”而过度模仿表层口癖

Always:

- 优先原始材料
- 区分事实、引述、外部观察和推断
- 保留张力、演化和信息不足
- 让结果目录自包含
- 写清楚诚实边界

## Resource Map

- [references/extraction-framework.md](references/extraction-framework.md)
  - 读这个文件来判断什么才算真正的心智模型、如何处理矛盾、如何标注置信度。
- [references/research-lanes.md](references/research-lanes.md)
  - 读这个文件来安排六路研究、选择信源、处理本地素材优先模式。
- [references/output-contract.md](references/output-contract.md)
  - 读这个文件来确定目标 Skill 的目录结构、章节契约和 advisor/role 模式差异。
- [assets/perspective-skill-template.md](assets/perspective-skill-template.md)
  - 最终 Perspective Skill 的模板。
- [assets/research-dossier-template.md](assets/research-dossier-template.md)
  - 六路调研文件的记录模板。
- [scripts/srt_to_transcript.py](scripts/srt_to_transcript.py)
  - SRT/VTT 转 transcript 的辅助脚本。
- [scripts/quality_check.py](scripts/quality_check.py)
  - 快速质量检查脚本。

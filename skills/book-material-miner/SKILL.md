---
name: book-material-miner
description: "Book-to-writing-material skill for Chinese content creation. Use when Codex needs to break down a book, chapter, excerpt, reading note, or book link into reusable writing materials instead of a normal book report:观点、故事、金句化表达、概念对比、可直接调用的素材块，以及一篇适合交给 $deep-writer 继续深化的素材文章。"
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/book-material-miner"}}
---

# Book Material Miner

## Overview

把一本书拆成可复用的写作素材包，而不是写成一份常规读书笔记或章节摘要。

这个 skill 的核心做法是分轮加压：

- 先找出这本书真正回答的问题、张力和概念骨架
- 再把书中的可用内容压缩成观点、故事、金句化表达和素材块
- 最后重组出一篇适合交给 `$deep-writer` 的素材文章

目标不是“证明你读懂了书”，而是“让这本书以后还能反复为写作供弹药”。

## Quick Start

1. 判断输入类型：书名、章节、摘录、读书笔记、文章链接，还是混合材料。
2. 判断用户真正想要的素材方向：主题、立场、受众、使用场景。
3. 完成第一轮后再进入细颗粒提炼，不要一上来就堆观点清单。
4. 只保留对后续写作有用的内容，不做机械逐章复述。
5. 最后一定交付“素材文章”与 `$deep-writer` 交接信息，除非用户明确不要。

如果用户只要观点库、故事库或金句库，停在对应层即可，不要强行补全全部产物。

## Default Contract

默认按以下约定执行，除非用户另有说明：

- 必填输入：书名、内容摘录、章节摘要、读书笔记、书籍链接中的至少一种
- 选填输入：目标主题、目标读者、发布场景、希望产出的内容方向、长度与深度
- 默认语言：中文
- 默认目标：沉淀可复用写作素材，而不是输出“我从这本书学到了什么”的心得
- 默认引用策略：优先做“金句化改写”，不是大段照抄原书
- 默认证据策略：区分“书里明确说的”“书里案例呈现的”“你基于材料外推的”
- 默认深写交接策略：
  - 如果素材文章已经是成形草稿，适合交给 `$deep-writer` 的 `draft-deepening`
  - 如果素材文章更像整理后的原始底稿，适合交给 `$deep-writer` 的 `source-driven`

## Workflow

### Round 1: 主题与张力扫描

先回答“这本书对写作有什么用”，而不是“这本书讲了几章”。

至少完成：

- 判断输入模式与材料覆盖度
- 提炼本书的中心问题、核心回答、关键张力
- 找出 3-7 个最值得转成内容的写作角度
- 提炼高频概念、关键对照、可反复调用的认知框架
- 标出材料充足处、材料薄弱处、需要保守处理的部分

输出至少包含：

- 拆书定位卡
- 中心问题与一句话主张
- 关键张力或冲突对
- 写作角度候选
- 材料覆盖说明

当只有书名、内容很碎、或者用户没有给出写作方向时，先读 [references/workflow.md](references/workflow.md)。

### Round 2: 素材颗粒提炼

把书里的内容变成可调用的素材单元，而不是泛泛总结。

优先提炼四类内容：

- 观点：能成为论点、反常识判断、结构判断的内容
- 故事：案例、实验、人物片段、历史情境、隐喻场景
- 金句化表达：适合开头、结尾、转折、点题的短表达
- 素材块：把多个颗粒拼成可以直接写进文章的一段或一节

每个强素材都尽量回答：

- 它到底在说什么
- 为什么值得写
- 适合写在哪类文章里
- 能朝哪几个方向展开
- 依据来自哪里

当你需要更细的块类型与字段定义时，读 [references/block-taxonomy.md](references/block-taxonomy.md)。

输出至少包含：

- 观点库
- 故事库
- 金句库
- 素材块库初稿
- 明显的信息缺口或不确定性说明

### Round 3: 写作重组

把前两轮的颗粒重新组织成“未来能直接拿去写”的素材包。

至少完成：

- 将素材按主题线、论证线或读者问题线重新聚类
- 选出最值得进入素材文章的主线与支线
- 生成一篇“素材文章”：信息密度高、结构清晰、论点可继续深化，但不必过度打磨成终稿
- 追加 `$deep-writer` 交接信息：建议模式、读者、场景、中心命题、建议结构

素材文章的目标不是替代深度写作，而是给深度写作一个更强、更净、更可控的起点。

生成素材文章前，读 [references/quality-bar.md](references/quality-bar.md)。

## Output Format

默认使用 [assets/material-pack-template.md](assets/material-pack-template.md)。

当需要交给 `$deep-writer` 时，再按 [assets/deep-writer-source-template.md](assets/deep-writer-source-template.md) 组织最后一段“素材文章”和交接说明。

如果用户只要局部输出，可以只返回其中相关章节，但仍建议保留：

- 材料边界说明
- 适用写作方向
- 不确定性提示

## Hard Rules

Do not:

- 把拆书结果做成普通章节摘要来交差
- 为了显得高级而堆很多空泛判断
- 把未经验证的推测包装成书中原意
- 大段直接摘抄原书文字充当金句库
- 生造书中没有的案例、人物细节、实验设置或数据
- 输出一堆“好句子”却说不清它们该怎么用
- 在用户要素材包时直接越界写成完整成品文章

Always:

- 优先提炼“可复用素材”而不是“完整复述”
- 区分书中原观点与你的延伸解释
- 给每个强观点或强故事补上“可用场景”
- 保留书中最有张力、最适合写作的冲突和反差
- 把最后的素材文章写成适合继续深写的中间产物
- 在材料不足时直说不足，不硬凑

## Resource Map

- [references/workflow.md](references/workflow.md)
  - 读这个文件来判断输入模式、三轮提炼顺序、标题党式拆书风险，以及如何从“读懂一本书”切换到“提炼可写素材”。
- [references/block-taxonomy.md](references/block-taxonomy.md)
  - 读这个文件来确定观点块、故事块、金句块、概念块、对比块和动作块的字段。
- [references/quality-bar.md](references/quality-bar.md)
  - 读这个文件来检查素材是否真能用于写作，以及素材文章是否适合交给 `$deep-writer`。
- [assets/material-pack-template.md](assets/material-pack-template.md)
  - 默认输出模板，适合一次性交付完整拆书素材包。
- [assets/deep-writer-source-template.md](assets/deep-writer-source-template.md)
  - 最后一段素材文章与交接信息模板，适合给 `$deep-writer` 做后续深写。

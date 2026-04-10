---
name: x-content-mentor
description: X/Twitter content strategy skill for Chinese creators, indie builders, and expert accounts. Use when Codex needs to decide whether an idea belongs on X, turn projects or experiences into X-native topics, write or review posts and threads, diagnose growth bottlenecks, or analyze an account from recent post data; route between topic strategy, writing, review, growth, and account diagnosis instead of free-generating tweets blindly.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/x-content-mentor"}}
---

# X Content Mentor

## Overview

把 X 上的内容工作，当成一个系统，不当成“随手写条推文”。

这个 Skill 主要解决五类问题：

- 不知道发什么
- 知道要发什么，但不知道怎么写成 X 原生内容
- 已经写了，想判断问题在哪里
- 账号有内容但增长停滞
- 想做一次结构化账号诊断并沉淀历史策略

它不是通用 tweet 生成器，而是一个路由式内容策略 Skill。

## Quick Start

1. 先判断当前属于哪个场景：选题、写作、审阅、增长，还是账号诊断。
2. 锁定受众、语言、目标动作，不要跳过。
3. 只读取当前场景需要的 reference，不一次性全读。
4. 如果真正的问题不在 X 写法，明确指出并切给更合适的 Skill。
5. 结束时给一个可直接执行的下一步。

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出解释用中文
- 如果目标平台是英文 X，正文内容用英文，解释与策略仍可用中文
- 优先判断“值不值得发”和“该怎么发”，再讨论具体 wording
- 不承诺爆款，不把历史算法经验当作绝对规律
- 如做过账号诊断，优先利用已有沉淀

## Workflow

### Step 1: Scope the Input

先判断用户手上有什么：

- 一个项目、经验、观察，想发出去
- 一条已经写好的短帖或 Thread
- 一个增长困惑
- 一个要分析的账号

同时锁定四个变量：

- 目标受众是谁
- 想要什么结果：增长、建认知、招募、导流、产品验证
- 发中文、英文，还是双语
- 当前账号大致处于什么阶段

如果这些信息缺得太厉害，不要假装确定。

### Step 2: Route to the Right Scene

按下面路由处理：

| 场景 | 什么时候进入 | 按需读取 |
| --- | --- | --- |
| A. 选题与方向 | 用户不知道发什么，或不知道某个项目怎么转成 X 内容 | [references/topic-engine.md](references/topic-engine.md) |
| B. 写短帖 / Thread | 用户已经有方向，想起草内容 | [references/writing-workshop.md](references/writing-workshop.md) |
| C. 审阅现有内容 | 用户给了现成帖子，需要诊断或改写 | [references/review-scorecard.md](references/review-scorecard.md) + [references/writing-workshop.md](references/writing-workshop.md) |
| D. 增长与策略 | 用户问涨粉、定位、分发、导流 | [references/growth-engine.md](references/growth-engine.md) |
| E. 账号诊断 | 用户要系统看账号数据与内容结构 | [references/account-diagnosis.md](references/account-diagnosis.md) + [references/review-scorecard.md](references/review-scorecard.md) |

### Step 3: Apply Scene Rules

#### Scene A: Topic and Direction

- 把用户素材先转成“可在 X 上成立的角度”，再写帖
- 优先判断它适合：
  - short post
  - thread
  - series
  - or not X at all
- 如果主题 promise 太弱、材料太薄、目标不清，先指出，不硬写

#### Scene B: Writing

- 先决定短帖还是 Thread
- 先给 2-4 个 hook 方向，再展开成正文
- 对英文 X 内容：
  - 正文用英文写
  - 不做中文句子直译式英文
- Thread 默认要有：
  - opening promise
  - structured middle
  - 收束或 CTA

#### Scene C: Review

- 先判断这是题的问题、hook 的问题、结构的问题，还是账号语境的问题
- 默认先给诊断，再决定是否给改写版
- 区分：
  - 同一路径优化
  - 换一种路径重写

#### Scene D: Growth

- 先判断阶段：冷启动、验证期、放大期
- 不要一上来讲宏大增长理论
- 优先指出当前最限制增长的一件事：
  - 定位太散
  - 题材不对
  - 写法抓力不足
  - 互动动作缺失
  - 没有把高表现内容扩成可复利资产

#### Scene E: Account Diagnosis

- 先判断是否已有历史数据
- 如无数据，按可获得性分级采样
- 输出不只给结论，还要沉淀到用户数据目录
- 如样本不足，明确标注

### Step 4: Hand Off When Needed

以下情况不要硬留在本 Skill 内：

- 题目本身不成立，先交给 `$content-strategy-diagnosis`
- 只是前两句抓力弱，先交给 `$hook-optimizer`
- 结构对了但风格太平，交给 `$celf-style-writer`
- 想找对标账号或案例，交给 `$benchmark-filter`

## User Data Persistence

账号诊断默认把用户历史信息保存在：

```text
user-data/x-content-mentor/<username>/
├── profile.md
├── posts_<date>.json
├── posts_<date>.md
├── report_<date>.md
└── strategy.md
```

规则：

- 如果已有 `strategy.md`，默认静默读取，用来提高后续建议的针对性
- 如果上次诊断已超过 30 天，提醒重新诊断
- 如果只有部分样本，照做，但把样本量不足写进结论

## Output Format

标准输出默认参考 [assets/x-strategy-pack-template.md](assets/x-strategy-pack-template.md)。

账号诊断默认参考 [assets/account-diagnosis-template.md](assets/account-diagnosis-template.md)。

## Hard Rules

Do not:

- 把所有请求都简化成“我给你写三条 tweet”
- 用过度确定的算法数字伪装成实时事实
- 忽略受众、语言、账号阶段
- 只给漂亮 wording，不给结构性判断
- 为了看起来专业，把简单动作说得很复杂

Always:

- 先判断场景
- 先说最关键的问题或机会
- 明确区分高置信度共识与阶段性经验
- 在账号诊断里留下可复用的策略沉淀
- 让建议能跟仓库内其他 Skill 接力

## Resource Map

- [references/topic-engine.md](references/topic-engine.md)
  - 读这个文件，把项目、经验、观察转成适合 X 的题材与角度。
- [references/writing-workshop.md](references/writing-workshop.md)
  - 读这个文件，处理短帖、Thread、hook 与语言适配。
- [references/growth-engine.md](references/growth-engine.md)
  - 读这个文件，判断账号阶段、分发动作与增长策略。
- [references/review-scorecard.md](references/review-scorecard.md)
  - 读这个文件，诊断现有内容、做复盘与反模式排查。
- [references/account-diagnosis.md](references/account-diagnosis.md)
  - 读这个文件，做数据采样、诊断结构与用户数据留存。
- [assets/x-strategy-pack-template.md](assets/x-strategy-pack-template.md)
  - 标准场景的输出模板。
- [assets/account-diagnosis-template.md](assets/account-diagnosis-template.md)
  - 账号诊断输出模板。

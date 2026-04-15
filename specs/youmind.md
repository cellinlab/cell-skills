# YouMind CLI Skill 设计文档

## 1. 目标概述

这个 Skill 用于把 YouMind 官方的 OpenAPI CLI 能力引入到当前仓库，提供一条稳定的 `search -> info -> call` 调用链路。

它解决的不是内容写作、知识整理或公众号发布，而是帮助用户完成下面这些动作：

- 安装并验证 `@youmind-ai/cli`
- 配置 `YOUMIND_API_KEY`
- 搜索可用的 YouMind API 能力
- 查看具体接口 schema
- 在确认参数后调用接口

这个 Skill 的价值是把 “YouMind API 怎么找、怎么确认、怎么调” 这件事做成一个可复用的基础能力，后续也能为其他需要 YouMind 能力的 Skill 提供底层入口。

## 2. 设计来源

这个 Skill 主要参考 `cellinlab/youmind-skills` 分支 `improve-youmind-skill-docs` 下的 `skills/youmind/SKILL.md`，也就是基于 `YouMind-OpenLab/skills` 官方 skill 继续扩写后的版本；同时保留对上游 commit `db33838c36621edf04481e6a143706b7d0e2cbff` 的设计追溯。

保留的部分：

- 使用 `youmind` CLI 作为统一入口
- 采用 `search -> info -> call` 的三段式工作流
- 把安装、鉴权、命令形式、功能索引和常见操作路径讲清楚

改造的部分：

- 先按本仓库规范补 `specs/`，再落 `skills/`
- 运行层文档只保留执行规则，不保留上游来源叙述
- 用更贴近本仓库风格的方式，明确它和内容类 Skill 的边界，同时保留你扩写版里的功能索引结构
- 补 `agents/openai.yaml` 与 README 索引，方便在本仓库发现和复用

## 3. 技能定位

它是一个 “YouMind API / CLI 调用适配器” Skill。

它不是：

- 文章写作 Skill
- 公众号发布 Skill
- 选题诊断 Skill
- YouMind 平台能力全集介绍页

更准确地说，它负责的是 “在终端里稳定调用 YouMind OpenAPI”。

## 4. 与现有 Skill 的关系

- `wechat-draft-publisher`
  - 负责公众号草稿发布
- `deep-writer`
  - 负责写作
- `content-strategy-diagnosis`
  - 负责内容策略判断
- `youmind`
  - 负责 YouMind CLI 安装、接口发现、schema 查看和 API 调用

理想顺序通常是：

1. 先用 `youmind` 取到 YouMind 侧能力或内容数据
2. 再把结果交给写作、研究或发布类 Skill

## 5. 建议技能名

建议英文目录名：

`youmind`

建议展示名：

`YouMind API`

## 6. 适用场景

这个 Skill 主要适用于：

- “帮我调 YouMind API”
- “查一下 YouMind 有哪些接口”
- “看看这个 YouMind 接口需要什么参数”
- “用 YouMind CLI 创建 board / note / craft”
- “把官方 youmind skill 也加到我的仓库”

## 7. 非目标

V1 默认不解决以下问题：

- 替用户设计复杂业务流程
- 在不了解 schema 时盲调接口
- 在没有 API key 的情况下假装已经调用成功
- 接管其他 Skill 的业务逻辑

## 8. 核心用户问题

这个 Skill 需要稳定回答以下问题：

1. 本机有没有安装 `youmind` CLI？
2. 该先查哪个 API，而不是直接猜名字？
3. 某个接口到底需要哪些参数？
4. 什么时候可以真正执行 `call`，什么时候应该先停下来补鉴权？
5. 调用失败时，是安装问题、鉴权问题、还是参数问题？

## 9. 默认输入约定

### 9.1 必填输入

- 至少提供以下之一：
  - 一个想完成的 YouMind 动作
  - 一个明确的 API 名

### 9.2 选填输入

- `YOUMIND_API_KEY`
- `YOUMIND_BASE_URL` 或 `--base-url`
- 已知的参数 JSON
- 当前报错信息

### 9.3 默认假设

如果用户没特别说明，默认：

- 输出解释用中文
- 优先通过 `youmind search` 找接口，而不是直接猜
- 在真正执行 `call` 之前先跑 `info`
- 如果缺 `YOUMIND_API_KEY`，只做到安装 / 搜索 / schema 检查，不伪造调用结果

## 10. 输出契约

### 10.1 成功调用

至少包含：

- 实际使用的 API 名
- 关键参数形式
- 调用结果摘要

### 10.2 调用失败

至少包含：

- 失败发生在哪一步
- 关键报错信息
- 下一步要补的是安装、鉴权还是参数

## 11. 方法论原则

### 11.1 先发现，再调用

优先 `search` 和 `info`，不要凭印象直接 `call`。

### 11.2 schema 是真相来源

接口参数以 `youmind info <name>` 的输出为准，而不是猜测。

### 11.3 没有鉴权就不要伪造执行

缺少 `YOUMIND_API_KEY` 时，可以做安装和接口发现，但不能假装已经成功执行写操作。

### 11.4 运行层只写执行规则

来源、上游和 commit 背景只留在 spec，不进入 skill 实现层。

## 12. 资源规划

建议资源结构：

- `skills/youmind/SKILL.md`
  - 适用场景、安装、鉴权、命令工作流、硬约束
- `skills/youmind/agents/openai.yaml`
  - 展示名和默认 prompt

## 13. V1 关键约束

1. 不把这个 Skill 写成 YouMind 平台宣传页
2. 不在未确认 schema 时直接猜参数
3. 不在缺 API key 时伪造 `call` 成功
4. 不在运行层写上游来源叙述

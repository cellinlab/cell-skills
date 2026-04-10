# 目标 Skill 交付契约

## 1. 目标目录

默认生成：

```text
skills/<target-slug>/
├── SKILL.md
├── references/
│   └── research/
├── assets/        # 可选
└── agents/
    └── openai.yaml
```

如果用户只要研究，不要擅自生成完整 Skill。

## 2. 最终 SKILL.md 至少包含

- frontmatter
- overview / quick-start
- 使用模式说明
- 身份卡或主题卡
- 3-7 个核心心智模型
- 5-10 条决策启发式
- 表达 DNA
- 价值观 / 反模式 / 核心张力
- 诚实边界
- 来源说明

## 3. Advisor-first vs Role-first

### advisor-first

更适合：

- 决策辅助
- 研究对话
- 思考框架借用

特点：

- 不需要强角色表演
- 优先清楚、稳、可解释

### role-first

更适合：

- 明确要“用某人视角聊天”
- 已有足够一手材料

特点：

- 可使用第一人称
- 但仍要保留边界与不确定性

默认优先 `advisor-first`，除非用户明确想要角色模式。

## 4. 更新模式

如果是更新已有 Skill：

- 先读旧版 SKILL.md
- 标出保留部分
- 补充最近资料
- 缩掉已经站不住的内容
- 不要重写到完全看不出连续性

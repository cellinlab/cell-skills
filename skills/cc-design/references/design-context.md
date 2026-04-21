# Design Context

> **Load when:** 任务是新设计、模糊设计，或者用户没给清楚设计系统 / 参考资产
> **Skip when:** 用户已经提供了明确的设计系统、代码、截图和输出要求
> **Why it matters:** 高保真设计最容易失败的地方，不是代码，而是从错误或过少的上下文出发
> **Typical failure it prevents:** 凭空设计、视觉 generic、品牌跑偏、做出“还行但不像用户产品”的结果

## Context Priority

设计上下文按优先级看：

1. 用户自己的设计系统 / token / 组件库
2. 用户项目里的现有代码和页面
3. 用户已经上线的产品截图 / URL
4. 品牌资产：logo、产品图、UI 截图、品牌规范
5. 用户给的竞品或参考
6. 通用风格 fallback

只要能拿到前面的层，就不要直接跳到后面的层。

## What to Ask

如果这是一个新任务，优先一次性问完，而不是一轮只问一个问题：

- 有没有 design system / UI kit / token 文件？
- 有没有现有页面、截图或代码可以读？
- 有没有品牌规范、logo、产品图或 UI 素材？
- 有没有希望参考的产品或风格对象？
- 希望做几种方向？哪些维度允许变化？

## What to Read

如果用户给了代码库，优先找：

- `theme.*`
- `tokens.*`
- `colors.*`
- `globals.css`
- 代表性组件：`Button`、`Card`、`Input`、`Layout`

目标不是“了解大概风格”，而是提取：

- 颜色
- 字体
- 间距尺度
- 圆角和阴影
- 组件语言

## When Context Is Missing

如果用户没有任何上下文，不要直接假装自己知道该做成什么样。

按这个顺序处理：

1. 先告诉用户：没有 design context，会显著增加 generic 风险
2. 再尝试从任务语义里提炼方向线索
3. 如果仍然模糊，切到 `design-direction-advisor.md`
4. 只有在用户接受 fallback 的情况下，才基于通用方向开做

## What to Tell the User Before Building

在真正开始写 HTML 前，先把你提炼出的系统用简短清单说出来：

- 主色 / 中性色
- 标题字体 / 正文字体
- 间距尺度
- 圆角 / 阴影
- 页面语言或参考对象

这一步的作用不是解释自己多聪明，而是给用户一次低成本纠偏机会。

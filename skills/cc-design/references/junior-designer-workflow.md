# Junior Designer Workflow

> **Load when:** 新任务、模糊任务、范围较大任务，或用户还没确认视觉方向
> **Skip when:** 只是局部微调、修 bug、或用户已经把方向钉死
> **Why it matters:** 设计里最贵的错误是方向错了却做到最后才暴露
> **Typical failure it prevents:** 闷头做完一整版才发现理解错了；只给最终稿不给过程确认点；用户无法低成本纠偏

## Core Mindset

把自己当成“会主动汇报的 junior designer”，不是闷头放大招的黑箱。

## Pass 1: Assumptions + Placeholder

开工后的第一版不追求完美，先追求方向可见。

至少要明确：

- 你对受众和目标的假设
- 你理解的页面主焦点
- 你还不确定的部分
- 哪些内容先用 placeholder

必要时把这些假设写进 HTML 注释里，方便用户和后续 agent 读。

## Pass 2: Core Build

用户确认方向后，再进入真正的布局、视觉和组件实现。

这时候重点是：

- 把 placeholder 变成真实结构
- 如果需要，提供 2-3 个方向或 tweak 切换
- 在完成 40%-70% 时再给用户看一次

不要憋到 100% 才第一次展示。

## Pass 3: Polish

整体方向稳定后，再打磨：

- 字重和字号
- 留白和节奏
- 动画 timing
- hover / pressed / focused 细节
- 文案密度

## Pass 4: Verify + Deliver

最后才做：

- 结构验证
- 截图验证
- 交互路径验证
- 导出验证（如果需要）

## What to Show the User

用户中途查看时，重点展示：

- 你现在押的方向是什么
- 还没定的是什么
- 用户最值得现在决定的 1-3 个问题

不要把阶段性汇报写成冗长复盘。

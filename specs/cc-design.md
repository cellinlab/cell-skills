# CC Design Skill 设计文档

## 1. 目标概述

这个 Skill 用于把“做一个视觉稿 / 原型 / 页面 / 演示稿”的模糊设计请求，收敛成一条稳定的 HTML 设计工作流。

它解决的不是“随便生成一个看起来像网页的东西”，而是帮助用户完成下面这些更具体的动作：

- 先澄清输出格式、保真度、屏数、风格和约束
- 优先复用现有品牌系统、设计 token、组件语言与项目上下文
- 在没有现成设计系统时，提供一套不容易落入 AI 套路的视觉起点
- 用 HTML / CSS / 可选 React JSX 产出高保真视觉稿、落地页、交互原型、移动端 mockup 或演示稿
- 用模板脚手架加速常见场景：slide deck、浏览器窗口、移动设备框、动画时间轴、方案对比画布
- 在交付前做结构校验、视觉校验与导出准备，而不是“写完即交”

这个 Skill 的价值在于把“设计判断 + HTML 原型实现 + 预览校验 + 导出准备”串成闭环，而不是把设计任务退化成普通前端切图。

## 2. 设计来源

这个 Skill 主要参考上游仓库 `ZeroZ-lab/cc-design` 的结构和方法论，也会吸收其中关于：

- 设计任务分流
- 视觉判断前置
- 模板脚手架复用
- React + Babel 原型约束
- 预览验证和导出脚本

的组织方式。

第二轮优化会继续参考 `alchaincyf/huashu-design`，重点学习它在下面这些方面的稳定性设计：

- 事实验证先于设计假设
- 品牌 / 产品任务下的资产协议
- 模糊需求时的风格方向顾问模式
- “junior designer” 分阶段工作流
- 设计评审维度化输出
- 针对 deck / prototype / review 的更细颗粒度约束

保留的部分：

- 设计任务先分流，再按需加载 references
- 把“先理解、再路由、再设计、再验证”做成主流程
- 用模板和脚本承接 slide deck、device frame、动画、导出等重复能力
- 强调截图校验和 console 校验，而不是只看代码
- 支持品牌风格加载和案例参考，避免凭空做视觉

改造的部分：

- 先按本仓库规范补 `specs/`，再落 `skills/`
- 运行层全部改成适合 Cell 仓库的写法，不保留来源叙述
- 把目录结构适配为本仓库更常见的 `assets/templates/` 形式，而不是顶层 `templates/`
- 把上游偏 Claude Code / AskUserQuestion 的说法，改成更通用的运行指令
- 默认输出说明、工作流表达和约束提示改成更适合中文协作语境
- 明确这个 Skill 是“HTML 设计与原型 Skill”，不是纯视觉灵感收集器，也不是 Figma 插件替代品
- 不直接照搬 `huashu-design` 的整套音视频、BGM/SFX、showcase 大资产库，而是提炼其中最能提升 `cc-design` 稳定性的流程骨架与约束

## 3. 技能定位

它是一个“高保真 HTML 设计 / 原型 / 视觉探索 / 演示稿制作” Skill。

它不是：

- 普通网页切图 Skill
- 通用前端工程脚手架 Skill
- 只会给配色建议的视觉点评 Skill
- Figma 文件生产 Skill
- 图片生成 Skill

更准确地说，它处理的是“用户需要可运行、可预览、可迭代的 HTML 设计产物”。

## 4. 与现有 Skill 的关系

- `cc-design`
  - 负责 HTML 设计稿、落地页、演示稿、交互原型、移动端视觉稿
- `xhs-image-director`
  - 负责小红书封面、轮播图、信息图方向提案与配图协作
- `speech-structure-coach`
  - 负责演讲 / 分享内容结构，不负责把它实现成视觉 deck
- `wechat-draft-publisher`
  - 负责公众号草稿发布，不负责视觉原型
- `x-article-publisher`
  - 负责 X Articles 草稿发布，不负责页面设计

理想顺序通常是：

1. 先用策略 / 写作 / 结构类 Skill 确定内容
2. 再用 `cc-design` 把内容做成视觉化 HTML 产物

## 5. 建议技能名

建议英文目录名：

`cc-design`

建议展示名：

`CC Design`

## 6. 适用场景

这个 Skill 主要适用于：

- “帮我做一个 SaaS 落地页”
- “把这个需求做成 10 页演示稿”
- “做一个高保真移动端 onboarding 原型”
- “给这个功能页出 3 个视觉方向”
- “帮我把这个 dashboard 做得像一个成熟产品”
- “做一个能预览、能截图、能导出 PDF / PPTX 的 HTML 设计稿”

## 7. 非目标

V1 默认不解决以下问题：

- 直接产出 Figma 文件
- 替用户生成复杂品牌资产本身
- 完整承担业务文案和产品策划
- 覆盖所有宿主平台下的浏览器预览与导出差异
- 把每种视觉方向都扩成大型 design system 工程

## 8. 核心用户问题

这个 Skill 需要稳定回答以下问题：

1. 用户这次要的到底是 slide、landing page、mobile mockup 还是交互原型？
2. 什么时候应该先复用现有设计系统，什么时候可以新建一套视觉基线？
3. 如何避免生成“标准 AI 网页风”的平庸设计？
4. 哪些场景应该直接复用模板而不是从零搭？
5. 交付前如何证明这个 HTML 设计稿真的可用、可看、可导出？

## 9. 典型触发语句

- 做一个登录页 / 落地页 / 定价页
- 设计一个 dashboard / app screen / onboarding flow
- 给这个功能出三版视觉方向
- 做一个 pitch deck / keynote deck
- 帮我把这个原型做得像成熟产品
- 用某个品牌风格做一版页面
- 做一个能交互点击的 HTML prototype

## 10. 默认输入约定

### 10.1 必填输入

- 至少提供以下之一：
  - 明确的设计目标
  - 一份已有内容材料
  - 一个现有项目 / 页面 / 设计系统上下文

### 10.2 选填输入

- 输出类型：落地页 / deck / mobile / prototype / mockup
- 屏数或页面数量
- 保真度：线框 / 中保真 / 高保真
- 风格方向：极简 / 技术 / 温暖 / 大胆 / 品牌化
- 品牌参考或竞品 URL
- 是否需要导出 PPTX / PDF / 单文件 HTML

### 10.3 默认假设

如果用户没特别说明，默认：

- 输出解释用中文
- 视觉产物用 HTML 交付
- 如果有现成设计系统，优先复用，不先发明新的
- 如果没有现成系统，先从受控的视觉规则和 token 出发
- 默认至少给出 2-3 个方向中的一种比较或 tweak 入口
- 交付前默认做结构检查和截图检查

## 11. 输出契约

### 11.1 标准输出

至少包含：

- 明确的文件产物（HTML 为主）
- 输出类型与适配说明
- 所采用的视觉方向 / 设计系统说明
- 是否通过结构校验与截图校验
- 如有导出，说明生成了什么文件

### 11.2 交付形态

默认交付为一个 Skill 目录，包含：

- `SKILL.md`
- `agents/openai.yaml`
- `references/*.md`
- `assets/templates/*`
- `scripts/*`

### 11.3 仓库改造型任务

如果用户要的是“把这个 Skill 加进仓库”，而不是只跑一次设计任务，至少包含：

- 触发范围定义
- 核心工作流
- 模板和脚本职责划分
- 导出链路说明
- 已验证与未验证部分

## 12. 方法论原则

### 12.1 先看上下文，再做视觉

设计任务不应该默认从白纸开始。只要项目已有品牌、组件、色板、页面语言，就优先复用。

### 12.2 视觉判断要前置

在开始写 HTML 之前，先判断：

- 这页最重要的视觉焦点是什么
- 情绪基调是什么
- 层级和留白如何组织
- 是否需要多个方向

### 12.3 模板是加速器，不是风格替代品

deck stage、device frame、design canvas、animation stage 这些模板的作用是减少重复劳动，不是替代视觉判断。

### 12.4 验证是交付的一部分

如果没有 console 检查、截图检查、基础结构检查，这个 Skill 就不算完成了设计闭环。

### 12.5 运行层只保留执行规则

来源、学习对象、保留 / 改造关系只留在 `specs/`，不写进 `skills/` 运行层。

### 12.6 先提升稳定性，再扩功能面

第二轮升级优先补：

- 设计前事实核验
- 品牌资产采集顺序
- 模糊需求 fallback
- 早期假设 / placeholder / 中途回看
- 设计评审标准化

而不是先把 Skill 扩成包含视频、音效、巨量 showcase 的大包。

## 13. 资源规划

建议资源结构：

- `skills/cc-design/SKILL.md`
  - 触发范围、工作流、硬约束、资源导航
- `skills/cc-design/agents/openai.yaml`
  - 平台展示信息
- `skills/cc-design/references/question-protocol.md`
  - 需求澄清问题模板
- `skills/cc-design/references/design-context.md`
  - 设计上下文采集顺序与 fallback
- `skills/cc-design/references/brand-asset-protocol.md`
  - 具体品牌 / 产品任务下的事实核验与资产采集协议
- `skills/cc-design/references/junior-designer-workflow.md`
  - 分阶段展示、假设说明与中途回看
- `skills/cc-design/references/design-direction-advisor.md`
  - 需求模糊时的 3 方向顾问模式
- `skills/cc-design/references/design-review-guide.md`
  - 5 维度设计评审与修复清单
- `skills/cc-design/references/design-excellence.md`
  - 设计判断前置清单
- `skills/cc-design/references/frontend-design.md`
  - 无设计系统时的视觉基线
- `skills/cc-design/references/design-patterns.md`
  - 常见页面 / 版式模式库
- `skills/cc-design/references/react-babel-setup.md`
  - React + Babel 原型约束
- `skills/cc-design/references/starter-components.md`
  - 模板脚手架地图
- `skills/cc-design/references/tweaks-system.md`
  - 方案切换与 tweak 面板
- `skills/cc-design/references/interactive-prototype.md`
  - 交互原型导航 / 状态模式
- `skills/cc-design/references/platform-tools.md`
  - 预览、截图、导出路径
- `skills/cc-design/references/verification-protocol.md`
  - 结构 / 视觉校验流程
- `skills/cc-design/references/brand-style-loader.md`
  - 品牌风格研究与 getdesign 路由
- `skills/cc-design/references/design-system-creation.md`
  - 新建设计系统时的 token 结构
- `skills/cc-design/references/case-studies/*`
  - 典型页面、移动端、演示稿案例
- `skills/cc-design/assets/templates/*`
  - deck stage、design canvas、device frame、browser window、animation stage
- `skills/cc-design/scripts/gen_pptx.js`
  - HTML -> PPTX 导出
- `skills/cc-design/scripts/open_for_print.js`
  - HTML -> PDF 导出
- `skills/cc-design/scripts/super_inline_html.js`
  - 打包成单文件 HTML
- `skills/cc-design/scripts/lib/parse_args.js`
  - 脚本参数解析工具
- `skills/cc-design/scripts/package.json`
  - 最小 Node 依赖

## 14. V1 关键约束

1. 不把这个 Skill 做成泛化前端工程助手
2. 不在已有设计系统时无视上下文另起炉灶
3. 必须保留模板脚手架和导出脚本，而不是只写概念文档
4. 必须把验证流程写进运行层，而不是默认“用户自己看”
5. 必须明确 HTML 是核心交付媒介，Figma 等不在 V1 主闭环内

## 15. 第二轮增强方向

参考 `huashu-design` 后，`cc-design` 最值得加强的地方主要有 5 类：

### 15.1 流程层

- 把“先问清楚”升级为“一次性批量澄清 design context + variations + tweaks + 输出格式”
- 把“直接开写”升级为“assumptions + placeholders + early reveal + mid-review”
- 把“模糊需求直接硬做”升级为“先给 3 个方向，再让用户选”

### 15.2 约束层

- 增加品牌 / 产品任务下的事实验证约束
- 增加 logo / 产品图 / UI 截图优先于纯色值抽象的资产协议
- 增加 prototype 的点击验证和核心路径检查
- 增加 review 模式的评分维度与 quick wins 结构

### 15.3 案例层

- 现有 case study 够用，但缺少“如何把案例变成方向提案”的路由
- 不必一次性引入大型 showcase 资产库，先通过方向矩阵 + 现有案例入口解决

### 15.4 提示词与触发层

- `description` 需要覆盖“风格推荐 / 方向顾问 / 设计评审”触发词
- `default_prompt` 需要更明确地鼓励“先出 3 个方向，缺上下文时先做方向建议”

### 15.5 暂不引入的内容

以下能力有价值，但暂不建议直接并入 `cc-design`：

- 音频设计规则
- BGM / SFX 资产库
- 视频导出整链路
- 大体量 demo / showcase 目录

原因不是它们不强，而是它们会显著扩大 skill 体积与边界，更适合后续拆成 motion / export 方向的独立补充能力。

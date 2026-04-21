---
name: cc-design
description: "High-fidelity HTML design and prototype skill for landing pages, slide decks, mobile mockups, interactive prototypes, dashboard explorations, design-direction advising, and design review work. Use when Codex needs to design a screen, make an interface look polished, explore multiple visual directions, recommend a style direction before building, adapt an existing brand style, critique a design, or deliver a reviewable HTML-based visual artifact. Also use when the user mentions presentations, design systems, wireframes, UI mockups, motion studies, design philosophy, style selection, or asks to 'make it look good'. Do not trigger for pure content strategy, pure writing, or bitmap image generation alone."
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/cc-design"}}
---

# CC Design

## Overview

这个 Skill 只处理一类任务：

- 把视觉需求做成可预览、可截图、可迭代的 HTML 设计产物

它覆盖的是：

- 落地页
- 演示稿 / slide deck
- dashboard / UI mockup
- 移动端 screen / onboarding
- 可点击交互原型
- 视觉方向探索与对比

它不处理：

- 纯文案策划
- 纯内容写作
- 纯图片生成
- Figma 文件生产

如果用户真正缺的是内容策略、文章、脚本或图片素材，不要在这里偷偷扩 scope。

## Quick Start

1. 先判断输出类型：landing page、deck、mobile mockup、prototype，还是视觉探索。
2. 先看项目里有没有现成设计系统、token、组件、品牌文档或现有页面。
3. 再决定加载哪些 references，必要时复制 `assets/templates/` 下的模板。
4. 写 HTML 之前，先明确视觉焦点、情绪基调、层级和留白策略。
5. 完成后默认做结构检查和截图检查；需要导出时再调用脚本。

## Routing Guide

| 任务类型 | 先读什么 | 可复用模板 | 重点检查 |
|---|---|---|---|
| 任意设计任务 | `references/design-excellence.md` | - | 视觉层级是否成立 |
| 任务模糊 / 需要先选风格 | `references/design-direction-advisor.md` | `assets/templates/design_canvas.jsx` 可选 | 3 个方向是否真的不同 |
| 需要设计评审 | `references/design-review-guide.md` | - | 反馈是否可执行 |
| 没有现成设计系统 | `references/frontend-design.md` | 按场景选择 | 是否落入通用 AI 风 |
| 有现成设计系统 / 代码 / 品牌资产 | `references/design-context.md` | 按场景选择 | 是否真的复用了上下文 |
| 具体品牌 / 产品任务 | `references/brand-asset-protocol.md` + `references/brand-style-loader.md` | 按场景选择 | 事实和资产是否核实 |
| 品牌风格克隆 | `references/brand-style-loader.md` | 按场景选择 | 品牌气质是否对味 |
| Landing page / 产品页 | `references/design-patterns.md` | `assets/templates/browser_window.jsx` 可选 | 响应式与首屏层级 |
| Slide deck | `references/starter-components.md` | `assets/templates/deck_stage.js` | 固定画布缩放与翻页 |
| 多方案探索 | `references/tweaks-system.md` | `assets/templates/design_canvas.jsx` | 方案切换是否清晰 |
| Mobile mockup | `references/starter-components.md` + `references/interactive-prototype.md` | `assets/templates/ios_frame.jsx` / `android_frame.jsx` | 安全区、触达区、设备框 |
| Interactive prototype | `references/interactive-prototype.md` + `references/react-babel-setup.md` | 按场景选择 | 导航、状态、交互是否成立 |
| 动画 / motion study | `references/starter-components.md` + `references/react-babel-setup.md` | `assets/templates/animations.jsx` | 时间轴和播放状态 |
| 设计系统 / token 体系 | `references/design-system-creation.md` | - | token 是否完整且被真正使用 |
| 需要导出 | `references/platform-tools.md` | - | 文件是否实际生成 |

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输出语言：中文说明
- 核心交付：HTML 文件
- 默认优先复用现有设计上下文，而不是凭空发明新风格
- 如果任务提到真实品牌或产品，默认先核实事实与资产，再设计
- 如果没有设计系统，先用可控 token 和字体组合建立视觉基线
- 如果需求模糊，默认先提 3 个方向而不是直接拍板
- 默认至少提供 2-3 个方向中的一个可比较入口，或通过 tweaks 暴露变化
- 交付前默认检查 console、结构和截图
- 需要导出时，优先导出 PDF / PPTX / 单文件 HTML，而不是口头说“可以导出”

## Workflow

### Step 0: Verify Facts for Real-World Entities

如果任务里出现了具体品牌、产品、公司或已命名服务：

- 先核实它是否存在、是否已发布、当前形态是什么
- 先找 logo、产品图、UI 截图或官方资产
- 不要直接凭印象写“像某某品牌”

需要时读 [references/brand-asset-protocol.md](references/brand-asset-protocol.md)。

### Step 1: Scope the Request

至少先弄清：

- 最终产物是什么
- 几屏 / 几页 / 几个方向
- 保真度要到什么程度
- 有没有现成品牌或参考对象
- 是否需要导出
- 是先做方向建议，还是直接做成品

如果信息不够，读 [references/question-protocol.md](references/question-protocol.md)。

### Step 2: Acquire Design Context

开始做之前，先主动搜：

- 现有 HTML / CSS / 组件
- token 文件 / 设计系统说明
- 已上线页面
- 品牌文案或视觉参考

已有系统时，优先复用它的颜色、字体、间距、圆角、阴影和组件语言。

如果上下文很少，先读 [references/design-context.md](references/design-context.md)。

### Step 3: Lock the Visual Intent

写代码之前，先用 [references/design-excellence.md](references/design-excellence.md) 的思路回答这些问题：

- 这一屏最重要的视觉焦点是什么
- 目标情绪更偏信任、兴奋、专业还是创意
- 层级如何建立
- 留白和节奏如何组织
- 颜色和字体如何配合
- 是否需要多个方向并列比较

如果没有设计系统，再读 [references/frontend-design.md](references/frontend-design.md)。

如果用户还没能决定方向，不要硬做，先读 [references/design-direction-advisor.md](references/design-direction-advisor.md)。

### Step 4: Work Like a Junior Designer, Not a Black Box

开始实现时，不要直接闷头做完整稿。

优先做：

- 一版 assumptions + placeholder
- 一次早期展示
- 用户确认后的主版本推进
- 中途再展示一次
- 最后才做 polish

需要更细流程时，读 [references/junior-designer-workflow.md](references/junior-designer-workflow.md)。

### Step 5: Build with the Right Level of Structure

按场景选择最省力的方式：

- deck 用 `assets/templates/deck_stage.js`
- 多方案对比用 `assets/templates/design_canvas.jsx`
- 手机稿用 `assets/templates/ios_frame.jsx` 或 `android_frame.jsx`
- 浏览器场景用 `assets/templates/browser_window.jsx`
- 桌面工具窗口用 `assets/templates/macos_window.jsx`
- 动画场景用 `assets/templates/animations.jsx`

如果要写 React 内联原型，读 [references/react-babel-setup.md](references/react-babel-setup.md)。

### Step 6: Add Variation without File Explosion

如果用户要多个方向，不要默认拆成一堆 HTML。

优先：

- 用 `design_canvas` 并列展示
- 用 tweaks 面板切换颜色、排版、布局、文案层级

需要时读 [references/tweaks-system.md](references/tweaks-system.md)。

### Step 7: Verify Before Delivery

完成后必须做验证，不要“写完即交”。

默认检查：

- 有没有 console error / 关键 warning
- 主要结构有没有渲染出来
- 截图里层级、留白、对比和对齐是否成立
- slide / prototype 的导航和缩放有没有坏掉

详细流程见 [references/verification-protocol.md](references/verification-protocol.md)。

### Step 8: Review When Asked, Export When Needed

如果用户要求 review、比较多个方向、或交付前做专家审查：

- 从方向匹配、层级、做工、功能性、辨识度 5 个维度看
- 给出可执行问题，不要只说“还差点意思”
- 最后附 `Quick Wins`

需要时读 [references/design-review-guide.md](references/design-review-guide.md)。

如果用户需要导出，再读 [references/platform-tools.md](references/platform-tools.md) 并调用脚本：

- `node skills/cc-design/scripts/gen_pptx.js`
- `node skills/cc-design/scripts/open_for_print.js`
- `node skills/cc-design/scripts/super_inline_html.js`

## Hard Rules

Do not:

- 在已有设计系统时无视上下文另起炉灶
- 在真实品牌 / 产品任务里跳过事实核验和资产采集
- 把视觉任务做成普通模板页
- 在需求模糊时直接默认一个 generic 方向
- 用一堆花哨效果掩盖信息层级问题
- 明明需要多方向，却只给一个含糊方案
- 没截图、没检查就直接交付
- 把图片生成需求硬塞进 HTML 设计流程

Always:

- 先明确输出类型和约束
- 先搜上下文，再设计
- 具体品牌任务先核实事实与资产
- 先做视觉判断，再写代码
- 在大任务里先给 assumptions / placeholder，再继续
- 需要模板时优先复用模板
- 交付前至少做一轮结构检查和截图检查
- 诚实说明哪些导出 / 预览环节已验证，哪些还没验证

## Resource Map

- [references/question-protocol.md](references/question-protocol.md)
  - 范围不清时，用这个收口需求。
- [references/design-context.md](references/design-context.md)
  - 现有系统、代码、截图和品牌上下文的采集顺序。
- [references/brand-asset-protocol.md](references/brand-asset-protocol.md)
  - 具体品牌 / 产品任务的事实核验与资产协议。
- [references/junior-designer-workflow.md](references/junior-designer-workflow.md)
  - 假设、placeholder、中途回看和分阶段推进。
- [references/design-direction-advisor.md](references/design-direction-advisor.md)
  - 需求模糊时先给 3 个方向。
- [references/design-excellence.md](references/design-excellence.md)
  - 写代码前先做视觉判断。
- [references/frontend-design.md](references/frontend-design.md)
  - 没有设计系统时，用这个建立视觉基线。
- [references/design-patterns.md](references/design-patterns.md)
  - 常见 landing page / 内容区块 / 布局模式。
- [references/design-system-creation.md](references/design-system-creation.md)
  - 需要从零搭 token 和组件基线时，用这个。
- [references/brand-style-loader.md](references/brand-style-loader.md)
  - 用户点名品牌风格时，走这个研究路径。
- [references/interactive-prototype.md](references/interactive-prototype.md)
  - 交互原型的导航、状态与过渡。
- [references/react-babel-setup.md](references/react-babel-setup.md)
  - React + Babel 内联原型约束。
- [references/starter-components.md](references/starter-components.md)
  - 所有模板脚手架的用途和接入方式。
- [references/tweaks-system.md](references/tweaks-system.md)
  - 多方向切换与 tweak 面板。
- [references/platform-tools.md](references/platform-tools.md)
  - 预览、截图、导出路径。
- [references/verification-protocol.md](references/verification-protocol.md)
  - 结构 / 视觉验证流程。
- [references/design-review-guide.md](references/design-review-guide.md)
  - 设计 review 的 5 维度和 quick wins 输出。
- [references/case-studies/README.md](references/case-studies/README.md)
  - 典型案例入口。
- [assets/templates/deck_stage.js](assets/templates/deck_stage.js)
  - 演示稿固定画布与翻页容器。
- [assets/templates/design_canvas.jsx](assets/templates/design_canvas.jsx)
  - 多方案并排画布。
- [assets/templates/ios_frame.jsx](assets/templates/ios_frame.jsx)
  - iPhone 设备框。
- [assets/templates/android_frame.jsx](assets/templates/android_frame.jsx)
  - Android 设备框。
- [assets/templates/browser_window.jsx](assets/templates/browser_window.jsx)
  - 浏览器窗口壳。
- [assets/templates/macos_window.jsx](assets/templates/macos_window.jsx)
  - macOS 桌面窗口壳。
- [assets/templates/animations.jsx](assets/templates/animations.jsx)
  - 动画时间轴引擎。
- [scripts/gen_pptx.js](scripts/gen_pptx.js)
  - HTML -> PPTX。
- [scripts/open_for_print.js](scripts/open_for_print.js)
  - HTML -> PDF。
- [scripts/super_inline_html.js](scripts/super_inline_html.js)
  - 打包单文件 HTML。

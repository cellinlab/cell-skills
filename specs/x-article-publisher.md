# X Articles 发布 Skill 设计文档

## 1. 目标概述

这个 Skill 用于把现成的 Markdown 长文发布到 X (Twitter) Articles 编辑器，并把整个过程收敛成一条稳定、可重复的发布工作流。

它解决的不是“帮用户写一篇适合 X 的内容”，而是帮助用户完成下面这些更具体的动作：

- 解析 Markdown，提取标题、封面图、正文图片、分割线与可粘贴 HTML
- 支持从 frontmatter 读取标题 / 封面，并在需要时把 HTTPS 远程图片落到本地临时文件
- 为 X Articles 编辑器准备富文本与图片插入所需的中间数据
- 通过浏览器自动化工具把内容送进 X Articles 编辑器
- 默认只保存草稿，不自动发布
- 在浏览器自动化开始前，优先把本机浏览器里的 X/Twitter 登录 cookies 同步给 Playwright，减少手动登录
- 默认把 storage state 持久化到用户 cache 目录，并优先复用有效 cache，而不是每次重新导出

这个 Skill 的价值在于把“Markdown -> X Articles 草稿”这条链路做稳，而不是扩成 X 内容策略或写作 Skill。

## 2. 设计来源

这个 Skill 主要参考 `wshuyi/x-article-publisher-skill` 的实现思路，也参考 `JimLiu/baoyu-skills` 里的 `baoyu-post-to-x` 在 frontmatter、远程图片和发布稳定性处理上的做法，但会做更适合 Cell 仓库的改造。

保留的部分：

- 先解析 Markdown，再驱动浏览器自动化
- 使用中间结构数据保存标题、图片位置、HTML 正文
- 通过剪贴板保留富文本格式
- 只保存草稿，不自动发布
- 图片按 block index 反向插入，减少位置偏移

改造的部分：

- 先按本仓库规范补 `specs/`，再落 `skills/`
- 把“cookie 同步到 Playwright”作为正式能力，而不是临时 workaround
- 增加 browser-cookie3 -> Playwright storage state 的脚本支持
- 把持久化 cache 和 `playwright-mcp --storage-state` 预加载作为默认建议路径
- 明确和 `x-content-mentor` 的边界：这个 Skill 负责发布，不负责选题和写作
- 运行层文档只保留执行规则，不保留上游来源叙述

## 3. 技能定位

它是一个“X Articles 发布 / 发布准备 / 登录态同步 / 发布排查” Skill。

它不是：

- X 内容策略 Skill
- Thread 写作 Skill
- X 增长诊断 Skill
- 自动爆文生成器

更准确地说，它处理的是“文章已经写好，如何稳定进入 X Articles 草稿”。

## 4. 与现有 Skill 的关系

- `x-content-mentor`
  - 负责 X 平台上的选题、写法、增长和账号诊断
- `deep-writer`
  - 负责长文的 Brief、结构和正文写作
- `wechat-draft-publisher`
  - 负责微信公众号草稿发布
- `x-article-publisher`
  - 负责 X Articles 草稿发布与登录态同步

理想顺序通常是：

1. 用写作或策略类 Skill 产出文章
2. 用 `x-article-publisher` 把现成 Markdown 送进 X Articles 草稿

## 5. 建议技能名

建议英文目录名：

`x-article-publisher`

建议展示名：

`X 长文发布`

## 6. 适用场景

这个 Skill 主要适用于：

- “把这篇 Markdown 发到 X Articles”
- “我已经有长文了，帮我发到 X 的长文编辑器”
- “Playwright 里没登录 X，帮我把本机浏览器 cookies 同步过去”
- “帮我补一个只做 X Articles 发布的 skill”

## 7. 非目标

V1 默认不解决以下问题：

- 直接帮用户写 X 长文
- 替用户决定文章是否值得发到 X
- 自动点击最终发布按钮
- 代替完整的浏览器登录流程管理所有账号体系
- 覆盖所有浏览器自动化框架的 cookies 注入方式

## 8. 核心用户问题

这个 Skill 需要稳定回答以下问题：

1. 一篇 Markdown 长文如何转换成适合 X Articles 的富文本输入？
2. 封面、正文图片、分割线在编辑器里该如何定位和插入？
3. 如何尽量避免 Playwright 打开后仍然处于未登录状态？
4. 什么情况下应该走 cookie 同步，什么情况下仍然需要人工登录？
5. 发布失败时，卡在解析、剪贴板、登录、还是浏览器自动化步骤？

## 9. 典型触发语句

- 把这篇文章发到 X Articles
- 帮我把 Markdown 发布到 X 长文
- 帮我同步 X 的 cookies 给 Playwright
- 这个 X Articles 发布脚本没登录，帮我修一下
- 给这个仓库补一个 X 长文发布 skill

## 10. 默认输入约定

### 10.1 必填输入

- 至少提供以下之一：
  - 一篇现成 Markdown 文章
  - 一个已经存在的 X Articles 发布项目

### 10.2 选填输入

- 标题覆盖值
- 是否允许表格转图片
- 是否允许 Mermaid 转图片
- 浏览器类型偏好（Chrome / Edge / Firefox）
- 当前报错信息

### 10.3 默认假设

如果用户没特别说明，默认：

- 输出解释用中文
- 目标平台是 X Articles 而不是普通 tweet/thread
- 文章正文已经存在
- 默认只保存草稿，不自动发布
- 优先尝试 cookie 同步，失败再回退到手动登录
- 如果运行环境不支持 cookie 注入，只保留 storage state 导出并提示下一步

## 11. 输出契约

### 11.1 成功发布

至少包含：

- 最终标题
- 封面状态
- 正文图片数量
- 草稿是否保存成功
- 是否使用了 cookie 同步

### 11.2 发布失败

至少包含：

- 失败发生在哪一步
- 关键报错信息
- 是否已经准备好 storage state / 中间文件
- 下一步需要人工补什么

### 11.3 仓库改造型任务

如果用户要补发布能力，而不是只跑一次发布，至少包含：

- 当前项目已有能力的复用判断
- 新增脚本职责
- cookie 同步与浏览器自动化的边界
- 已验证与未验证的部分

## 12. 方法论原则

### 12.1 先把 Markdown 解析成结构数据，再进浏览器

浏览器自动化阶段不应该临时思考文章结构。

### 12.2 登录态问题优先在浏览器启动前解决

如果 Playwright 上来就是未登录状态，后面的自动化基本都会失效。优先尝试 cookies 同步。

更稳的做法是：

- 先复用持久化 storage state cache
- 在创建 browser context 前就加载 storage state
- 只有 cache 失效时，才重新导出 cookies

### 12.3 cookie 同步是优先路径，不是唯一真理

browser-cookie3 能解决很多登录态问题，但不是所有环境都能直接注入到当前自动化工具里。做不到就诚实降级到手动登录。

### 12.4 默认只保存草稿

不替用户点击最终发布按钮，保持安全边界。

### 12.5 运行层只写执行规则

来源、上游、保留/改造关系只留在 spec，不进入 skill 实现层。

## 13. 资源规划

建议资源结构：

- `skills/x-article-publisher/SKILL.md`
  - 触发范围、工作流、硬约束、资源导航
- `skills/x-article-publisher/references/workflow.md`
  - Markdown 解析、浏览器自动化、图片/分割线插入顺序
- `skills/x-article-publisher/references/cookie-sync.md`
  - browser-cookie3、Playwright storage state、失败降级规则
- `skills/x-article-publisher/references/troubleshooting.md`
  - 登录失败、剪贴板失败、图片定位失败、Playwright 不可用等问题
- `skills/x-article-publisher/scripts/parse_markdown.py`
  - 解析 Markdown，支持 frontmatter、远程图片下载，输出标题、HTML、图片、分割线和 block index
- `skills/x-article-publisher/scripts/copy_to_clipboard.py`
  - HTML / 图片复制到系统剪贴板
- `skills/x-article-publisher/scripts/table_to_image.py`
  - 表格转图片
- `skills/x-article-publisher/scripts/export_x_cookies.py`
  - 从本机浏览器导出 X/Twitter cookies，并转成 Playwright storage state JSON
- `skills/x-article-publisher/requirements.txt`
  - 最小 Python 依赖

## 14. V1 关键约束

1. 不把这个 Skill 做成 X 写作策略总控
2. 不在没有现成文章时偷偷接手写作任务
3. 必须提供 cookie 同步脚本，而不是只在文档里提一句
4. 必须保留“cookie 失败 -> 手动登录”的降级路径
5. 必须默认只保存草稿，不自动发布

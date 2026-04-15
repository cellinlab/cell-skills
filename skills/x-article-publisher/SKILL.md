---
name: x-article-publisher
description: Publish existing Markdown articles to X (Twitter) Articles drafts with browser automation preparation, rich-text clipboard support, image/divider positioning, and cookie export for Playwright login reuse. Use when Codex needs to send a finished Markdown article to X Articles, prepare block-indexed publish data, troubleshoot X Articles draft publishing, or sync local X/Twitter cookies into Playwright storage state before automation. Do not trigger for X topic strategy, thread writing, or growth diagnosis.
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/x-article-publisher"}}
---

# X Article Publisher

## Overview

这个 Skill 只处理一件事：

- 把已经写好的 Markdown 长文送进 X Articles 草稿

它覆盖的是发布准备和发布执行链路，不是内容生产链路。也就是说，它处理：

- Markdown 解析
- 富文本 HTML 准备
- 封面图、正文图片、分割线定位
- 剪贴板复制
- Playwright 登录态准备
- 浏览器自动化发布与排查

它不处理：

- X 选题
- Thread 写作
- 增长诊断
- 内容改写

如果用户真正缺的是文章本身，而不是发布动作，不要在这里偷偷扩 scope。

## Quick Start

1. 先确认用户已经有一篇可发布的 Markdown 长文。
2. 发布前先跑解析脚本，拿到 title、HTML、封面图、正文图片和分割线位置。
3. 优先导出本机 X/Twitter cookies 给 Playwright，用已有登录态减少手动登录。
4. 默认只保存草稿，不自动发布。

当前 skill 目录内置的最小工具链：

```bash
pip install -r skills/x-article-publisher/requirements.txt

# 解析 Markdown
python3 skills/x-article-publisher/scripts/parse_markdown.py article.md

# 生成 HTML 并复制到剪贴板
python3 skills/x-article-publisher/scripts/parse_markdown.py article.md --save-html /tmp/x-article.html --output json
python3 skills/x-article-publisher/scripts/copy_to_clipboard.py html --file /tmp/x-article.html

# 导出或复用 X/Twitter cookies 缓存
python3 skills/x-article-publisher/scripts/export_x_cookies.py

# 强制刷新缓存，或从其他浏览器读取
python3 skills/x-article-publisher/scripts/export_x_cookies.py --no-cache --browser edge
```

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输入通常是现成 Markdown 文件
- `title`、`cover_image` 等 frontmatter 可以直接作为解析输入
- 目标平台是 X Articles，不是普通 tweet / thread
- 默认只保存草稿，不自动发布
- 默认优先尝试 cookie 同步，再回退到人工登录
- 默认把 storage state 持久化到 `~/.cache/x-article-publisher/x-storage-state.json`
- 默认优先复用有效缓存，而不是每次重新扫描 Chrome cookies
- 如果运行环境没有浏览器自动化能力，就先把中间文件和 cookies 准备好，不假装已经发布成功
- 表格和 Mermaid 如需稳定呈现，应先转成图片再进入发布流程

## Workflow

### Step 1: Scope the Request

先判断当前请求属于哪一类：

- 已有 Markdown，要发到 X Articles
- 发布流程报错，需要排查
- 仓库里还没有 X Articles 发布能力，需要补一个 publish-only 流程

如果用户没有现成文章，或者其实在问“X 上该写什么”，切给更合适的 Skill。

### Step 2: Parse Before Browsing

先跑解析脚本，不要先打开浏览器：

- 提取标题
- 读取 frontmatter 里的标题 / 封面覆盖值
- 在必要时把 HTTPS 远程图片下载到本地临时目录
- 没有显式封面时，识别第一张图作为封面
- 提取正文图片及 `block_index`
- 提取分割线及 `block_index`
- 生成可粘贴 HTML

只有解析结果完整，才进入浏览器自动化。

需要详细步骤时，读 [references/workflow.md](references/workflow.md)。

### Step 3: Prefer Cookie Sync First

在打开 X Articles 编辑器之前，优先尝试 cookie 同步：

- 从本机浏览器导出 `x.com` / `twitter.com` cookies
- 转成 Playwright storage state JSON
- 默认先检查持久化 cache 是否仍然有效
- 如果当前宿主支持 storage state / cookie 注入，在创建 browser context 前优先加载
- 如果宿主不支持，或注入后仍未登录，再回退到人工登录

不要默认让用户每次都手动登录。

需要具体规则时，读 [references/cookie-sync.md](references/cookie-sync.md)。

### Step 4: Publish in the Stable Order

发布顺序不要乱：

1. 打开 X Articles 编辑器或文章列表页
2. 先探测当前 browser context 是否已经登录
3. 如果未登录，优先重建为带 `storage_state` 的 context，而不是先硬导航到编辑器
4. 如果落在列表页，先点 `Create` / `Write`
5. 上传封面图
6. 填标题
7. 通过剪贴板粘贴 HTML 正文
8. 按 `block_index` 反向插入正文图片
9. 按 `block_index` 反向插入分割线
10. 保存草稿

这里最重要的是两点：

- 先文后图后分割线
- 图片和分割线按高索引到低索引插入，避免位置偏移

### Step 5: Report the Result

成功时至少报告：

- 最终标题
- 封面状态
- 正文图片数量
- 分割线数量
- 是否保存成草稿
- cookie 是否同步成功

失败时至少报告：

- 卡在哪一步
- 关键报错
- 是否已经生成 HTML / storage state 等中间文件
- 还需要用户补什么

## Hard Rules

Do not:

- 在这个 Skill 里代替用户写长文
- 自动点击最终发布按钮
- 跳过 Markdown 解析直接硬做浏览器操作
- 明明能做 cookie 同步却每次都让用户手动登录
- 发现宿主不支持 cookie 注入时还假装“已经同步成功”

Always:

- 先解析 Markdown，再进浏览器
- 优先尝试 cookie 同步
- 默认只保存草稿
- 把 block index 当作图片/分割线定位依据
- 诚实说明当前运行环境能不能真正把 cookies 注入到 Playwright

## Resource Map

- [references/workflow.md](references/workflow.md)
  - 读这个文件，拿 Markdown 解析、浏览器自动化、图片和分割线插入顺序。
- [references/cookie-sync.md](references/cookie-sync.md)
  - 读这个文件，拿 browser-cookie3、Playwright storage state 和登录降级规则。
- [references/troubleshooting.md](references/troubleshooting.md)
  - 读这个文件，排查登录、剪贴板、图片定位、Playwright 工具不可用等问题。
- [scripts/parse_markdown.py](scripts/parse_markdown.py)
  - 解析 Markdown，输出标题、HTML、图片、分割线和 block index。
- [scripts/copy_to_clipboard.py](scripts/copy_to_clipboard.py)
  - 把 HTML 或图片复制到系统剪贴板。
- [scripts/table_to_image.py](scripts/table_to_image.py)
  - 把 Markdown 表格转成 PNG。
- [scripts/export_x_cookies.py](scripts/export_x_cookies.py)
  - 从本机浏览器导出 X/Twitter cookies，并转成 Playwright storage state JSON。

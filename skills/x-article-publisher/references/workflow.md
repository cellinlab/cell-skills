# Workflow

这个 workflow 只服务“把现成 Markdown 发到 X Articles 草稿”。

## 1. 先解析 Markdown

先运行：

```bash
python3 skills/x-article-publisher/scripts/parse_markdown.py article.md
```

目标是拿到这些结构数据：

- `title`
- `cover_image`
- `content_images`
- `dividers`
- `html`
- `total_blocks`
- `dividers[].editor_block_index`
- `cover_source`

不要在没拿到这些中间数据之前就开始浏览器自动化。

当前解析器还支持两类常见输入：

- frontmatter 里的 `title` / `cover_image` / `cover`
- HTTPS 远程图片，会先下载到本地临时目录再交给后续流程

## 2. 预处理需要转图片的内容

如果文章里有表格或 Mermaid，优先先转图片：

- 表格：`table_to_image.py`
- Mermaid：优先用 `mmdc`

原因很简单：

- X Articles 对表格和复杂图形支持不稳定
- 先转图片更可控

## 3. 浏览器执行顺序

稳定顺序如下：

1. 先确认可复用的 storage state cache 是否存在且有效
2. 用带 `storage_state` 的 browser context 启动浏览器
3. 先打开 `https://x.com/home` 探测当前 context 是否已登录
4. 再打开 X Articles 编辑器或文章列表页
5. 如果当前是列表页，先点 `Create` / `Write`
6. 上传封面
7. 填标题
8. 粘贴 HTML 正文
9. 反向插入正文图片
10. 反向插入分割线（路径：插入 → 分割线）
11. 保存草稿

如果迟迟看不到编辑器，要先怀疑两件事：

- 当前账号没有 X Articles 能力
- 实际落在的是文章列表页，还没点创建按钮

不要把顺序写反成：

1. 先开一个未登录 context
2. 直接导航到编辑器
3. 再尝试补注入 cookies

这种顺序很容易让首个请求直接落到登录页，然后后续状态变得混乱。

## 4. 先文后图后分割线

正文应先整体进入编辑器。

然后再做两种补充插入：

- 正文图片
- 分割线

如果先插图再粘正文，位置很容易错。

## 5. 分割线入口

工具栏上有两个下拉，不要混淆：

- 「正文」块类型下拉：只有标题 / 副标题 / 正文，没有分割线。
- 「插入」下拉：按钮 `aria-label="添加媒体内容"`，文字标为「插入」。这里包含 6 项：媒体 / GIF / 帖子 / 分割线 / 代码 / LaTeX。

分割线只能从「插入」下拉进入：

1. 用 Playwright 的真点击打开「插入」下拉。
2. 选择文字精确等于「分割线」的 `[role="menuitem"]`。
3. 插入成功后，编辑器里会新增一个 `<div role="separator">` 块。

不要从「正文」块类型下拉里找分割线；那里没有。

## 6. 为什么用 block index

图片和分割线都要先参考解析结果定位，但口径要分清：

- `total_blocks` 不含分割线，等于纯文本粘贴后编辑器里的块数。
- `dividers[].block_index` 是最终文档里的位置，包含已经出现过的分割线。
- `dividers[].editor_block_index` 是纯文本粘贴后编辑器里的定位索引，可直接用于浏览器步骤。

分割线实操时优先用每条 `after_text` 的前 15 个字，在编辑器 `[data-block="true"]` 块中精确匹配目标位置。这比手动做 `block_index - prior_divider_count` 更稳，也避免重复换算。

如果必须用索引，优先用 `editor_block_index`，不要重新推导。

## 7. 为什么反向插入

图片和分割线按从大到小的索引插入。

这样做的原因：

- 先插靠后的元素，不会影响靠前元素的位置
- 可以减少多次插入造成的索引漂移

## 8. 反向插入分割线

对每个分割线，按 `block_index` 从大到小执行：

1. 用每条分割线 `after_text` 的前 15 个字，在编辑器 `[data-block="true"]` 块里精确匹配目标块。
2. 用 Selection API 把光标定位到目标 H2 前一段 `[data-block="true"]` 的末尾文本节点。
3. 用 Playwright 的 `browser_click(ref)` 真点击「插入」下拉；不要用 JS `button.click()`。
4. 选择文字精确等于「分割线」的 `[role="menuitem"]`。
5. 等 1 秒，确认 `[role="separator"]` 数量增加 1，再处理下一条。

如果目标是“在 H2 前插分割线”，光标应落在这个 H2 前一段的末尾。插入后得到的 separator 应位于该 H2 前一格。

## 9. 草稿边界

默认只保存草稿。

不要替用户自动点击最终发布按钮。

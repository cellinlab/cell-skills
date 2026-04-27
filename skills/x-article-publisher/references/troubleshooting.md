# Troubleshooting

## 1. Playwright 打开后还是未登录

先区分两件事：

- cookies 有没有成功导出
- storage state 有没有被当前宿主真正加载

先跑：

```bash
python3 skills/x-article-publisher/scripts/export_x_cookies.py
```

如果导出成功但 Playwright 仍未登录，问题通常在“注入”而不是“导出”。

如果确认已经登录但仍然进不了文章编辑器，再检查账号本身是否有 X Articles 能力。

如果当前宿主支持 `--storage-state`，优先排查：

- browser context 是不是在启动前就加载了 cache
- 是不是先开了未登录 context 再去导航

这两类问题通常比 cookies 导出本身更常见。

## 2. 打开的是文章列表页，不是编辑器

这通常不是脚本坏了，而是页面先落在草稿列表。

先检查：

- 页面里有没有 `Create` 或 `Write` 按钮
- 点击后标题输入框是否出现

不要在还没点创建入口时，就把“看不到标题框”判断成选择器失败。

## 3. cache 明明存在，但还是重复导出

先检查：

- cache 文件是不是在 `~/.cache/x-article-publisher/x-storage-state.json`
- `auth_token` 和 `ct0` 是否仍在 cache 中
- cache 文件修改时间有没有超过默认的 12 小时

如果就是要强制刷新，显式跑：

```bash
python3 skills/x-article-publisher/scripts/export_x_cookies.py --no-cache
```

## 4. 图片位置不对

先检查：

- `parse_markdown.py` 输出里的 `block_index`
- 浏览器里是否按从大到小顺序插入

不要回退到模糊的文字匹配。

## 5. 远程图片上传失败

如果 Markdown 里用的是 `https://...` 图片：

- 先确认 `parse_markdown.py` 有没有把它下载到本地临时目录
- 再确认临时文件是否还存在

X Articles 上传阶段需要的是本地文件，不是远程 URL。

## 6. 表格显示异常

优先把表格转图片，再插入 X Articles。

## 7. 粘贴后格式丢失

通常是：

- 没有把 HTML 作为富文本放进剪贴板
- 用了纯文本粘贴而不是正常粘贴

先确认 `copy_to_clipboard.py html` 成功执行。

## 8. Playwright 工具不可用

如果宿主里没有可用的浏览器自动化工具：

- 先完成 Markdown 解析
- 先准备 HTML 和 storage state
- 明确告诉用户“浏览器自动化这一步当前环境不能执行”

不要假装已经保存成草稿。

## 9. 分割线插入失败

先确认入口是否找对：分割线在「插入」下拉里，不在「正文」块类型下拉里。

已知坑：

- `---` Markdown shortcut 不会在 X Articles 里自动转成 HR，别试。
- 粘贴 `<hr>` HTML 会被剥离，别试。
- JS-only 的 `composer.focus()` + `Meta+v` 看似有效但不触发 autosave：DOM 上可能有完整块，刷新页面后正文为空。必须用 Playwright 的 `browser_click(ref)` 真点编辑器，再 `Meta+v`，再等 3-5 秒，看草稿列表预览出现首句话才算成功。
- 「插入」按钮只能用真点击。JS `button.click()` 在这个按钮上会触发文件选择器，而不是弹出菜单。
- `parse_markdown.py` 下载远程封面图到 `/var/folders/.../x-article-publisher-images/...` 时，这条路径不在 Playwright MCP allowed roots 内。先 `cp` 到 `/Users/cell/.playwright-mcp/<name>.jpg` 再上传。
- 剪贴板可能被外部覆盖。`copy_to_clipboard.py` 和 `Meta+v` 之间如果隔了用户操作或别的进程，可能粘到错的内容。粘完立刻校验首段是否匹配；不匹配就重新 copy 再粘。

插入后用 `[role="separator"]` 计数校验，数量必须等于 Markdown 里的 `---` 数量，并且每个 separator 都在对应 H2 前一格。

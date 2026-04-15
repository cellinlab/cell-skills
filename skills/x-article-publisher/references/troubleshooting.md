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

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
10. 反向插入分割线
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

## 5. 为什么用 block index

图片和分割线都用 `block_index` 定位。

不要依赖“前后文字匹配”，因为：

- 段落可能重复
- 短句不够唯一
- 粘贴后文本结构可能发生微小变化

更稳的方式是：

- 先统计块元素顺序
- 再用 `block_index` 定位

## 6. 为什么反向插入

图片和分割线按从大到小的索引插入。

这样做的原因：

- 先插靠后的元素，不会影响靠前元素的位置
- 可以减少多次插入造成的索引漂移

## 7. 草稿边界

默认只保存草稿。

不要替用户自动点击最终发布按钮。

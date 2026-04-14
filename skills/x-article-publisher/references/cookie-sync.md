# Cookie Sync

这个文件只讲一件事：

- 如何优先把本机浏览器里的 X/Twitter 登录态同步给 Playwright

## 1. 为什么先做 cookie 同步

很多 X Articles 自动化失败，不是因为选择器不对，而是 Playwright 打开的是未登录上下文。

如果用户本机浏览器已经登录 X/Twitter，优先复用这份登录态，通常比重新手动登录更稳、更快。

## 2. 导出方式

运行：

```bash
python3 skills/x-article-publisher/scripts/export_x_cookies.py --output /tmp/x-storage-state.json
```

默认行为：

- 默认只从 Chrome 读取 cookies
- 只导出 `x.com` / `twitter.com` 及其子域 cookies
- 输出成 Playwright storage state JSON

如果你的登录态在其他浏览器里，再显式传：

```bash
python3 skills/x-article-publisher/scripts/export_x_cookies.py \
  --browser edge \
  --browser firefox \
  --output /tmp/x-storage-state.json
```

## 3. 成功后得到什么

输出文件是标准 Playwright storage state 格式，核心是：

- `cookies`
- `origins`

当前脚本只负责 cookies，不负责 localStorage。

对 X/Twitter 登录态来说，cookies 通常已经足够覆盖大多数场景。

## 4. 运行时如何使用

如果当前宿主支持在 Playwright 上下文创建前加载 storage state：

- 在创建 browser context 时直接使用导出的 JSON

典型方式是：

- `browser.new_context(storage_state="/tmp/x-storage-state.json")`
- 或 Playwright CLI / MCP 里等价的 storage state 注入入口

如果当前宿主只支持打开一个现成浏览器标签，但不支持 cookie 注入：

- 保留 storage state 文件
- 再回退到人工登录

不要把“导出了 storage state 文件”和“Playwright 已经成功登录”混为一谈。

## 5. 什么时候回退到人工登录

以下情况应直接回退：

- 没有找到任何 X/Twitter cookies
- 宿主浏览器自动化工具不支持导入 storage state
- 导入后仍然打开的是未登录页面

回退时要明确说清：

- cookies 是否导出成功
- 失败点是在“导出”还是“注入”

## 6. 安全边界

这个 Skill 只负责在本机导出和转换 cookies。

默认不要：

- 把 cookies 提交到仓库
- 把 storage state 长期保存在公开目录
- 在回复里直接展示敏感 cookie 值

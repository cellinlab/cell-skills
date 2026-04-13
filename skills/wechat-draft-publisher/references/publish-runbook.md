# Publish Runbook

这个 runbook 只服务“发布到微信公众号草稿箱”这件事。

目标是给出一条稳定、可迁移的最小发布闭环，而不是扩成完整公众号内容系统。

## 1. 先看仓库里有没有现成发布能力

进入新仓库后，优先搜这些模式：

```bash
rg -n "draft/add|uploadimg|add_material|access_token|publish" .
rg -n "wechat|publisher|converter|preview|media_id" .
rg --files | rg "config|wechat|theme|publisher|converter|cli"
```

先回答这几个问题：

- 已经有 CLI / script 吗
- 已经有 Markdown -> 微信 HTML 的 converter 吗
- 现有配置字段是什么名字
- 现有代码有没有 preview fallback

如果仓库已经有可用 publish 命令，优先复用，不要先重写。

## 2. 稳定发布闭环

实践里更稳的发布顺序通常是：

1. 读取配置，拿 `appid` / `secret` / `author`
2. 把 Markdown 转成微信能接受的 HTML
3. 获取 `access_token`
4. 上传正文里的本地图片，替换掉本地 `src`
5. 上传封面，得到 `thumb_media_id`
6. 调 `draft/add` 创建草稿
7. 成功后返回 `media_id`
8. 失败就降级到本地 preview

默认按下面这些原则实现：

- 对 token 做 cache
- 把正文图上传和封面上传分开处理
- 把 `errcode` / `errmsg` 原样保留到错误信息里
- 把“草稿创建成功”的判断收敛到 `media_id`

## 3. 发布前检查清单

### 配置检查

最低要求：

- `appid`
- `secret`

常见附加项：

- `author`
- `theme`
- `theme_color`

如果缺少真实发布配置：

- 不要伪造成功结果
- 直接走 preview fallback

### IP 白名单检查

公众号 API 常见阻塞点不是代码，而是出口 IP 没进白名单。

常用命令：

```bash
curl -s https://ifconfig.me
```

拿到公网 IP 后，引导用户去公众号后台开发配置里补上。

如果报错明显像白名单问题，不要盲目重试多次，先回到这里。

### 内容检查

实用上限建议如下：

- 标题：控制在微信可接受长度内
- 摘要：`<= 120 UTF-8 bytes`
- 单图：`<= 5MB`
- 正文图片：`<= 20`
- 正文必须没有本地图片路径残留

另外：

- 当前这条草稿发布链应视为“封面必填”
- 没封面时不要继续调 `draft/add`，直接转 preview fallback

## 4. 推荐的发布顺序

### 4.1 获取 token

接口：

```text
GET /cgi-bin/token
```

做法：

- 用 `appid + secret`
- 带缓存，通常留 5 分钟缓冲
- 拿不到 `access_token` 就终止发布

### 4.2 上传正文图

接口：

```text
POST /cgi-bin/media/uploadimg
```

用途：

- 只给正文内 `<img>` 使用
- 返回的是 URL，不是 `media_id`

处理规则：

- 只上传本地图片
- 远程 URL 可以跳过或保留
- 上传成功后立即替换 HTML 里的原始路径

### 4.3 上传封面

接口族：

```text
POST /cgi-bin/material/add_material
```

用途：

- 拿封面所需的 `thumb_media_id`

注意：

- 不同项目在 `type` 细节上可能不完全一致
- 所以如果当前项目已有稳定实现，不要轻易改它
- 如果是从零补链路，先保持与项目现有约定一致，再验证

### 4.4 创建草稿

接口：

```text
POST /cgi-bin/draft/add
```

最核心字段：

```json
{
  "articles": [
    {
      "title": "...",
      "author": "...",
      "digest": "...",
      "content": "...",
      "show_cover_pic": 0,
      "thumb_media_id": "..."
    }
  ]
}
```

判断成功的关键：

- 返回里有 `media_id`

错误处理的关键：

- 如果有 `errcode` 且不为 0，直接按失败处理
- 错误信息里保留 `errcode` 和 `errmsg`

## 5. Preview Fallback

这部分建议始终保留为降级链：

- 真实发布失败
- 没有配置凭据
- 白名单还没配
- 图片资源不完整，暂时不想阻塞内容确认

这几种情况都可以先生成本地 HTML preview。

对用户至少要说清：

- 预览文件路径
- 为什么这次没有真实发到草稿箱
- 真正补齐发布条件还差什么

## 6. 发布链路里最容易踩的坑

### 把“写作问题”误当“发布问题”

这个 Skill 不负责写文章。用户没给内容时，不要在这里偷偷进入写作模式。

### 本地图片没替换就进 draft/add

这是很常见的假成功来源。HTML 里如果还留着本地路径，微信端就会挂图。

### 没检查公网 IP 就一直重试

公众号 API 很多“明明代码没问题却一直失败”的情况，本质是白名单。

### 误把封面上传和正文图上传当成同一种接口

正文图要的是可放进正文里的 URL，封面要的是可放进草稿字段里的媒体标识。两者不要混。

### 没拿到 `media_id` 就宣称发布成功

成功条件要收敛，不要靠“接口没报异常”来猜。

## 7. 输出结果建议

发布成功时，输出至少包含：

- 标题
- 摘要
- `media_id`
- 封面是否已上传
- 需要用户去草稿箱继续检查 / 手动发布

发布失败时，输出至少包含：

- 失败步骤
- 核心报错
- 是否已生成 preview
- 下一步建议

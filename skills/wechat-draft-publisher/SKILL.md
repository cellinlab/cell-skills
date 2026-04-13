---
name: wechat-draft-publisher
description: 微信公众号草稿发布与发布故障排查 Skill，专门处理把现成 Markdown / 文章内容排版、检查并推送到微信公众号草稿箱。Use when Codex needs to publish existing content to WeChat Official Account drafts, troubleshoot AppID / AppSecret / API IP 白名单 / 图片上传 / 草稿创建问题, or add a publish-only workflow to a repo. Do not trigger for 选题、写作、SEO、配图创作、数据复盘。
metadata: {"openclaw":{"homepage":"https://github.com/cellinlab/cell-skills/tree/main/skills/wechat-draft-publisher"}}
---

# WeChat Draft Publisher

## Overview

这个 Skill 只处理一件事：

- 把已经写好的内容发到微信公众号草稿箱

它覆盖的是发布链路，不是内容生产链路。也就是说，它处理：

- 发布前检查
- Markdown / HTML 到微信可接受内容的落地
- 正文图片上传与替换
- 封面上传
- 草稿箱创建
- 发布失败后的预览降级与故障排查

它不处理：

- 选题
- 写作
- 改写
- SEO 补强
- 配图创作
- 数据复盘

如果用户真正缺的是文章本身，而不是发布动作，不要在这里偷偷扩 scope。

## Quick Start

1. 先判断用户是不是已经有可发布内容。
2. 优先复用当前仓库已有的 publisher / converter / CLI，不要先重写一套。
3. 发布前先做配置、白名单、素材和内容约束检查。
4. 能发就进草稿箱；发不了就给本地 preview 和明确卡点。

当前 skill 目录已经内置最小可执行工具链：

```bash
pip install -r skills/wechat-draft-publisher/requirements.txt
cp skills/wechat-draft-publisher/config.example.yaml skills/wechat-draft-publisher/config.yaml

# 本地预览
python3 skills/wechat-draft-publisher/toolkit/cli.py preview article.md

# 看当前公网 IP，去配微信白名单
python3 skills/wechat-draft-publisher/toolkit/cli.py show-ip

# 真实发布；缺凭据时默认降级为 preview
python3 skills/wechat-draft-publisher/toolkit/cli.py publish article.md --cover cover.png
```

## Default Contract

默认采用以下约定，除非用户另有说明：

- 输入通常是现成 Markdown、HTML，或仓库中已经存在的一篇文章
- 默认目标是“发到公众号草稿箱”，不是直接群发
- 默认不改写正文，只做发布所需的最小安全修正
- 默认会尽量保留现有排版系统、主题系统和 CLI 入口
- 如果仓库没有现成发布链路，先补最小可用发布路径，不顺手把写作链路也一起做了
- 如果缺少真实发布条件，降级为本地 HTML 预览，而不是假装已经发布成功

## Workflow

### Step 1: Scope the Request

先判断当前请求属于哪一类：

- 已有文章，要发布到草稿箱
- 已有发布链路，但现在发不出去，需要排查
- 仓库里还没有发布能力，需要补一个 publish-only 流程

如果用户没有现成内容，或者明确在要“写一篇公众号文章”，先交给更合适的写作 Skill，不要在这个 Skill 里硬写。

### Step 2: Inspect Before Touching

先看当前仓库有没有现成实现。优先搜索：

- `draft/add`
- `uploadimg`
- `add_material`
- `access_token`
- `publish`
- `wechat`
- `publisher`
- `converter`

重点判断四件事：

- 现有 CLI / 脚本 / SDK 能不能直接复用
- 配置文件在哪里，字段叫什么
- Markdown 是怎么转微信 HTML 的
- 失败时有没有 preview 降级链

只有在现有实现缺失或明显不够时，才补新代码。

需要具体搜索和落地顺序时，读 [references/publish-runbook.md](references/publish-runbook.md)。

### Step 3: Run Publish Preflight

发布前必须先过这组检查：

- 是否有现成内容文件
- 是否能拿到 `appid` 和 `secret`
- 当前出口公网 IP 是否已经加入微信 API IP 白名单
- 标题、摘要、图片、封面是否满足约束
- 本地图片路径是否真实存在

默认约束：

- 标题控制在微信可接受长度内
- 摘要不超过 120 UTF-8 bytes
- 正文图不超过 20 张
- 单张图片不超过 5MB
- 当前这条草稿发布链要求提供有效封面

如果缺少凭据或白名单未配好：

- 不要假装“已发布”
- 直接转入 preview 降级
- 明确告诉用户差的是什么

### Step 4: Publish in the Proven Order

发布顺序不要乱：

1. 获取 `access_token`
2. 上传正文内图片，并把本地 `src` 替换成微信返回 URL
3. 上传封面，拿到 `thumb_media_id`
4. 调用草稿接口创建 draft
5. 回传 `media_id`

这里最重要的是顺序和边界：

- 正文图和封面图不是同一种用途，不要混着传
- 本地图片路径必须在发布前全部处理掉
- 草稿创建成功的判断依据是拿到 `media_id`
- 请求失败时要原样保留 `errcode` / `errmsg`

### Step 5: Report the Result

成功时至少报告：

- 最终标题
- 摘要
- 是否带封面
- 发布得到的 `media_id`
- 提醒用户去公众号后台草稿箱检查并手动发布

失败时至少报告：

- 卡在哪一步
- 报错原文或关键 errcode
- 是否已经生成本地预览
- 接下来需要用户补什么

## Hard Rules

Do not:

- 在这个 Skill 里替用户补写整篇文章
- 因为用户说“发公众号”就偷偷加入选题、写作、配图生成
- 没有 `media_id` 还对外宣称“发布成功”
- 静默丢掉正文里的本地图片
- 没有检查白名单就反复重试 API
- 看到仓库里已有可用发布链路，却另起炉灶重写一套

Always:

- 先检查当前项目能不能复用已有实现
- 先做 preflight，再打 API
- 保留真实错误信息，尤其是微信接口返回值
- 缺真实发布条件时，明确降级到 preview
- 把“发布”和“写作”边界说清楚

## Resource Map

- [references/publish-runbook.md](references/publish-runbook.md)
  - 读这个文件，拿发布链路的搜索入口、内容约束、API 顺序、错误排查和降级策略。
- [config.example.yaml](config.example.yaml)
  - 复制成 `config.yaml` 后填写 `wechat.appid`、`wechat.secret`、`wechat.author`。
- [requirements.txt](requirements.txt)
  - 安装最小依赖：Markdown 转换、HTML 处理、YAML 配置、微信 API 请求。
- [toolkit/cli.py](toolkit/cli.py)
  - 提供 `preview`、`publish`、`show-ip` 三个可执行入口；`publish` 当前要求提供有效封面。

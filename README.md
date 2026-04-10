# Cell 细胞 公开 Skills 仓库

👋 大家好，这是 Cell 细胞 的公开 Skills 仓库。

这里会逐步整理并公开 Cell 细胞 在内容创作中经常使用的一批技能，包括提示词、工作流、结构化方法，以及一些适合和 AI 一起协作的创作套路。大部分内容都会开源，少部分如果依赖个人环境或仍在迭代中，可能暂时不会放出。

## 仓库结构

当前仓库主要分为两层：

- `skills/`
  - 已经实现的 Skills 本体，每个 Skill 都是一个独立目录，通常包含 `SKILL.md`、`agents/`、`references/`、`assets/`
- `specs/`
  - 对应 Skill 的设计文档，用来沉淀目标、边界、输入输出契约和实现思路

## 当前已完成的 Skills

目前已经整理并落地的 Skills 包括：

- `skills/opc-case-research`
  - 面向超级个体、创作者 IP、一人公司案例的系统化公开信息调研，重点关注内容策略、IP 定位、渠道与商业模式
- `skills/deep-writer`
  - 面向通用深度内容写作，支持主题驱动写作、草稿深化、以及访谈 / 播客 / 笔记等素材整理型写作
- `skills/book-material-miner`
  - 面向拆书与写作素材提炼，把书籍内容压缩成观点、故事、金句、素材块，以及可交给 `deep-writer` 继续深写的素材文章
- `skills/celf-style-writer`
  - 面向 Cell 细胞个人风格写作，适合文章写作、改写、增强与风格审查
- `skills/content-strategy-diagnosis`
  - 面向内容开写前的策略诊断，判断选题、形式、平台、材料密度与目标连接是否成立
- `skills/hook-optimizer`
  - 面向短内容开头优化，先诊断前几秒 / 前几句的问题，再给出多组可兑现的开头方案
- `skills/ai-writing-diagnosis`
  - 面向 AI 写作痕迹诊断，逐段指出文本里过度光滑、模板化或作者感不足的位置
- `skills/benchmark-filter`
  - 面向创作者 / OPC / 一人公司语境下的对标筛选，判断谁值得研究、值得学哪一层
- `skills/learning-builder`
  - 面向“学习-消化-输出”一体化的学习路径构建，把模糊学习目标转成可执行学习包（学习者画像、权威来源、阶段练习、里程碑与复盘）

## 这些 Skills 会覆盖什么

- 内容前置诊断与策略判断
- 内容选题与研究
- 对标筛选与案例研究
- 大纲设计与结构梳理
- 标题、摘要、开头、结尾等文案生成与优化
- 长文、短内容、脚本、口播稿等创作辅助
- 改写、润色、翻译、风格统一与 AI 痕迹诊断
- 发布前检查与内容优化

## 这个仓库的定位

它不是一个追求“大而全”的模板仓库，更像是我们 Cell 细胞 长期使用、持续打磨的一套创作技能集合。

如果你也在做内容创作，或者在搭建自己的 AI 工作流，希望把零散经验沉淀成可复用的能力，这个仓库也许会对你有帮助。

## 当前状态

这个仓库目前已经从“零散提示词整理”开始进入“按 Skill 目录组织”的阶段。

当前的整理方式是：

- 先在 `specs/` 中定义 Skill 设计文档
- 再在 `skills/` 中实现真正可复用的 Skill
- 逐步补齐 references、assets、agents 元信息和后续迭代

## 开源说明

这个仓库中的大部分 Skills 会以开源方式维护和更新，默认采用 [MIT License](./LICENSE)。

## 进度

目前仓库仍在持续整理中，后续会逐步补充：

- 更多内容创作相关 Skills
- 每个 Skill 更完整的说明
- 使用方式
- 示例内容
- 持续更新的版本迭代

## OpenClaw 安装

这个仓库当前已经可以被 OpenClaw 识别，但更推荐按下面两种方式安装：

### 方式一：把仓库作为共享 Skills 源

OpenClaw 支持把一个额外目录加入 `skills.load.extraDirs`。这个仓库可以直接指向仓库根目录，也可以直接指向里面的 `skills/` 目录。

示例：

```json
{
  "skills": {
    "load": {
      "extraDirs": [
        "/absolute/path/to/skills"
      ]
    }
  }
}
```

或：

```json
{
  "skills": {
    "load": {
      "extraDirs": [
        "/absolute/path/to/skills/skills"
      ]
    }
  }
}
```

更新配置后，新开一个 OpenClaw 会话，或重启 gateway，再用下面的命令确认是否加载成功：

```bash
openclaw skills list
```

### 方式二：只安装单个 Skill

如果你只想用某一个 Skill，直接把对应目录复制到你的 workspace `skills/` 下即可，例如：

```bash
cp -R ./skills/deep-writer /path/to/your-workspace/skills/
```

这种方式最直接，也最适合只挑一两个 Skill 使用的场景。

## ClawHub 支持

这个仓库现在已经按“一 Skill 一个目录”的方式组织，单个 Skill 目录可以直接作为 ClawHub 的发布单元。

目前更推荐两种使用方式：

### 1. 从 GitHub 导入单个 Skill

可以直接把某个 Skill 的 GitHub 路径丢给 ClawHub 的 GitHub Import，例如：

- `https://github.com/cellinlab/cell-skills/tree/main/skills/deep-writer`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/opc-case-research`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/celf-style-writer`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/book-material-miner`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/content-strategy-diagnosis`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/hook-optimizer`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/ai-writing-diagnosis`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/benchmark-filter`
- `https://github.com/cellinlab/cell-skills/tree/main/skills/learning-builder`

如果直接导入整个仓库，ClawHub 也能自动识别多个 `SKILL.md` 候选项，再让你选择其中一个。

### 1.1 已发布到 ClawHub 的新 Skill

- [内容策略诊断](https://clawhub.ai/cellinlab/cell-content-strategy-diagnosis)
- [开头优化](https://clawhub.ai/cellinlab/cell-hook-optimizer)
- [AI 写作诊断](https://clawhub.ai/cellinlab/cell-ai-writing-diagnosis)
- [对标筛选](https://clawhub.ai/cellinlab/cell-benchmark-filter)
- [学习路径构建](https://clawhub.ai/cellinlab/cell-learning-builder)

### 2. 用 `clawhub` CLI 发布单个 Skill

示例：

```bash
clawhub publish ./skills/deep-writer \
  --slug cell-deep-writer \
  --name "Deep Writer" \
  --version 0.1.0 \
  --tags latest \
  --changelog "Initial public release"
```

发布 `opc-case-research` 或 `celf-style-writer` 时，把路径、slug、name、version 改成对应值即可。

如果你想直接在这个仓库里发单个 Skill，也可以用内置脚本：

```bash
./scripts/publish-skill.sh deep-writer --version 0.1.0 --changelog "Initial public release"
```

这个脚本会自动：

- 定位 `skills/<slug>` 目录
- 默认用 `cell-<目录名>` 作为 ClawHub slug，降低重名概率
- 优先读取 `agents/openai.yaml` 里的 `display_name` 作为展示名
- 调用 `clawhub publish`

## 当前兼容性结论

从仓库结构上看，它对 OpenClaw 已经算“可安装”，但之前对 ClawHub 还不够友好，主要问题有：

- README 里没有安装入口，第一次使用的人不知道该指向仓库根目录还是 `skills/`
- 没有写清楚单 Skill 发布与导入的推荐路径
- `SKILL.md` 里有些模板 / 资产文件只是代码字面量，没有用相对链接指向，导致 ClawHub 的 GitHub Import 默认选择文件时，可能漏掉这些依赖文件

这次已经把这些点补齐，仓库现在更适合作为 OpenClaw 共享 Skills 源，也更容易拆成单个 Skill 上 ClawHub。

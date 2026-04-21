# Design Direction Advisor

> **Load when:** 用户需求模糊、没有 design context、或明确说“你帮我推荐风格 / 方向”
> **Skip when:** 已经有明确品牌系统、参考对象和交付方向
> **Why it matters:** 模糊需求最怕直接凭默认审美硬做，最后只得到一个 generic 版本
> **Typical failure it prevents:** 一上来生成“标准 AI 网页”；只给单一方向；没有把可能性空间展示给用户

## Goal

先给用户 3 个明显不同的方向，再让用户选一个继续深化。

## Direction Set

默认从下面这些方向里选 3 个差异足够大的：

| 方向 | 关键词 | 适合什么 |
|---|---|---|
| Swiss / Structured | 克制、网格、强层级、信息建筑 | SaaS、数据页、正式 deck |
| Editorial / Human | serif、留白、内容感、温度 | 品牌页、讲述型页面、内容产品 |
| Soft Tech | 柔和、圆角、自然色、科技但不冷 | AI 产品、移动端、说明页 |
| Dark Precision | 深色、高对比、开发者感、节奏强 | devtools、技术产品、功能页 |
| Bold Campaign | 高冲击、对比强、hero 驱动 | 落地页、发布页、营销页 |
| Quiet Minimal | 极简、留白、低噪音、材料感 | 作品集、介绍页、展示页 |

## Recommendation Rule

推荐时不要给 3 个“几乎一样”的版本。

至少保证：

- 1 个保守稳定方向
- 1 个中等风险、最可能成稿的方向
- 1 个更大胆或更有识别度的方向

## How to Present the 3 Directions

每个方向都要说明：

- 一句话定义
- 适合的原因
- 视觉关键词
- 版式或字体倾向
- 它和另外两个方向最不同的地方

## How to Build After Selection

用户选定一个方向后：

1. 回到主工作流
2. 结合 `design-excellence.md` 明确视觉策略
3. 用最接近的 case study 和模板开始实现

## Useful Internal References

- 产品页偏理性：看 `case-studies/product-pages/stripe-homepage.md`
- 暗色 / 开发者感：看 `case-studies/product-pages/linear-features.md`
- 轻盈 / 亲和：看 `case-studies/product-pages/notion-landing.md`
- 演示稿节奏：看 `case-studies/presentations/keynote-style.md`
- 移动端引导：看 `case-studies/mobile-apps/ios-onboarding.md`

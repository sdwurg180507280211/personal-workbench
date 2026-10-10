---
illustration_id: "04"
type: framework
style: editorial
case_id: canghe-article-editorial
target_path: imgs/06-two-firewalls.png
aspect: "16:9"
source_status: upstream-spec
---

Use case: infographic-diagram
Asset type: 小团子Java公众号技术入门示意图
输入参考：图库案例 canghe-article-editorial 的预览，仅作为整体设计参考，不复制其主题、英文、数字或结论。
设计来源：https://github.com/freestylefly/canghe-skills/blob/dd0bf355955b4c82b764740b4183c86a72ba0e0c/skills/canghe-article-illustrator/references/styles/editorial.md
来源边界：upstream-spec；exactGenerationPrompt=false。以下保留上游 editorial 原文一次，后续内容是本篇适配，不声称已获得样图完整生成记录。

# editorial

Magazine-style editorial infographic for professional content

## Design Aesthetic

High-quality magazine explainer aesthetic. Clear visual storytelling with structured layouts and professional typography. Think Wired, The Verge, or quality science publications. Complex information made digestible.

## Background

- Color: Pure White (#FFFFFF) or Light Gray (#F8F9FA)
- Texture: None or subtle paper grain

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | Pure White | #FFFFFF | Primary background |
| Alt Background | Light Gray | #F8F9FA | Section backgrounds |
| Primary Text | Near Black | #1A1A1A | Headlines, body |
| Secondary Text | Dark Gray | #4A5568 | Captions |
| Accent 1 | Editorial Blue | #2563EB | Primary accent |
| Accent 2 | Coral | #F97316 | Secondary accent |
| Accent 3 | Emerald | #10B981 | Positive elements |
| Accent 4 | Amber | #F59E0B | Attention points |
| Dividers | Medium Gray | #D1D5DB | Section dividers |

## Visual Elements

- Clean flat illustrations
- Structured multi-section layouts
- Callout boxes for insights
- Icon-based visualizations
- Visual metaphors for concepts
- Flow diagrams with hierarchy
- Pull quotes and highlights
- Clear section dividers

## Style Rules

### Do

- Create clear narrative flow
- Use structured layouts
- Include callout boxes
- Design visual metaphors
- Maintain magazine polish

### Don't

- Use photographic imagery
- Create cluttered layouts
- Mix too many styles
- Add purposeless decoration
- Compromise clarity for style

## Best For

Technology explainers, science communication, research articles, policy analysis, investigative pieces, thought leadership, long-form journalism

执行视觉约束：参照所选案例实际样图的白色背景、沉稳深蓝与珊瑚色、细分区线、蓝色主信息区、珊瑚强调、圆形线描示意和短注释。保留整张杂志信息图的层级与叙事关系，不改成普通四宫格图标卡片，不与其他案例混搭。样图里的增长图表、百分比、建筑主题一律替换为本篇内容。
COLORS: 白色 #FFFFFF；深蓝约 #1E5A82；珊瑚约 #F18A77；浅分区线 #A7CED9；中文正文近黑 #1A1A1A。若规范色值与参考图实际观感不同，以传入样图的整体配色为视觉匹配依据。
STYLE: 精细但清晰的平面线描；专业中文无衬线字体，粗标题、短标签、轻注释；少量圆角注释气泡；清爽留白。无照片、无3D、无水印、无第三方标志。所有中文逐字正确，字号可在手机正文中读清。Main elements positioned by content needs with generous white space.
科学与事实边界：仅表现已写正文的概念与关系；不是产品控制台截图，不画精确按钮、伪造界面、真实服务器地址、凭据、未经证实的数据。所有路径或数字若出现，必须是下方明确提供的已核实示例。

TITLE: “端口能不能通，要看两层”
Layout: 沿用参考图的专业杂志分区。左侧是进入流量与端口标签，右侧主图是双层边界，底部短说明；不要画成某厂商界面。
ZONES:
- 左侧：三个必要端口示例标签“22 · SSH”“80 · HTTP”“443 · HTTPS”，配细线流向右侧，不能出现所有端口全开放的意思。
- 右侧外边界：珊瑚色或珊瑚线描，准确标注“外层：云安全组”。
- 右侧内部第二边界：深蓝框或线描，准确标注“内层：服务器 ufw”。服务器在 ufw 边界内部，不把安全组放到服务器内部。
- 进入流量需要依次越过外层安全组和内层 ufw；两层都允许所需端口才通。不画成两条可择一的并行路线。
- 下方注释：“所需端口，两层都要允许”；另一个小提醒“先放行 SSH，再启用 ufw”。
LABELS（逐字）：端口能不能通，要看两层；22 · SSH；80 · HTTP；443 · HTTPS；外层：云安全组；内层：服务器 ufw；服务器；所需端口，两层都要允许；先放行 SSH，再启用 ufw。

ASPECT: 16:9。高清横向 PNG，整张内容完整，禁止边缘裁字。

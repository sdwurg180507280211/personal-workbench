---
illustration_id: "03"
type: comparison
style: editorial
case_id: canghe-article-editorial
target_path: imgs/03-use-vs-default.png
aspect: "16:9"
source_status: upstream-spec
---

Use case: infographic-diagram
Asset type: 小团子Java公众号技术工具入门示意图
输入参考：图库案例 canghe-article-editorial 的实际预览，仅作为整体设计依据，不复制其主题、英文、数字或结论。
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

执行视觉约束：参照所选样图的白色背景、沉稳深蓝与珊瑚色、细分区线、蓝色主信息区、珊瑚强调、圆形线描和短注释。保留整张杂志信息图的专业排印、层级与叙事关系，不改成普通图标卡片，不与其他案例混搭。样图里的主题、增长图表、百分比、建筑、英文一律不用。
COLORS: 白色 #FFFFFF；深蓝约 #1E5A82；珊瑚约 #F18A77；浅分区线 #A7CED9；中文近黑 #1A1A1A。若规范色值与参考图实际观感不同，以实际参考图整体配色为视觉匹配依据。
STYLE: 精细清晰的平面线描；专业中文无衬线字体，粗标题、短标签、轻注释；少量圆角注释气泡；清爽留白。无照片、无3D、无水印、无第三方标志。中文逐字正确，在手机正文中易读。
事实边界：仅表现已读正文和配图需求中的已核实概念；所有图均是概念示意，不画真实截图、假界面、精确按钮、虚构数据或不存在的功能。只允许使用下面明确给出的标签、关系及示例。

TITLE: “临时切换，还是修改默认？”
Layout: 清爽左右比较，仍然采用参考图杂志信息图的深蓝主信息块、珊瑚强调、分区线、抽象图形与短注释，保留信息层次而非两张普通图标卡片。左栏有珊瑚色短标题“sdk use”，一个抽象终端符号被选中，其他终端不被改变，短标签“只影响当前终端”“关闭窗口后失效”。右栏深蓝标题“sdk default”，有三个之后才打开的抽象终端符号由同一个默认版本设置连出，短标签“影响之后新开的终端”“不改变已打开的窗口”。底部统一小注释“图中终端为示意”。
LABELS（逐字）：临时切换，还是修改默认？；sdk use；只影响当前终端；关闭窗口后失效；sdk default；影响之后新开的终端；不改变已打开的窗口；图中终端为示意。
No fake screenshots, menu bars, exact controls, invented code output, or implication that sdk default retroactively changes existing terminals or IDEs.

ASPECT: 16:9。高清横向 PNG，内容完整，禁止边缘裁字。

执行前的具体排除项：不要因为本文讲 Java 就画 Java 咖啡杯、蒸汽、咖啡杯商标或任何第三方 Logo；JDK 只用文字标签和通用工具包/文档图形。终端仅是通用 >_ 概念符号，不要画三色窗口按钮、窗口工具栏、菜单或伪造应用截图。不新增下方未列出的图中文字。

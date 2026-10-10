---
illustration_id: "04"
type: flowchart
style: editorial
case_id: canghe-article-editorial
target_path: imgs/04-sdkmanrc.png
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

TITLE: “让项目记住自己的 JDK”
Layout: 将参考图的多分区叙事改为一个清晰的横向流程主线，仍然保留其整体深蓝与珊瑚配色、白底、细线、短注释和专业中文字号。左侧抽象项目文件夹与纸张 .sdkmanrc，标注“进入项目目录”；中心深蓝主信息区写“切到项目指定版本”，下方用等宽短代码“java=21.0.4-tem”，明确加“示例”；右侧抽象离开文件夹的符号写“离开目录”“恢复默认版本”。箭头只表示已开启自动环境切换时的进入/离开行为，不暗示未配置就自动切换。底部横向珊瑚强调前提“需先开启 sdkman_auto_env=true”，再短注释“标识符以实际列表为准”。
LABELS（逐字）：让项目记住自己的 JDK；.sdkmanrc；进入项目目录；切到项目指定版本；java=21.0.4-tem；示例；离开目录；恢复默认版本；需先开启 sdkman_auto_env=true；标识符以实际列表为准。
Boundary: Java 21 is represented by the complete source-provided example identifier, not the incomplete executable configuration java=21. The auto-env prerequisite must be conspicuous. No fake UI or exact buttons.

ASPECT: 16:9。高清横向 PNG，内容完整，禁止边缘裁字。

执行前的具体排除项：不要因为本文讲 Java 就画 Java 咖啡杯、蒸汽、咖啡杯商标或任何第三方 Logo；JDK 只用文字标签和通用工具包/文档图形。终端仅是通用 >_ 概念符号，不要画三色窗口按钮、窗口工具栏、菜单或伪造应用截图。不新增下方未列出的图中文字。

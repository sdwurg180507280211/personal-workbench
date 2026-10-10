---
illustration_id: "03"
type: framework
style: editorial
case_id: canghe-article-editorial
target_path: imgs/03-ssh-key.png
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

TITLE: “公钥放服务器，私钥留本机”
Layout: 同一参考的杂志分区与蓝珊瑚短注释。左侧是本机与密钥生成，右侧是服务器验证，底部宽注释区说明私钥保管。不绘制密码、密钥文件内容或假登录窗口。
ZONES:
- 左侧本机：标签“自己电脑”，在此生成一对抽象钥匙，标注“公钥”“私钥”。私钥始终留在本机的边界内。
- 上方单向箭头：只有公钥被复制到右侧服务器，标注“公钥放到服务器”。
- 左右之间另一条细虚线：标注“登录验证”，代表本机用私钥证明身份、服务器用公钥验证。绝不能把私钥画成发给服务器，也不能暗示服务器拿到私钥。
- 右侧蓝色主区：一台服务器，公钥标识与验证通过的简单符号。
- 底部珊瑚强调区：“私钥只留本机，不外发”。
LABELS（逐字）：公钥放服务器，私钥留本机；自己电脑；生成一对密钥；公钥；私钥；公钥放到服务器；服务器；登录验证；私钥只留本机，不外发。

ASPECT: 16:9。高清横向 PNG，整张内容完整，禁止边缘裁字。


EDIT CORRECTION — only one targeted change:
Input image 1 is the generated SSH-key illustration to edit. Input image 2 is the editorial style reference.
保留图1的标题、电脑、公钥和私钥位置、服务器、公钥复制箭头、登录验证虚线、颜色、构图、字形与比例。只修改底部珊瑚色长条右侧的小字。
删除“私钥是你身份的唯一凭证”和其下方新增的长句；右侧改为两行准确短句：“不要外发”“不上传网盘或群聊”。
底部左侧大字“私钥只留本机，不外发”保持不变。不得出现“唯一凭证”、唯一登录方式、零风险等绝对化新说法，不添加其他文字。

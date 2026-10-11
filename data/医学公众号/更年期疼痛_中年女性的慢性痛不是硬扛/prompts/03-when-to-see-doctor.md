---
illustration_id: "03"
type: flowchart
style: scientific
case_id: canghe-article-scientific
target: imgs/03-when-to-see-doctor.png
method: deterministic-plot-png
---

Layout: 顶部起点框向下分左右两个就医分支；底部横向六行科室分区表。各分支之间不画病程进展箭头；箭头只表达分流关系。
LABELS（逐字，可换行）：
标题：身体疼痛，什么时候该去医院
起点框：关节或身体疼痛
左支标题：尽快就医（当天或急诊）
左支：关节痛，周围皮肤肿胀、发热｜关节痛，伴发烧、寒战或全身不适｜摔倒或受伤后剧痛、无法行走或负重、关节变形或麻木
右支标题：预约门诊
右支：影响日常活动或睡眠｜越来越重或反复发作｜在家处理 2 周仍未好转｜晨起关节僵硬超过 30 分钟
可以挂哪个科
月经变化、潮热、性交痛、盆腔痛 → 妇科／更年期门诊
关节肿痛、晨僵 → 风湿免疫科
关节、腰背结构问题 → 骨科
头痛、偏头痛 → 神经内科
长期多部位慢性疼痛 → 疼痛科、康复医学科
伴失眠、情绪低落或焦虑 → 心理科
底部：就医信号参考：参考文献[8]；科室建议为一般指引
COLORS: #FAFAFA白底，#1E293B标题，#475569标签，左支#EF4444红橙警示，右支#0D9488蓝绿，底表浅蓝灰#F0F4F8、精细边界。
STYLE: 科学图解、精细一致线条、分色模块和清晰中文字体，不使用卡通、装饰花纹或医学头像。来源为NHS正文已核对信号；科室建议为一般指引，不冒充NHS内容，不添加建议。
ASPECT: 约4:5，竖向但六行表横向呈现，所有长标签逐字一致。

## 案例风格原文（来源状态：upstream-spec，非已核实样图完整生成记录）
# scientific

Academic scientific illustration style for technical diagrams and processes

## Design Aesthetic

Academic scientific illustration aesthetic for biological, chemical, and technical diagrams. Clean, precise diagrams with proper labeling and clear visual flow. Educational clarity with professional polish. Textbook quality illustrations.

## Background

- Color: Off-White (#FAFAFA) or Light Blue-Gray (#F0F4F8)
- Texture: None or subtle paper grain

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | Off-White | #FAFAFA | Primary background |
| Primary Text | Dark Slate | #1E293B | Labels, headers |
| Label Text | Medium Gray | #475569 | Annotations |
| Pathway 1 | Teal | #0D9488 | Primary pathway |
| Pathway 2 | Blue | #3B82F6 | Secondary pathway |
| Pathway 3 | Purple | #8B5CF6 | Tertiary pathway |
| Structure | Amber | #F59E0B | Membranes, structures |
| Alert | Red | #EF4444 | Key elements |
| Positive | Green | #22C55E | Products, outputs |

## Visual Elements

- Precise labeled diagrams
- Flow arrows showing direction
- Modular components with colors
- Chemical formulas and notation
- Cross-section views
- Numbered step sequences
- Molecule and cell representations
- Process summary boxes

## Style Rules

### Do

- Use precise consistent lines
- Label all components clearly
- Show directional flow
- Include technical notation
- Create clear numbered sequences

### Don't

- Use decorative elements
- Create imprecise diagrams
- Omit important labels
- Use inconsistent styling
- Add artistic flourishes

## Best For

Biology articles, chemistry explanations, medical content, research summaries, academic writing, technical documentation, process explanations

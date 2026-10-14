---
illustration_id: 03
type: comparison
style: canghe-article-scientific
target: imgs/03-cervical-rct-data.png
route: controlled-png
---

Use case: productivity-visual
风格依据：https://github.com/freestylefly/canghe-skills/blob/dd0bf355955b4c82b764740b4183c86a72ba0e0c/skills/canghe-article-illustrator/references/styles/scientific.md
来源状态：上游规范原文；未核实为该样图的完整生成记录，不是样图完整生成记录。

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


Asset type: 医学公众号精确数据图，最终PNG。白底教材科学图解、精细灰网格与分区注释，无装饰图标。确定性绘图，不能让生图模型排数字。
Layout: 三组横向条形图；每组光动力组#0D9488、安慰剂组#CBD5E1，共享0%—60%横轴，条形从同一零点出发，长度按真实率严格计算。每组标签在条形上方，比例和人数放条末，必要时超出坐标区但不截断。标题两级、底部来源与终点注释分行，中文黑/深灰无衬线，关键文字手机可读。画布约1200×1300，不加CI、P值或额外面板。
Text (verbatim):
宫颈高级别病变光动力治疗：随机对照试验
6 个月疗效与治疗期间不良事件
光动力组　安慰剂组
治疗有效率
41.1%（104/253）
21.7%（28/129）
人乳头瘤病毒 16/18 型转阴率
31.4%（49/156）
15.4%（12/78）
治疗期间出现不良事件的比例
56.8%（151/266）
56.0%（75/134）
0%　20%　40%　60%
共纳入 402 名成年女性；治疗有效＝6 个月时病理恢复正常或降为低级别病变，且人乳头瘤病毒转阴
各指标分析人群不同；不良事件不一定由治疗引起
数据来源：参考文献[6]

Evidence: Chen等Med2025原论文摘要，DOI10.1016/j.medj.2025.100851；实际核对六组分子分母与百分比。前两项是6个月疗效；第三项是治疗期间TEAE，不是6个月时点发生率。402是总入组数，不可用作所有指标的分母。无新增数据或等安全/等效结论。

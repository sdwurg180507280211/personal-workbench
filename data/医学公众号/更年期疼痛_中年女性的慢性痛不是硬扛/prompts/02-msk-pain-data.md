---
illustration_id: "02"
type: infographic
style: scientific
case_id: canghe-article-scientific
target: imgs/02-msk-pain-data.png
method: deterministic-plot-png
---

Use case: productivity-visual
Layout: 左右两个面板，保持白底、精细线条、分色结构；高分辨率PNG。左面板比例条从0到100%，实际填充71%，64%到78%浅色区间；右面板线性森林图横轴0.8到2.0，OR=1竖参考线。
LABELS（逐字；可换行、不改字）:
围绝经期女性的肌肉骨骼疼痛
A 围绝经期女性中有肌肉骨骼疼痛的比例
71%
95% 置信区间 64%~78%
合并 16 项研究
B 与其他阶段女性相比（比值比 OR）
围绝经期 vs 绝经前　OR 1.63（95% 置信区间 1.35~1.96）
围绝经期 vs 绝经后　OR 1.07（95% 置信区间 0.95~1.20）
OR = 1（无差异）
横轴刻度：0.8　1.0　1.2　1.4　1.6　1.8　2.0
与绝经前相比风险更高；与绝经后相比差异无统计学意义
数据来源：参考文献[4]
DATA: prevalence=0.71; prevalence_CI=[0.64,0.78]; studies=16; row1_OR=1.63,CI=[1.35,1.96]; row2_OR=1.07,CI=[0.95,1.20]。来自Lu等2020研究实际收录摘要；只绘制上述数据，不扩展亚组。
COLORS: 背景#FAFAFA，文字#1E293B/#475569，比例条#0D9488，森林第一行#3B82F6，第二行#8B5CF6，辅助线浅灰。不加人物、装饰或其他数值标签。
ASPECT: 横向约3:2，左右面板；长标签合理换行，手机缩放可读。

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

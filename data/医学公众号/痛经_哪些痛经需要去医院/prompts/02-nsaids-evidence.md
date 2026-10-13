---
illustration_id: 02
type: infographic
style: canghe-article-scientific
---
目标图片：imgs/02-nsaids-evidence.png
案例ID：canghe-article-scientific
风格来源：上游规范原文；未核实为该样图的完整生成记录
参考图片：assets/style-previews/canghe-article-scientific.webp，仅作视觉参考，不借用内容，不承诺像素复现。
STYLE（选中案例规范原文，一次）：
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

本篇内容契约（优先于默认风格中的题材与配色）：
2. `imgs/02-nsaids-evidence.png`（位于「03 止痛药怎么吃才安全有效」小节，“首选的一类止痛药”段落之后；类型：数据图）
   - 要表达：Cochrane 系统评价中，非甾体抗炎药与安慰剂相比，疼痛缓解的人更多，出现不良反应的人也略多。
   - 构图：左右两个面板的横向条形图。面板 A“疼痛缓解”，面板 B“不良反应”。每个面板两根横条：安慰剂（浅灰）、非甾体抗炎药（蓝绿色）。非甾体抗炎药为区间值，用条形主体到 45%（A）/ 11%（B），再用浅色延伸段画到 53%（A）/ 14%（B）表示区间；条长与数值成比例，两个面板使用同一 0%~60% 横轴刻度。不加 OR、置信区间等图中未列出的数字。
   - 图中文字（逐字）：
     - 标题：非甾体抗炎药治疗原发性痛经：效果与不良反应
     - 面板 A 标题：A 获得中等或很好止痛效果的比例
     - 面板 A 安慰剂：18%
     - 面板 A 非甾体抗炎药：45%~53%
     - 面板 B 标题：B 出现不良反应的比例
     - 面板 B 安慰剂：10%
     - 面板 B 非甾体抗炎药：11%~14%
     - 横轴刻度：0%　20%　40%　60%
     - 底部注释：纳入 80 项随机对照试验、5820 名女性；多数比较证据质量为“低”
     - 底部：数据来源：参考文献[4]
ZONES / Layout：严格使用上述构图，各栏对应行对齐，留白为阅读服务。中文全部逐字显示，清晰易读，可换行但不能省略连接词或标签。科学图只用教材式细线，不装饰，不画真实人体或病理，不暗示原发性变成继发性。封面暖粉、浅杏，水彩纸纹与柔软边缘，不画人物、药片或药盒。不要Logo、水印、二维码。
ASPECT：3:2 横向科学图，细节清晰、高分辨率。
执行方式：可控绘图输出PNG。两面板同0%~60%轴，18与10固定；药物条实色到45与11，浅色延长到53与14。精确计算长度，不加OR/CI数字。

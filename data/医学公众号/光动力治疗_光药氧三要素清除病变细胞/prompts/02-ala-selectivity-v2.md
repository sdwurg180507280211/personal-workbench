---
illustration_id: 02-ala-selectivity
type: flowchart
style: canghe-article-scientific
target: imgs/02-ala-selectivity.png
---

Use case: scientific-educational
Input images: Image 1仅为该案例真实样图的视觉参考，不是编辑目标或医学证据。
风格依据：https://github.com/freestylefly/canghe-skills/blob/dd0bf355955b4c82b764740b4183c86a72ba0e0c/skills/canghe-article-illustrator/references/styles/scientific.md
来源状态：上游规范原文；未核实为该样图的完整生成记录，不声称已核实样图的完整生成记录。

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


Asset type: 医学公众号流程图，目标 imgs/02-ala-selectivity.png
Layout: 横向16:9，白底科学图解，三步从左至右，精细均匀线条、教材级细胞示意。箭头仅表示局部给药→转化→照光的操作/机制顺序，不是疾病进展。大号中文无衬线标签，合理换行，不堆成文字墙。
ZONES: 第一列局部药滴与简洁表面示意；第二列两个并排细胞，正常细胞淡红色PpIX点较少、增殖活跃细胞点较多，数量只是相对示意不加具体数字；第三列柔和红光照入虚线治疗区域、旁边示意未受相应光照的区域。底部灰色提示和来源各单独一行。
Text (verbatim):
“氨基酮戊酸怎样‘挑中’病变细胞”
“局部涂抹氨基酮戊酸”
“（前药，本身不能被光激活）”
“在细胞内转化为原卟啉 IX”
“正常细胞：积累较少”
“增殖活跃的细胞：积累较多”
“用特定波长的光照射治疗区域”
“治疗区域”
“未受相应光照：不启动光动力反应”
“选择性是相对的，周围正常组织也可能出现反应”
“概念示意　资料：参考文献[1][2][3][4]”
COLORS: #FAFAFA底，#1E293B标题，#475569说明，#0D9488第一阶段，#3B82F6转化箭头，#8B5CF6第三阶段标号，#F59E0B细胞膜，#EF4444光和PpIX小点。
Constraints: 不写“绝对选择性”“未照光就不用避光”或“无毒”。光敏物质需要对应激活光，不暗示只接受医院照射才会反应。图中没有真实病变外观、不画器官/人体/药品品牌/设备/水印。仅相对积累示意，非定量研究结果。
ASPECT:16:9。依据[3]原论文摘要的ALA/PpIX和活跃细胞积累、[1][4]完整官方光照资料、[2]机制摘要。

Clean composition with generous white space; background and framing are content-appropriate. 不混搭其他案例，不增加清单外标签。

本目标唯一一次重试：严格只保留Text清单中的文字，不能添加“原卟啉 IX (PpIX)”的红点图例或任何清单外标签；红点仅作为无文字的积累示意。第三步仅画柔和光束，不画金属灯头、仪器或设备。保持三步布局、正确原卟啉 IX 用字、准确中文、相对选择性提示。标题用中文双引号“挑中”。

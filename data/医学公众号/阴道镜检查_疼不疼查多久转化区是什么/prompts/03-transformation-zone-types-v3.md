# 03-transformation-zone-types（v3）

- 目标路径：`imgs/03-transformation-zone-types.png`
- 案例 ID：`canghe-article-scientific`
- 类型：概念插图
- 比例：横向约 3:2
- 版本说明：v1 请求被网关安全审核拦截；v2 文字正确但几何关系含糊（1 型鳞柱交界画进了宫颈管内、观察方向与宫颈口方向相反）；v3 明确几何朝向
- 生成方式：图像模型 images/edits，附该案例参考样图

## 完整提示词

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

---

本图任务（医学科普公众号正文配图，横向约 3:2）：
（位于「04 报告上的“转化区”和“鳞柱交界”是什么意思」小节开头；类型：概念插图，概念示意）
   - 要表达：转化区三型的区别在于鳞柱交界在宫颈表面还是缩进宫颈管、能不能完全看到；类型描述的是解剖位置，不是病情轻重。
   - 构图：三栏并排，每栏一个简洁的宫颈纵切面极简几何示意（平面线稿）：外侧粉色表示鳞状上皮，宫颈管内侧浅红表示柱状上皮，交界处用一条醒目的细线标出“鳞柱交界”，交界附近的浅色带标“转化区”；每栏上方一个小眼睛图标示意“从外面看”，1 型和 2 型的交界线全部在视线可及范围内，3 型的交界线一部分在宫颈管深处，用虚线和“看不到”标出。三栏下方各一句说明。底部一条浅灰提示带。
   - 图中文字（逐字）：
     - 标题：转化区的三种类型
     - 通用标注：鳞状上皮；柱状上皮；鳞柱交界；转化区；宫颈管
     - 第 1 栏标题：1 型
     - 第 1 栏说明：全部在宫颈表面，鳞柱交界完全看得见
     - 第 2 栏标题：2 型
     - 第 2 栏说明：部分伸进宫颈管，鳞柱交界仍能完全看到
     - 第 3 栏标题：3 型
     - 第 3 栏说明：伸进宫颈管，鳞柱交界不能完全看到
     - 第 3 栏虚线处标注：看不到
     - 底部提示带：转化区类型说的是位置，不是病情轻重
     - 底部：概念示意　资料：参考文献[2][5][6]

风格要求（v2 重点）：这是教科书式的极简几何示意图，不是解剖插画。每个宫颈示意只用简单的平面几何形状和细线条绘制：一个圆角的“U”形/漏斗形轮廓代表宫颈，中间一条竖直窄通道代表宫颈管；外侧表面用浅粉色平涂色块、通道内侧用浅红色平涂色块区分两种上皮，交界处用一条醒目的深蓝细线标出。纯平面填色，无阴影、无纹理、无肉色、无褶皱、无立体感、无写实组织质感；白底，整体像一张干净的示意线稿图。

几何朝向（v3 必须严格遵守）：三栏的宫颈示意统一朝向——宫颈外口朝上。每个示意是一个倒置的圆顶形：顶部是宫颈外表面（一个平缓的圆拱），圆拱正中有一个开口（宫颈外口），从开口向下延伸出一条竖直窄通道（宫颈管）。眼睛图标在圆拱正上方，从眼睛向下画两条浅灰虚线视线，视线只能看到圆拱表面和开口附近一小段通道。1 型：深蓝鳞柱交界线完整地画在圆拱外表面上、开口两侧（不进入通道），浅黄色转化区带也全部在圆拱外表面上。2 型：深蓝鳞柱交界线位于开口内侧通道最上端一小段，仍在两条视线之内，转化区带从圆拱表面延伸进通道上端。3 型：深蓝鳞柱交界线位于通道深处、在两条视线之外，用深蓝虚线表示，旁边标“看不到”；转化区带从开口一直延伸进通道深处。圆拱外表面（鳞状上皮）浅粉色平涂，通道内壁（柱状上皮）浅红色平涂。

约束：图中所有文字只用中文（不出现英文），只出现上面清单里的文字，逐字一致、不增不减、无错字；标签短而少。这是概念示意，不冒充真实影像或显微照片；不画真实人脸、人物、官方 Logo、二维码、真实检查器械操作场景、仿真病理或惊悚画面；不把相关画成因果，不把非必然进展画成单向病程箭头（检查流程的步骤箭头除外）。参考图只用于学习风格（白底、精细线条、分区标注、分色结构），不照抄参考图中的任何文字或内容。

# 08-to-ollama

- 目标：`imgs/08-to-ollama.png`
- 案例：`canghe-article-editorial`（参考样图 `assets/style-previews/canghe-article-editorial.webp`）
- 比例：横版约 16:9

## 完整提示词

````text
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

## 本图内容（杂志信息图，中文，横版约 16:9）

上下两条路线（并列选择，不是先后步骤）：上面一条标“接法一 · 直接拉取”，一个箭头从“魔搭模型库”直达“Ollama”，箭头上标“ollama run modelscope.cn/作者/模型”（命令后面不加任何符号或圆点），旁边小标签“默认选 Q4_K_M”；下面一条标“接法二 · 先下载再导入”，依次是“魔搭模型库”→一个文件夹里一个“.gguf”文件→一张“Modelfile”卡片→“Ollama”，最后一段箭头标“ollama create”。

## 图中准确的中文标签清单（逐字照写，不增不减）

- 接法一 · 直接拉取
- 魔搭模型库
- Ollama
- ollama run modelscope.cn/作者/模型
- 默认选 Q4_K_M
- 接法二 · 先下载再导入
- .gguf
- Modelfile
- ollama create

## 约束
- 图中所有文字只用下面清单里的中文标签、产品名和命令文字，字形清晰、无错字、无乱码；标签短而少，不额外添加英文说明、段落文字或小字注释。
- 这是概念示意图，不是截图：不画假软件界面、假数据、精确按钮，不画任何官方 Logo、品牌标志或商标图形（包括魔搭、阿里、Hugging Face、Ollama 的标志），产品名只用普通文字书写。
- 不画真实人物，不加水印或作者署名。
- 保留参考样图与上方风格说明的整体构图、配色、线条和文字层级，只替换内容。

````

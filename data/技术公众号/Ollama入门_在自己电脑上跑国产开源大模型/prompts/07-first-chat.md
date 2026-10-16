# 07-first-chat

- 目标：`imgs/07-first-chat.png`
- 案例：`canghe-article-editorial`
- 比例：横版，约 3:2

## 完整提示词

```text
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

## 本图内容

四步横向流程卡片，步骤编号①②③④，用箭头连接：
① 一个简化命令条，写“ollama run qwen3.5:9b”
② 一条进度条，标“下载模型”
③ 一个简化提示符条，写“>>> 输入问题”
④ 写“/bye 退出”
第④步旁边一个小标签“第二次运行不用再下载”。只画简化的图形卡片，不画真实终端界面细节，不写其他输出内容。

## 图中中文标签（逐字照写，不增不减）

①、②、③、④、ollama run qwen3.5:9b、下载模型、>>> 输入问题、/bye 退出、第二次运行不用再下载

## 约束

图中文字以简体中文为主，标签短而少，逐字准确、无错字乱码；只出现上面清单里的标签，清单中的英文名称、版本号和命令按原样逐字照写，不加其他文字；不画假界面、假数据、精确按钮、官方 Logo 或商标；这是示意图，不要做成截图的样子；不画真实人物。
```

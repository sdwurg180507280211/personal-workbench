# 02-irregular-cycles

- 目标路径：imgs/02-irregular-cycles.png
- 案例 ID：canghe-article-scientific（视觉沿用：近白底 #FAFAFA、深石板字色、Teal/Blue/Purple/Amber 分色、细线圆角框）
- 类型：数据图（代码绘制，matplotlib 3.11.2 + Noto Sans CJK SC Regular/Bold）
- 比例：16:9；画布 16x9 英寸，保存 dpi=200（3200x1800），入库时等比缩放到宽 1536
- 数值与文字：逐字取自 配图需求.md 第 2 项；三段等宽，不表示时间长短；数据来源：参考文献[2]（2023 国际循证指南推荐 1.1.1）
- 运行：python3 fig02.py <字体目录> <输出.png>

## 绘图脚本

```python
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch

FONT_DIR = sys.argv[1]
OUT = sys.argv[2]
REG = fm.FontProperties(fname=f"{FONT_DIR}/NotoSansCJKsc-Regular.otf")
BOLD = fm.FontProperties(fname=f"{FONT_DIR}/NotoSansCJKsc-Bold.otf")

# canghe-article-scientific palette
BG, TEXT, LABEL = "#FAFAFA", "#1E293B", "#475569"
TEAL, BLUE, PURPLE, AMBER = "#0D9488", "#3B82F6", "#8B5CF6", "#F59E0B"

W, H = 16.0, 9.0  # inches; 100 dpi x 2 = 3200 x 1800 px, later scaled to 1536 wide
fig = plt.figure(figsize=(W, H), dpi=100)
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

def box(x, y, w, h, fc, ec, lw=1.6, r=0.18):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw))

ax.text(W/2, 8.35, "月经怎样算“不规律”", ha="center", va="center", fontproperties=BOLD, fontsize=34, color=TEXT)

# three equal-width segments (width does not represent duration)
x0, segw, gap = 0.7, 4.75, 0.15
segs = [
    ("初潮后第 1 年内", "不规律属于青春期正常过渡", "#CCFBF1", TEAL),
    ("初潮后 1~3 年", "周期短于 21 天或长于 45 天", "#DBEAFE", BLUE),
    ("初潮 3 年以后至围绝经期", "周期短于 21 天或长于 35 天，\n或一年少于 8 次", "#EDE9FE", PURPLE),
]
band_y, band_h = 6.55, 0.85
for i, (lab, card, light, dark) in enumerate(segs):
    x = x0 + i * (segw + gap)
    box(x, band_y, segw, band_h, dark, dark, r=0.12)
    ax.text(x + segw/2, band_y + band_h/2, lab, ha="center", va="center", fontproperties=BOLD, fontsize=21, color="white")
    box(x, 3.95, segw, 2.3, light, dark)
    ax.text(x + segw/2, 3.95 + 1.15, card, ha="center", va="center", fontproperties=REG, fontsize=21,
            color=TEXT, linespacing=1.5)

# bar spanning segments 2 and 3
bx = x0 + segw + gap
bw = 2 * segw + gap
box(bx, 2.75, bw, 0.85, "#FEF3C7", AMBER)
ax.text(bx + bw/2, 2.75 + 0.425, "初潮 1 年以后：任何一次周期超过 90 天", ha="center", va="center",
        fontproperties=BOLD, fontsize=20, color="#92400E")

# bottom note card
box(x0, 1.15, W - 2*x0, 1.05, "#F1F5F9", "#CBD5E1")
ax.text(W/2, 1.15 + 0.525, "15 岁仍未来月经，或乳房发育 3 年以上仍未来月经，也需要评估", ha="center", va="center",
        fontproperties=REG, fontsize=20, color=LABEL)

ax.text(W - x0, 0.5, "数据来源：参考文献[2]", ha="right", va="center", fontproperties=REG, fontsize=16, color=LABEL)

fig.savefig(OUT, dpi=200, facecolor=BG)
```

# 01-valency-types.png 绘制说明

- 目标路径：imgs/01-valency-types.png
- 案例 ID：canghe-article-scientific（沿用其近白底 #FAFAFA、深板岩文字 #1E293B、青绿 #0D9488、琥珀描边等配色与精细线条）
- 类型：数据图（代码绘制，非生图）
- 内容：三行型别格子条 + 两根 0~100% 横向比例条（71%、约 90%）
- 参数：matplotlib，画布宽 8 英寸 × 200 dpi = 1600 像素（800 逻辑像素 × 2 倍），保存后等比缩放到宽 1536；字体 Noto Sans CJK SC Regular/Bold（notofonts/noto-cjk）
- 运行：python3 figs.py <字体目录> <输出目录>（同一脚本生成 01、02 两张图）
- 图中文字与 配图需求.md 清单逐字一致。

## 绘图脚本

```python
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle

FONT_DIR = sys.argv[1]   # 字体目录（NotoSansCJKsc-Regular.otf / -Bold.otf）
OUT_DIR = sys.argv[2]    # 输出目录
REG = fm.FontProperties(fname=f"{FONT_DIR}/NotoSansCJKsc-Regular.otf")
BOLD = fm.FontProperties(fname=f"{FONT_DIR}/NotoSansCJKsc-Bold.otf")

# canghe-article-scientific 配色
BG = "#FAFAFA"; TEXT = "#1E293B"; LABEL = "#475569"; GRID = "#CBD5E1"
TEAL = "#0D9488"; TEAL_LIGHT = "#5EC4B6"; SLATE_BLUE = "#7C93B0"
APRICOT = "#FCDDBB"; APRICOT_EDGE = "#F59E0B"; TRACK = "#E2E8F0"

W_IN, DPI = 8.0, 200      # 1600 像素宽（800 逻辑像素 × 2 倍）


def canvas(h_in):
    fig = plt.figure(figsize=(W_IN, h_in), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 800); ax.set_ylim(h_in * 100, 0); ax.axis("off")
    return fig, ax


def t(ax, x, y, s, size, bold=False, color=TEXT, ha="left", va="center"):
    ax.text(x, y, s, fontproperties=BOLD if bold else REG, fontsize=size, color=color, ha=ha, va=va)


def fig1():
    fig, ax = canvas(5.9)
    t(ax, 400, 42, "二价、四价、九价，覆盖的型别不同", 19, True, ha="center")
    ax.plot([40, 760], [78, 78], color=GRID, lw=0.8)
    rows = [("二价", ["16", "18"]), ("四价", ["16", "18", "6", "11"]),
            ("九价", ["16", "18", "31", "33", "45", "52", "58", "6", "11"])]
    low = {"6", "11"}
    x0, cw, ch, gap = 130, 62, 40, 5
    for i, (lab, cells) in enumerate(rows):
        y = 112 + i * 56
        t(ax, 60, y + ch / 2, lab, 14, True)
        for j in range(9):  # 未覆盖处留空，仅画淡虚线占位
            x = x0 + j * (cw + gap)
            if j < len(cells):
                c = cells[j]; is_low = c in low
                ax.add_patch(FancyBboxPatch((x, y), cw, ch, boxstyle="round,pad=0,rounding_size=5",
                             fc=APRICOT if is_low else TEAL, ec=APRICOT_EDGE if is_low else TEAL, lw=1))
                t(ax, x + cw / 2, y + ch / 2, c, 13, True, color=TEXT if is_low else "white", ha="center")
            else:
                ax.add_patch(FancyBboxPatch((x, y), cw, ch, boxstyle="round,pad=0,rounding_size=5",
                             fc="none", ec=GRID, lw=0.8, ls=(0, (3, 3))))
    # 图例
    ly = 300
    ax.add_patch(Rectangle((60, ly - 8), 16, 16, fc=TEAL, ec=TEAL))
    ax.add_patch(Rectangle((84, ly - 8), 16, 16, fc=APRICOT, ec=APRICOT_EDGE))
    t(ax, 108, ly, "深色＝高危型　浅色＝低危型（6、11 型可引起尖锐湿疣）", 11.5, color=LABEL)
    ax.plot([40, 760], [330, 330], color=GRID, lw=0.8)
    # 比例条
    bx, bw, bh = 60, 680, 26
    bars = [("16、18 型引起的宫颈癌比例（全球）", "71%", 0.71),
            ("九价所含 7 种高危型，在人乳头瘤病毒阳性宫颈鳞癌中的比例", "约 90%", 0.90)]
    for k, (lab, val, v) in enumerate(bars):
        y = 372 + k * 82
        t(ax, bx, y, lab, 12.5, color=TEXT)
        t(ax, bx + bw, y, val, 15, True, color=TEAL, ha="right")
        ax.add_patch(Rectangle((bx, y + 18), bw, bh, fc=TRACK, ec="none"))
        ax.add_patch(Rectangle((bx, y + 18), bw * v, bh, fc=TEAL, ec="none"))
    # 刻度
    sy = 372 + 82 + 18 + bh
    for v, s in [(0, "0%"), (0.5, "50%"), (1, "100%")]:
        ax.plot([bx + bw * v] * 2, [sy, sy + 7], color=LABEL, lw=1)
        t(ax, bx + bw * v, sy + 20, s, 11, color=LABEL, ha="center")
    t(ax, 760, 562, "数据来源：参考文献[1]", 10.5, color=LABEL, ha="right")
    fig.savefig(f"{OUT_DIR}/01-valency-types.png", dpi=DPI, facecolor=BG)


def fig2():
    fig, ax = canvas(7.4)
    t(ax, 400, 42, "越早接种，获益越大", 20, True, ha="center")
    ax.plot([40, 760], [78, 78], color=GRID, lw=0.8)
    t(ax, 400, 108, "瑞典 167 万名 10~30 岁女性：至少接种 1 剂四价疫苗后，", 12.5, True, ha="center")
    t(ax, 400, 132, "宫颈浸润癌发生率下降", 12.5, True, ha="center")
    # 坐标区：0% 在 y=520，100% 在 y=180
    y0, y100, px = 520, 180, 150
    def Y(v): return y0 - (y0 - y100) * v
    for v, s in [(0, "0%"), (0.5, "50%"), (1, "100%")]:
        ax.plot([px, 740], [Y(v)] * 2, color=GRID if v else LABEL, lw=0.8 if v else 1.2,
                ls="-" if v == 0 else (0, (3, 3)), zorder=0)
        t(ax, px - 12, Y(v), s, 11, color=LABEL, ha="right")
    # 数值为校正后发生率比换算（1-IRR），误差线为 95% 置信区间（Lei 等 2020）
    bars = [("全部接种者", 0.63, (0.43, 0.79), SLATE_BLUE),
            ("17 岁前接种", 0.88, (0.66, 1.00), TEAL),
            ("17~30 岁接种", 0.53, (0.25, 0.73), TEAL_LIGHT)]
    bw = 110
    for i, (lab, v, (lo, hi), c) in enumerate(bars):
        cx = 250 + i * 190
        ax.add_patch(Rectangle((cx - bw / 2, Y(v)), bw, Y(0) - Y(v), fc=c, ec="none"))
        ax.plot([cx, cx], [Y(lo), Y(hi)], color=TEXT, lw=1.1)
        for e in (lo, hi):
            ax.plot([cx - 9, cx + 9], [Y(e)] * 2, color=TEXT, lw=1.1)
        t(ax, cx + bw / 2 + 6, Y(v) + 14, f"{round(v * 100)}%", 15, True, color=c if c != TEAL_LIGHT else "#0F766E", ha="left")
        t(ax, cx, y0 + 24, lab, 12.5, i == 1, ha="center")
    ax.plot([40, 760], [580, 580], color=GRID, lw=0.8)
    # 信息卡
    ax.add_patch(FancyBboxPatch((60, 600), 680, 70, boxstyle="round,pad=0,rounding_size=10",
                 fc="#F0F4F8", ec=TEAL, lw=1))
    # 线性盾牌小图标
    sx, sy = 100, 635
    ax.plot([sx - 16, sx - 16, sx, sx + 16, sx + 16], [sy - 6, sy - 18, sy - 24, sy - 18, sy - 6], color=TEAL, lw=1.6)
    ax.plot([sx - 16, sx, sx + 16], [sy - 6, sy + 20, sy - 6], color=TEAL, lw=1.6)
    ax.plot([sx - 7, sx - 1, sx + 9], [sy - 2, sy + 5, sy - 9], color=TEAL, lw=1.6)
    t(ax, 132, 635, "9~14 岁女孩接种后的抗体水平，是 15 岁以上人群的 2 倍以上", 12.5, color=TEXT)
    t(ax, 760, 712, "数据来源：柱状图 参考文献[2]；信息卡 参考文献[4]", 10.5, color=LABEL, ha="right")
    fig.savefig(f"{OUT_DIR}/02-age-benefit.png", dpi=DPI, facecolor=BG)


fig1(); fig2()
```

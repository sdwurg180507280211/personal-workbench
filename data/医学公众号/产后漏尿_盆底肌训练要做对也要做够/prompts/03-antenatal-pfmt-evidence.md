# 03-antenatal-pfmt-evidence

- 目标路径：`imgs/03-antenatal-pfmt-evidence.png`
- 案例 ID：canghe-article-scientific（视觉沿用：近白底、精细线条、青绿/蓝分色）
- 类型：数据图（代码绘制，未使用生图模型）
- 比例：8 x 6.2 英寸，200 dpi，输出 1600x1240，入库时等比缩放到宽 1536

## 数据（Woodley 等 2020，Cochrane CD007471.pub4，摘要）
- 孕晚期漏尿：RR 0.38（95% CI 0.20～0.72），6 项试验，624 人 → 风险降低 62%，误差线 28%～80%
- 产后 3～6 个月漏尿：RR 0.71（95% CI 0.54～0.95），5 项试验，673 人 → 风险降低 29%，误差线 5%～46%
- 产后已持续漏尿者产后 6～12 个月：RR 0.55（95% CI 0.29～1.07），3 项试验，696 人，低质量证据 → 只写“证据还不充分”，不画条形

## 字体
Noto Sans CJK SC Regular / Bold（notofonts/noto-cjk，Sans/OTF/SimplifiedChinese）

## 绘图脚本（python3 fig03.py <字体目录> <输出.png>，matplotlib 3.11）

```python
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch

font_dir, out = sys.argv[1], sys.argv[2]
REG = fm.FontProperties(fname=font_dir + "/NotoSansCJKsc-Regular.otf")
BOLD = fm.FontProperties(fname=font_dir + "/NotoSansCJKsc-Bold.otf")

BG, INK, GRAY, TEAL, BLUE, LINE = "#FAFAFA", "#1E293B", "#475569", "#0D9488", "#3B82F6", "#CBD5E1"
# Woodley 2020 Cochrane CD007471.pub4：风险降低 = 1 - RR；误差线 = 1 - 95% CI
bars = [
    ("孕晚期漏尿", 62, (28, 80), "降低 62%", "（6 项试验，624 人）", TEAL),
    ("产后 3～6 个月漏尿", 29, (5, 46), "降低 29%", "（5 项试验，673 人）", BLUE),
]

fig = plt.figure(figsize=(8, 6.2), dpi=200, facecolor=BG)
fig.text(0.06, 0.935, "孕期开始盆底肌训练，漏尿风险更低", fontproperties=BOLD, fontsize=19, color=INK)
fig.text(0.06, 0.885, "对象：原本没有漏尿的孕妇；对照：常规孕期保健", fontproperties=REG, fontsize=11.5, color=GRAY)

ax = fig.add_axes([0.06, 0.40, 0.62, 0.42], facecolor=BG)
ys = [1.0, 0.0]
for y, (label, v, (lo, hi), vtxt, ntxt, c) in zip(ys, bars):
    ax.barh(y, v, height=0.36, color=c, alpha=0.88, zorder=3)
    ax.errorbar(v, y, xerr=[[v - lo], [hi - v]], fmt="none", ecolor=INK, elinewidth=1.1, capsize=5, capthick=1.1, zorder=4)
    ax.text(0, y + 0.27, label, fontproperties=BOLD, fontsize=12.5, color=INK, va="bottom", ha="left")
    ax.text(hi + 3, y + 0.06, vtxt, fontproperties=BOLD, fontsize=13, color=c, va="center", ha="left", clip_on=False)
    ax.text(hi + 3, y - 0.14, ntxt, fontproperties=REG, fontsize=10, color=GRAY, va="center", ha="left", clip_on=False)
ax.set_xlim(0, 100)
ax.set_ylim(-0.45, 1.65)
ax.set_yticks([])
ax.set_xticks(range(0, 101, 20))
for t in ax.get_xticklabels():
    t.set_fontproperties(REG); t.set_fontsize(10); t.set_color(GRAY)
ax.grid(axis="x", color=LINE, linewidth=0.6, zorder=0)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRAY)
ax.tick_params(axis="x", colors=GRAY, length=3)
ax.set_xlabel("风险降低比例（%）", fontproperties=REG, fontsize=11, color=GRAY, labelpad=6)

box = FancyBboxPatch((0.06, 0.12), 0.88, 0.13, boxstyle="round,pad=0.008,rounding_size=0.012",
                     transform=fig.transFigure, facecolor="#EEF1F5", edgecolor=LINE, linewidth=0.8)
fig.patches.append(box)
fig.text(0.085, 0.185, "产后已经持续漏尿的女性，盆底肌训练在产后 6～12 个月的效果，\n目前研究证据还不充分",
         fontproperties=REG, fontsize=11.5, color=INK, va="center", linespacing=1.6)
fig.text(0.94, 0.045, "数据来源：参考文献[1]", fontproperties=REG, fontsize=9.5, color=GRAY, ha="right")
fig.savefig(out, dpi=200, facecolor=BG)
```

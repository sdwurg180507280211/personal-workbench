目标图片：imgs/02-guideline-comparison.png
案例ID：canghe-article-scientific（视觉沿用：近白底、精细线条、分区标注、分色）
类型：数据图（代码绘制，未调用生图模型）
比例：1600x1400 绘制（8 英寸宽、200 dpi），保存时等比缩放到宽 1536
字体：Noto Sans CJK SC Regular / Bold（notofonts/noto-cjk）
运行：python3 fig02.py <字体目录> <输出 PNG>（需要 matplotlib）
图中文字与 配图需求.md 第 2 张图清单逐字一致；数字已核对参考文献[1]–[4]。

## 绘图脚本

```python
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle

font_dir, out = sys.argv[1], sys.argv[2]
REG = fm.FontProperties(fname=f"{font_dir}/NotoSansCJKsc-Regular.otf")
BOLD = fm.FontProperties(fname=f"{font_dir}/NotoSansCJKsc-Bold.otf")

# 色板：canghe-article-scientific
BG, INK, GRAY, LINE = "#FAFAFA", "#1E293B", "#475569", "#CBD5E1"
WARM_BG, WARM = "#FFF7ED", "#F59E0B"   # 国内
COOL_BG, COOL = "#EFF6FF", "#3B82F6"   # 国外

rows = [  # (来源, 年龄大字, 年龄小字, 方式与间隔分行, 分组)
    ("国家宫颈癌筛查项目（2022）", "35 岁", "（覆盖 35~64 岁）",
     ["细胞学检查每 3 年 1 次，", "或高危型人乳头瘤病毒检测每 5 年 1 次"], "cn"),
    ("中国子宫颈癌筛查指南（2023）", "25 岁", "",
     ["25~64 岁：人乳头瘤病毒检测或联合筛查", "每 5 年 1 次，或细胞学检查每 3 年 1 次"], "cn"),
    ("世界卫生组织", "30 岁", "", ["高效能检测每 5~10 年 1 次"], "intl"),
    ("美国预防服务工作组（2018）", "21 岁", "",
     ["21~29 岁：细胞学检查每 3 年 1 次；", "30~65 岁：细胞学检查每 3 年 1 次，",
      "或高危型人乳头瘤病毒检测每 5 年 1 次，", "或联合筛查每 5 年 1 次"], "intl"),
]

W = 16.0                      # 坐标单位：0.1 英寸
heights = [max(1.55, 0.62 * len(r[3]) + 0.55) for r in rows]
top_pad, title_h, head_h, gap = 0.6, 1.5, 0.9, 0.18
foot_h = 2.0
H = top_pad + title_h + head_h + sum(heights) + gap * (len(rows) - 1) + 0.3 + foot_h
fig = plt.figure(figsize=(W / 2, H / 2), dpi=200)   # 宽 8 英寸 × 200 dpi = 1600 像素
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
fig.patch.set_facecolor(BG)

ax.text(W / 2, top_pad + 0.65, "宫颈癌筛查建议对比（一般女性）", fontproperties=BOLD,
        fontsize=21, color=INK, ha="center", va="center")

x_grp, x_src, x_age, x_way, x_end = 0.5, 1.45, 5.35, 7.75, W - 0.5
y = top_pad + title_h
ax.add_patch(Rectangle((x_src, y), x_end - x_src, head_h, color="#E2E8F0", lw=0))
for x, t in ((x_src + 0.25, "来源"), (x_age + 0.25, "起始年龄"), (x_way + 0.25, "筛查方式与间隔")):
    ax.text(x, y + head_h / 2, t, fontproperties=BOLD, fontsize=12.5, color=INK, va="center")
y += head_h + 0.08

spans = {}
for (src, age, age_note, way, grp), h in zip(rows, heights):
    bg, accent = (WARM_BG, WARM) if grp == "cn" else (COOL_BG, COOL)
    ax.add_patch(FancyBboxPatch((x_src, y), x_end - x_src, h, boxstyle="round,pad=0,rounding_size=0.18",
                                fc=bg, ec=LINE, lw=0.8))
    ax.plot([x_age, x_age], [y + 0.2, y + h - 0.2], color=LINE, lw=0.8)
    ax.plot([x_way, x_way], [y + 0.2, y + h - 0.2], color=LINE, lw=0.8)
    ax.text(x_src + 0.25, y + h / 2, src.replace("（", "\n（"), fontproperties=BOLD, fontsize=11.5,
            color=INK, va="center", linespacing=1.45)
    if age_note:
        ax.text(x_age + 1.2, y + h / 2 - 0.3, age, fontproperties=BOLD, fontsize=22, color=accent, ha="center", va="center")
        ax.text(x_age + 1.2, y + h / 2 + 0.5, age_note, fontproperties=REG, fontsize=8.5, color=GRAY, ha="center", va="center")
    else:
        ax.text(x_age + 1.2, y + h / 2, age, fontproperties=BOLD, fontsize=22, color=accent, ha="center", va="center")
    ax.text(x_way + 0.25, y + h / 2, "\n".join(way), fontproperties=REG, fontsize=11.5, color=INK,
            va="center", linespacing=1.6)
    spans.setdefault(grp, [y, y + h])[1] = y + h
    y += h + gap

for grp, (y0, y1) in spans.items():
    c, label = (WARM, "国内") if grp == "cn" else (COOL, "国外")
    ax.add_patch(FancyBboxPatch((x_grp, y0), 0.6, y1 - y0, boxstyle="round,pad=0,rounding_size=0.25", fc=c, ec="none"))
    ax.text(x_grp + 0.3, (y0 + y1) / 2, "\n".join(label), fontproperties=BOLD, fontsize=13, color="white",
            ha="center", va="center", linespacing=1.3)

y += 0.15
ax.add_patch(FancyBboxPatch((x_grp, y), x_end - x_grp, 0.95, boxstyle="round,pad=0,rounding_size=0.2",
                            fc="#F1F5F9", ec="none"))
ax.text(x_grp + 0.35, y + 0.475, "人类免疫缺陷病毒感染女性：世界卫生组织建议从 25 岁开始，每 3~5 年 1 次",
        fontproperties=REG, fontsize=11.5, color=INK, va="center")
ax.text(W / 2, y + 1.45, "数据来源：参考文献[1][2][3][4]（第 1 行[1]，第 2 行[2]，第 3 行及备注[3]，第 4 行[4]）",
        fontproperties=REG, fontsize=9.5, color=GRAY, ha="center", va="center")
fig.savefig(out, dpi=200, facecolor=BG)
```

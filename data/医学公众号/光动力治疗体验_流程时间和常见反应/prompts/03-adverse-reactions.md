---
illustration_id: 03-adverse-reactions
type: 数据图（代码绘制）
style: canghe-article-scientific
---
目标图片：imgs/03-adverse-reactions.png
案例ID：canghe-article-scientific（沿用白/近白底、精细线条、分区标注与分色）
类型：数据图，matplotlib 代码绘制，锁定数字与文字
比例：5:4（1600x1280，figsize 8x6.4 英寸，dpi 200），入库时等比缩放到宽 1536
字体：Noto Sans CJK SC Regular/Bold（notofonts/noto-cjk）
数据（参考文献[2]，国家医保局 2026 年申报材料公示版说明书摘录，已核对全文）：至少发生 1 次不良反应 治疗组 31.3%、安慰剂组 25.6%；治疗组阴道分泌物 12.5%、腹痛 5.7%、阴道出血 4.5%；严重程度均为轻度至中度，无重度或严重不良反应。
配色：背景 #FAFAFA；文字 #1E293B / #475569；治疗组 #E8836B；安慰剂组 #CBD5E1。原文无置信区间，不画误差线。

绘图脚本：

```python
# 绘制 imgs/03-adverse-reactions.png（数据图，代码绘制）
# 用法：FONT_DIR=<Noto Sans CJK SC 字体目录> python3 plot03.py <输出.png>
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

fd = os.environ['FONT_DIR']
for w in ('Regular', 'Bold'):
    fm.fontManager.addfont(os.path.join(fd, f'NotoSansCJKsc-{w}.otf'))
plt.rcParams['font.family'] = 'Noto Sans CJK SC'

BG, TXT, SUB, GRID = '#FAFAFA', '#1E293B', '#475569', '#E2E8F0'
TREAT, PLACEBO = '#E8836B', '#CBD5E1'

fig = plt.figure(figsize=(8, 6.4), dpi=200, facecolor=BG)
fig.text(0.5, 0.955, '治疗后的不良反应：多为轻度至中度', ha='center', va='center',
         fontsize=17, fontweight='bold', color=TXT)

def panel(rect, title, labels, values, colors, xmax, ticks):
    ax = fig.add_axes(rect, facecolor=BG)
    y = list(range(len(labels)))[::-1]
    ax.barh(y, values, height=0.56, color=colors, edgecolor='none', zorder=3)
    for yi, v in zip(y, values):
        ax.text(v + xmax * 0.012, yi, f'{v}%', va='center', ha='left',
                fontsize=12.5, fontweight='bold', color=TXT, zorder=4)
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=12.5, color=TXT)
    ax.set_xlim(0, xmax); ax.set_xticks(ticks)
    ax.set_xticklabels([f'{t}%' for t in ticks], fontsize=10, color=SUB)
    ax.set_ylim(-0.6, len(labels) - 0.4)
    ax.grid(axis='x', color=GRID, linewidth=0.8, zorder=0)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#94A3B8'); ax.spines['bottom'].set_linewidth(0.8)
    ax.tick_params(axis='y', length=0, pad=8); ax.tick_params(axis='x', color='#94A3B8', length=3)
    fig.text(0.06, rect[1] + rect[3] + 0.045, title, ha='left', va='center',
             fontsize=13.5, fontweight='bold', color=TXT)
    return ax

panel([0.22, 0.615, 0.68, 0.17], 'A　至少发生 1 次不良反应的比例',
      ['治疗组', '安慰剂组'], [31.3, 25.6], [TREAT, PLACEBO], 40, [0, 10, 20, 30, 40])
fig.add_artist(plt.Line2D([0.06, 0.94], [0.505, 0.505], color='#CBD5E1', linewidth=0.9))
panel([0.22, 0.215, 0.68, 0.21], 'B　治疗组较多见的不良反应',
      ['阴道分泌物', '腹痛', '阴道出血'], [12.5, 5.7, 4.5], [TREAT] * 3, 15, [0, 5, 10, 15])
fig.text(0.5, 0.105, '严重程度均为轻度至中度，无重度或严重不良反应', ha='center', va='center',
         fontsize=11.5, color=SUB)
fig.text(0.5, 0.045, '数据来源：参考文献[2]（药品说明书收载的关键随机对照试验双盲期数据）',
         ha='center', va='center', fontsize=9.5, color=SUB)
fig.savefig(sys.argv[1], dpi=200, facecolor=BG)
```

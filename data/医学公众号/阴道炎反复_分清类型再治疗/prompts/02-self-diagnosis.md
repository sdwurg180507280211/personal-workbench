# 02-self-diagnosis

- 目标路径：`imgs/02-self-diagnosis.png`
- 案例 ID：`canghe-article-scientific`（沿用其近白底 #FAFAFA、深石板文字 #1E293B、蓝绿 #0D9488 主色与精细线条）
- 类型：数据图（代码绘制，matplotlib + Noto Sans CJK SC）
- 比例：1600x1080（8x5.4 英寸，200 dpi，2 倍清晰度），入库时等比缩放到宽 1536
- 数据：Ferris DG, et al. Obstet Gynecol 2002;99(3):419-425（参考文献[8]，PubMed 摘要核对）：n=95；霉菌性阴道炎 33.7%、混合性阴道炎 21.1%、细菌性阴道病 18.9%、检查正常 13.7%、其他问题 10.5%、滴虫性阴道炎 2.1%（合计 100.0%）
- 运行：`python3 fig02.py <字体目录> <输出.png>`

## 绘图脚本

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import sys
fontdir, out = sys.argv[1], sys.argv[2]
for w in ('Regular', 'Bold'):
    fm.fontManager.addfont(f'{fontdir}/NotoSansCJKsc-{w}.otf')
plt.rcParams['font.family'] = 'Noto Sans CJK SC'

# 数据：参考文献[8] Ferris 2002 摘要，n=95，从高到低
data = [('霉菌性阴道炎', 33.7, '#0D9488'),
        ('混合性阴道炎', 21.1, '#F6D9BF'),
        ('细菌性阴道病', 18.9, '#DDD3F5'),
        ('检查正常', 13.7, '#CFDCEB'),
        ('其他问题', 10.5, '#DCDFE4'),
        ('滴虫性阴道炎', 2.1, '#F5D3DC')]
INK, MUTED, BG = '#1E293B', '#475569', '#FAFAFA'

fig = plt.figure(figsize=(8, 5.4), dpi=200, facecolor=BG)  # 1600 x 1080 像素
ax = fig.add_axes([0.24, 0.17, 0.66, 0.6], facecolor=BG)
y = list(range(len(data)))[::-1]
for yi, (name, v, c) in zip(y, data):
    ax.barh(yi, v, height=0.62, color=c, edgecolor='#94A3B8' if c != '#0D9488' else '#0D9488', linewidth=0.6)
    ax.text(v + 0.6, yi, f'{v}%', va='center', ha='left', fontsize=13,
            color=INK, fontweight='bold' if name == '霉菌性阴道炎' else 'normal')
ax.set_yticks(y)
ax.set_yticklabels([d[0] for d in data], fontsize=13, color=INK)
ax.get_yticklabels()[0].set_fontweight('bold')
ax.set_xlim(0, 38)
ax.set_xticks([])
for s in ('top', 'right', 'bottom'):
    ax.spines[s].set_visible(False)
ax.spines['left'].set_color('#94A3B8')
ax.tick_params(axis='y', length=0, pad=8)

fig.text(0.05, 0.92, '自认为是霉菌性阴道炎，实际诊断是什么', fontsize=19, fontweight='bold', color=INK)
fig.text(0.05, 0.855, '95 位准备自行购买抗真菌药的女性，经医生检查后的结果', fontsize=12.5, color=MUTED)
fig.add_artist(plt.Line2D([0.05, 0.95], [0.1, 0.1], color='#CBD5E1', linewidth=0.8))
fig.text(0.05, 0.05, '美国研究，2002 年发表', fontsize=10.5, color=MUTED)
fig.text(0.95, 0.05, '数据来源：参考文献[8]', fontsize=10.5, color=MUTED, ha='right')
fig.savefig(out, facecolor=BG)
```

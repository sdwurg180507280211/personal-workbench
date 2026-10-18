---
illustration_id: 02
type: 数据图
style: canghe-article-scientific
---
目标图片：imgs/02-avoidance-duration.png
案例ID：canghe-article-scientific（沿用其背景 #FAFAFA、文字 #1E293B/#475569、Teal #0D9488、Purple #8B5CF6 分色与精细线条）
类型：数据图（代码绘制，非生图）
比例：约 10:7 横向；matplotlib，figsize=(8,5.6)，dpi=200 → 1600×1120，入库时等比缩放到宽 1536
字体：Noto Sans CJK SC Regular / Bold（notofonts/noto-cjk）

数据（单位：天，条长严格按数值；均已核对原文）：
- 外用氨基酮戊酸：约 48 小时 → 2 天（FDA 氨基酮戊酸凝胶说明书 5.5 节全文；参考文献[2][6]）
- 海姆泊芬：2 周 → 14 天（Zhao 2016 PLoS One 全文 Methods；参考文献[5]）
- 血卟啉注射液：1 个月 → 30 天（国内说明书全文「严格避光一个月」；参考文献[4]）
- 卟吩姆钠：至少 30 天 → 30 天，浅紫虚线延伸至 90 天（DailyMed 美国说明书全文「at least 30 days… up to 90 days or more」；参考文献[3]）
横轴 0–96，刻度 0/30/60/90；无误差线（来源未给区间）。

图中文字与配图需求.md 清单逐字一致：标题、分组标签「局部外用」「静脉注射」、四条标签与数值、「部分人可达 90 天或更久」、横轴标题「避光时间（天）」、图下注释、「数据来源：参考文献[2][3][4][5][6]」。

绘图脚本：
```python
import sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch
FD=sys.argv[1]; OUT=sys.argv[2]  # 字体目录、输出路径
R=fm.FontProperties(fname=FD+'/NotoSansCJKsc-Regular.otf'); B=fm.FontProperties(fname=FD+'/NotoSansCJKsc-Bold.otf')
INK='#1E293B'; GRAY='#475569'; TEAL='#0D9488'; TEAL_L='#99F6E4'; PUR='#8B5CF6'; PUR_L='#C4B5FD'; BG='#FAFAFA'; GRID='#E2E8F0'
# 数据（天）：外用氨基酮戊酸约 48 小时 = 2 天；海姆泊芬 2 周 = 14 天；血卟啉注射液 1 个月 = 30 天；卟吩姆钠至少 30 天，虚线延伸至 90 天
bars=[('外用氨基酮戊酸',2,'约 48 小时（治疗部位及周围皮肤）',TEAL),
      ('海姆泊芬',14,'2 周（随机对照试验方案）',PUR),
      ('血卟啉注射液',30,'1 个月（国内说明书）',PUR),
      ('卟吩姆钠',30,'至少 30 天（美国说明书）',PUR)]
fig=plt.figure(figsize=(8,5.6),dpi=200); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.25,0.24,0.70,0.58]); ax.set_facecolor(BG)
ys=[4.0,2.6,1.6,0.6]; h=0.5
for (lab,v,val,c),y in zip(bars,ys):
    ax.barh(y,v,height=h,color=c,edgecolor='none',zorder=3)
    ax.text(-2.5,y,lab,ha='right',va='center',fontproperties=B,fontsize=11.5,color=INK)
    ax.text(v+1.2,y+(0.0 if v<90 else 0),val,ha='left',va='center',fontproperties=R,fontsize=10,color=GRAY,zorder=4)
# 卟吩姆钠虚线延伸
yb=ys[3]
ax.plot([30,90],[yb,yb],color=PUR_L,lw=3.2,ls=(0,(3,2)),zorder=2)
ax.plot([90],[yb],marker='|',color=PUR_L,ms=14,mew=2.2,zorder=2)
ax.text(90,yb-0.48,'部分人可达 90 天或更久',ha='right',va='top',fontproperties=R,fontsize=9.5,color=PUR)
# 把卟吩姆钠数值标签移到条上方，避免和虚线重叠
for t in ax.texts:
    if t.get_text()=='至少 30 天（美国说明书）': t.set_position((31.2,yb+0.42))
# 分组标签
for y,lab,c in [(4.0,'局部外用',TEAL),(1.6,'静脉注射',PUR)]:
    pass
ax.text(-2.5,4.62,'局部外用',ha='right',va='center',fontproperties=B,fontsize=10,color='white',
        bbox=dict(boxstyle='round,pad=0.35',fc=TEAL,ec='none'))
ax.text(-2.5,3.22,'静脉注射',ha='right',va='center',fontproperties=B,fontsize=10,color='white',
        bbox=dict(boxstyle='round,pad=0.35',fc=PUR,ec='none'))
ax.axhline(3.3+0.0,xmin=0,xmax=1,color=GRID,lw=0.8)
ax.set_xlim(0,96); ax.set_ylim(-0.2,5.0)
ax.set_xticks([0,30,60,90]); ax.set_xticklabels(['0','30','60','90'])
for l in ax.get_xticklabels(): l.set_fontproperties(R); l.set_fontsize(10); l.set_color(GRAY)
ax.set_yticks([]); ax.xaxis.grid(True,color=GRID,lw=0.8,zorder=0)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(GRAY); ax.tick_params(axis='x',colors=GRAY,length=3)
ax.set_xlabel('避光时间（天）',fontproperties=R,fontsize=10.5,color=GRAY,labelpad=6)
fig.text(0.04,0.92,'不同光敏剂，避光时间差别很大',fontproperties=B,fontsize=16,color=INK,ha='left')
fig.text(0.04,0.085,'具体避光时间和范围以所用药品说明书和医嘱为准',fontproperties=R,fontsize=10,color=INK,ha='left')
fig.text(0.04,0.035,'数据来源：参考文献[2][3][4][5][6]',fontproperties=R,fontsize=9,color=GRAY,ha='left')
fig.savefig(OUT,dpi=200,facecolor=BG)
```

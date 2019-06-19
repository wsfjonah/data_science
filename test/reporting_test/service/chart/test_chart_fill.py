import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

import pandas as pd
import numpy as np


t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)

#曲线
plt.plot(t, s)

# 以y轴0点画横线
plt.axhline(linewidth=8, color='#d62728')

# 画横线
plt.axhline(y=1)

# 画纵线
plt.axvline(x=1)

# Draw a thick blue vline at x=0 that spans the upper quadrant of the yrange
# plt.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')

# 画线段
plt.axhline(y=.5, xmin=0.25, xmax=0.75)

# 平行填充
plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)

# 垂直填充
plt.axvspan(1.25, 1.55, facecolor='#2ca02c', alpha=0.5)

# 坐标轴
plt.axis([-1, 2, -1, 2])

plt.show()
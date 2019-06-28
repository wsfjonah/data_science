import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# n个点
n = 1024
# 平均值是0，方差是1
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 确定颜色
T = np.arctan2(Y, X)

print(X)
print(Y)
print(T)

# plt.scatter(X, Y, s=75, c=T, cmap=cm.Reds, alpha=0.5)
plt.scatter(X, Y, s=60, c=Y, alpha=0.5)


plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 隐藏所有的ticks
plt.xticks(())
plt.yticks(())

plt.show()


import matplotlib.pyplot as plt
import numpy as np


# 通过x，y计算高度
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
    # return x


def f2(x, y):
    xy_map = np.zeros((len(y), len(x))).tolist()
    for x0 in x:
        for y0 in y:
            xy_map[y.tolist().index(y0)][x.tolist().index(x0)] = abs(x0)+abs(y0)
    return xy_map


n = 60
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

print(x)
print(y)

# 把x，y绑定成网格的输入值
X, Y = np.meshgrid(x, y)

print(X)
print(Y)

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
# contour为网格
# 8代表分成10部分
# 0分成2部分
# plt.cm.cool为冷色调,plt.cm.hot为暖色调,plt.cm.Spectral,plt.cm.hsv,plt.cm.ocean
# plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hsv)  # 画上颜色
plt.contourf(X, Y, f2(x, y), 8, alpha=0.75, cmap=plt.cm.hsv)

# use plt.contour to add contounlines
# 画线,contour为等高线的线
C = plt.contour(X, Y, f2(x, y), 8, colors='black')

# adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print([1, 2, 3] in a.tolist())

print(a.tolist().index([4,5,6]))

b = np.ones(3)

c = np.array([[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]])

print(a)

print(b)

print(c)

b = np.append(b, 1)

print(b)

print(np.zeros((8, 9)).tolist())

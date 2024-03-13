import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x)

vstack = np.vstack((x, y))
print(vstack)

hstack = np.hstack((x, y))
print(hstack)


def returnSum(x, y):
    return x + y


returnSum(3, 4)

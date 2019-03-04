import numpy as np
# A = np.array([2, 3], dtype='object')
# print(A[0])
# print(type(A[0]))# <class 'int'>

x = np.matrix([[1, 2], [4, 3]])
print(x.sum())

print(x.sum(axis=1))


print(x.sum(axis=1, dtype='float'))


out = np.zeros((2, 1), dtype=float)

print(x.sum(axis=1, dtype='float', out=out))

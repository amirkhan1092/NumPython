import numpy as np

'''
1. matrix
2. mat
3. array

Numpy matrices are strictly 2-dimensional, while numpy arrays (ndarrays) are N-dimensional. 
Matrix objects are a subclass of ndarray, so they inherit all the attributes and methods of ndarrays.

The main advantage of numpy matrices is that they provide a convenient notation for matrix multiplication: 
if a and b are matrices, then a*b is their matrix product.
'''

A = np.mat('2 4;6 3')
print(A)

S = np.matrix('3,5;7,9')
print(S)

G = np.array([[2, 4],[7, 9]])
print(G)
# mat and matrix both are the same but array is n-dimensional
print('mat ', type(A))
print('matrix ', type(S))
print('Array  ', type(G))

# A = np.array([2, 3], dtype='object')
# print(A[0])
# print(type(A[0]))# <class 'int'>


x = np.matrix([[1, 2], [4, 3]])
print(type(x))
print(x.sum())

print(x.sum(axis=1))


print(x.sum(axis=1, dtype='float'))


out = np.zeros((2, 1), dtype=float)

# print(x.sum(axis=1, dtype='float', out=out))


# Addition/Subtraction
A = np.array([[2,4,5],[3,5,5]])
B = np.array([[3,2,1],[2,7,4]])
C = A+B # normal array elementary operation
C = C - 2 # Add value with every elements
print(C)


A = np.mat('2,4,5;3,5,5')
B = np.mat('3,2,1;2,7,4')
C = A+B # matrix elementary operation result will be same as array for addition only
C = C - 4
print(C)

# Multiplication and Division
A = np.array([[2,4],[3,5],[3,7]])
A = np.mat('2,4,4;3,5,2;3,7,8')
B = np.array([[3,2,3],[2,7,8]])
B = np.mat('3,2,3;2,7,8;4,3,7')
C = np.multiply(A, B) # elementary operation
print(C)
C = A * B # normal array elementary operation in array only but in matrix type its change to matrix multiplication
print(C)
C = np.matmul(A, B)  # matrix multiplication
print(C)
C = np.dot(A, B)  # matrix multiplication
print(C)
C = C * 2 # Multiply value with every elements
print(C)


# transpose matrix

A = np.array([[2,3,4],[3,5,6]])
print(A)

A = A.transpose()
print(A)


A = np.linspace(0, 2, 10)
print(A)
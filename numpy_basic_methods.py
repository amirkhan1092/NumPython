import numpy as np


# sd = np.array([2,3,4,3,5,4])
#
# print(sd)
#
# dd = sd.reshape(2,3)
#
# print(dd)

# output
'''
[2 3 4 3 5 4]
[[2 3 4]
 [3 5 4]]
'''

#DType

A = np.array([2,3],dtype='int32')
print(A)
# output [2 3]
A.dtype = 'int16'
print(A)
# output [2 0 3 0]
A.dtype = 'int8'
print(A)
# output [2 0 0 0 3 0 0 0]

# Built in type
print(A[0]) # output 2
print(type(A[0])) # not a object like like int ,float,etc <class 'numpy.int8'>
A = np.array([2,3])

# make it object
# ?A.dtype = object # cant change or modify it to the object so we can perform normal operation on its elements






# Numpy Array vs Python List

#
#
# import time
#
# import numpy
#
#
# def Pure_python_list():
#      t1 = time.time()
#      x1 = range(1000000)
#      x2 = range(1000000)
#      X = [x1[i]+x2[i] for i in range(len(x1))]
#      return time.time()-t1
#
# def Numpy_array():
#      t1 = time.time()
#      x1 = numpy.arange(1000000)
#      x2 = numpy.arange(1000000)
#
#      X = x1 + x2
#      return time.time()-t1
#
#
# print(Pure_python_list())
#
# print(Numpy_array())
#
#



# Linear Algebra

# np.identity matrix
"""
A square matrix in which all the elements of the Diagonals are 1 , and all the others are Zero

NOTE : The effect of multiplying the given matrix by the identity matrix == the result should be unchanged matrix
"""


import numpy as np

a = np.identity(3, dtype=int) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=bool) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=bytes) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=bytearray) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=str) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=object) # default = float
print(a)

print("="*100)

a = np.identity(3, dtype=None) # default = float
print(a)

print("="*100)


# np.matmul() - Matrix Multiplication

import numpy as np

a = np.arange(3)
print(a)

b = np.random.randint(2,10,size=(3,))
print(b)

c = np.matmul(a,b)  # Each row of array is multiplied by each column of array
print(c)

print(a*b)  # shows only the multiply of two vectors


# Find the determinant of linear algebra:

import numpy as np

a = np.arange(1,5).reshape(2,2)
print(a)
print(a.ndim)
print(type(a))

print("="*100)

b = np.linalg.det(a)
print(b)

print("="*100)

# Example 2

import numpy as np
ndarray = np.array([[1,-2,3],[2,-3,-4],[5,-2,-6]])
print(ndarray)

a = np.linalg.det(ndarray)
print(a)

print("="*100)
# np.linspace():

# 6 parameters - start, stop, num, endpoint, retstep, dtype

a = np.linspace(start=0,stop=10,num=2,endpoint=True,retstep=True,dtype=float)
print("Numpy . linspace:",a)


a = np.linspace(start=0,stop=10,num=5,endpoint=False,retstep=False,dtype=int)
print("Numpy . linspace:",a)

print("="*100)

# Example:

# Using linspace creating nd array:

import numpy as np
x= np.linspace(start=0,stop=100,num=20,endpoint=True,retstep=False,dtype=int)
print(x)
y = x.reshape(5,4)
print(y)
print(type(y))
print(len(x))
print(len(y))

print("="*100)

# Using linspace can able to draw graph:

# Example

# import numpy as np
# import matplotlib.pyplot as ply
#
# N=8
# a = np.zeros(N)
# print(a)
#
# x = np.linspace(0,10,N,endpoint=True,retstep=False)
# print(x)
# y = np.linspace(0,10,N,endpoint=True,retstep=False)
# print(y)
#
# plt.plot(x,y,'o')
# plt.show()
#
print("="*100)

# # Example 2 :
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0,2*np.pi,10,endpoint=True,retstep=False)
# print("Linspace:", x)
# #
# y = np.tan(x)
# print(y)
#
# plt.plot(x,y)
# plt.show()
#
# print("="*100)

# Example 3 - for np.linspace

"""retstep=True == Output will be Tuple"""

import numpy as np

x1 = np.linspace(start=100,stop=1000,num=50,endpoint=True,retstep=True)
print(x1)

print("="*100)

# np.logspace()

# Default base10

import numpy as np
data = np.logspace(start = 2,stop = 5,num = 5,dtype='i4')  # Default base10 so, it takes 10 power of 2 & 10 power of 5
print("Logspace:",data)

data = np.logspace(start = 2,stop = 5,num = 2,base = 2,dtype='i1')  #  base2 so, it takes 2 power of 2 & 2 power of 5
print("Logspace:",data)
print(data.dtype)

data = np.logspace(start = 2,stop = 5,num = 5,base = 5,dtype='i4')  #  base2 so, it takes 5 power of 2 & 5 power of 5
print("Logspace:",data)

data = np.logspace(start = 2,stop = 3,num = 10,base = 9,endpoint = False,dtype='i4')  #  base2 so, it takes 9 power of 2 & 9 power of 5
print("Logspace:",data)

data = np.logspace(2,10)  #  base2 so, it takes 4 power of 2 & 4 power of 5
print("Logspace:\n",data)  # no num is given, so it take 50 num as dufault & base 10

data = np.logspace(5,2)  # start value is < stop value
print("Logspace:\n",data)  # gives the output in descending order







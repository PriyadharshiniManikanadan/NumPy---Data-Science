# Adds Dimensions -

# 1. np.newaxis
# 2. np.atleast_2/3D
# 3. np.expand_dims  --  @ specified position using [axix = 0/1/2/3/4] based on index

# Reduces Dimensions -

# 1. np.nditer(flags=external_loop) ,
# 2. np.flatten() ,
# 3. reshape(-1)
# 4. np.squeeze - Removes ALL 1D(single dimension entry) in array shape


# To convert vector into 1D / 2D / 3D
import numpy as np
a = [1,2,3,4,5]
print(a)
print(np.ndim(a))
print(np.shape(a))

print("====================================")

b = np.atleast_2d(a)  # increases the dimensions in rows
print(b)
print(np.ndim(b))
print(np.shape(b))

print("====================================")

c = np.atleast_3d(a)  # increses the dimension in columns
print(c)
print(np.ndim(c))
print(np.shape(c))

print("====================================")

# Transpose

a = np.arange(9).reshape(3,3)
print(a)

print("====================================")

b =a.T
print(b)

print("====================================")

# Transpose() method
"""Permutes the dimensions of the given array"""

# parameters = (array, axes)

# Without axes / rows & columns

A = np.arange(12).reshape(4,3)
print(A)
print(A.ndim)
print("====================================")
B = A.transpose()
print(B)
print(B.ndim)
print("====================================")

# with axes

X = np.arange(24).reshape((2,4,3))
print(X)
print(X.ndim)

# Permutations shows the number of models we can pass axes to the array

# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

# Example 1  - in 3D

Y = X.transpose(0,1,2)
print(Y)
print("====================================")
Y = X.transpose(0,2,1)
print(Y)
print("====================================")
Y = X.transpose(1,0,2)
print(Y)
print("====================================")

# To check the permutations possible in the array - import itertools - permutations

import itertools as itt
obj = [0,1,2]
X = itt.permutations(obj)
print(X)
print(list(X))
print("====================================")

# Example 2 - in 4D

X = np.arange(24).reshape((1,2,4,3))
print(X)
print(X.ndim)
print("====================================")

L1 = [0,1,2,3]

Y = itt.permutations(L1)  # Possibilities of permutations

# [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2),
# (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3), (2, 1, 3, 0),
# (2, 3, 0, 1), (2, 3, 1, 0), (3, 0, 1, 2), (3, 0, 2, 1), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]

print(Y)
print(list(Y))

print("====================================")

U = X.transpose(2,3,1,0)
print(U)
print(U.ndim)

# Broadcast() method

arr1 = np.array([[1],[2],[3],[4]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print("====================================")
arr2 = np.array([1,2,3,4])
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print("====================================")

# Using Broadcast() method

arrays = np.broadcast(arr1,arr2)
print(arrays)
print(list(arrays))
print(arrays.ndim)
print(arrays.shape)

print("====================================")

arrays1 = np.broadcast(arr1+arr2)
print(arrays1)
print(list(arrays1))
print(arrays1.ndim)
print(arrays1.shape)

print("====================================")
arrays2 = np.broadcast(arr1*arr2)
print(arrays2)
print(list(arrays2))
print(arrays2.ndim)
print(arrays2.shape)

print("====================================")

# np.expand_dims

""" Expands the array to be inserting a new axis (dimensions) at the specified position"""

# Paramaters = ( arr, axis )

#example :
# if  axis = 0 : it adds 1D before the 0th index
# if  axis = 1 : it adds 1D before the 1st index
# if  axis = 2 : it adds 1D before the 2nd index

x = np.arange(18).reshape(3,2,3)
print(x)
print(x.shape)
print(x.ndim)
print("====================================")
# axis = o

y = np.expand_dims(x,axis=0)
print(y)
print(y.shape)
print(y.ndim)
print("====================================")
# axis = 1

z = np.expand_dims(x,axis=1)
print(z)
print(z.shape)
print(z.ndim)

print("====================================")

# axis = 2

X = np.expand_dims(x,axis=2)
print(X)
print(X.shape)
print(X.ndim)

print("====================================")

# np.squeeze
"""Removes ALL 1D (single dimension) entries in the array"""

a = np.arange(12).reshape(1,4,3)
print(a)
print(a.ndim)
print(a.shape)

print("====================================")

b = np.squeeze(a)
print(b)
print(b.ndim)
print(b.shape)

print("====================================")

c = np.arange(12).reshape(1,1,4,1,3)
print(c)
print(c.ndim)
print(c.shape)

print("====================================")

d= np.squeeze(c)
print(d)
print(d.ndim)
print(d.shape)

print("====================================")
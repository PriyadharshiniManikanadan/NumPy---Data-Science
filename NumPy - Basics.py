# Axis
""" Axis = 0, Axis  = 1 """

import numpy as np

a = [[1,2],
     [2,3],
     [3,4]]
sum_ans = np.sum(a,axis=0)
print(sum_ans)


a = [[1,2],
     [2,3],
     [3,4]]
sum_ans = np.sum(a,axis=1)
print(sum_ans)


print("=" * 100)

# Dimensions

a = [[1,2],
     [2,3],
     [3,4]]

print("Dimension ", np.ndim(a))
SumAnswer= (np.sum(a,axis = 0))
print(SumAnswer)
print(SumAnswer.ndim)

print("Shape",np.shape(a))

b =[ [[1,2],
     [2,3],
     [3,4]] ]

print(np.ndim(b))
SumAns = (np.sum(b,axis = 1))
print(SumAns)
print(SumAns.ndim)

print("Shape",np.shape(b))

# if axis is not given

print(np.sum(a)) # it adds all the elements in the array

print("=" * 100)

# Index:

"""Index Starts from 0"""

A = [ [ 100,10,30],
      [50,60,40],
      [80,90,100] ]

print(np.shape(A))

print(A[2][1]) # row - 2 , col - 1
print(A[-2])
print(A[0])
print(A[-2]  [-1])

print("=" * 100)

# 3 Dimensions

""" 
We can not able to explain how it collapsing the rows and columns"""

Train = [   [[1,2],[2,3],[3,4]],
            [[2,2],[3,3],[4,2]]   ]

# Two compartments
# 3 Seats
# 2 Passengers in each seat

import numpy as np

print("Dim",np.ndim(Train))
print("shape", np.shape(Train))


""" Shape result explaination"""

# 2  means it contains --  Two 2D arrays
# 3 means 3 Rows
# 2 means 2 columns

A = [   [[1,2],[2,3],[3,4]],
        [[2,2],[3,3],[4,2]]   ]

print("Axis 0")

""" between the compartment of  3D array index wise"""

SumAns = np.sum(A,axis=0)
print(SumAns)



print("Axis 1")

""" Top to bottom of  2D array
First completes the 1st compartment, then
Second completes the 2nd compartment
"""
SumAns = np.sum(A,axis = 1)
print(SumAns)

print("Axis 2")

"""Left to Right of  2D array
First completes the 1st compartment, then
Second completes the 2nd compartment
"""



SumAns = np.sum(A,axis = 2)
print(SumAns)


""" If the dimension is 3 we can sum only till axis = 0, axis = 1, axis = 2  === (3-1)  """

print("=" * 100)


# 4 Dimensions

A = [ [  [[1,2],[2,3],[3,4]],
        [[2,2],[3,3],[4,2]]   ] ]

print("4D Shape example", np.shape(A))

# [  [[1,2],[2,3],[3,4]],             # Has 1 - 3D
#         [[2,2],[3,3],[4,2]]   ]
#
#
# [[1,2],[2,3],[3,4]],                # 2 - 2D
#         [[2,2],[3,3],[4,2]]
#
#
# [1,2],    #3 rows and 2 col
# [2,3],
# [3,4]

print("=" * 100)

# Range [ start, stop, step ]


# Normal range function in python :

for i in range(0,5,1):
    print(i)

for i in range(0,5,2):
    print(i)

    print("=" * 100)

#  Normal range function in NumPy

for i in np.arange(0,5):
    print(i)

a= [[[1, 2], [2, 3], [3, 4]],
     [[2, 2], [3, 3], [4, 2]]]

for a in np.arange(0,5):
    print(i)

# what we can do using arange :

range = np.arange(0,12)
print(range)

# np.arange in RESHAPE :

""" changing data into Matrix  """

matrix = np.arange(0,12).reshape(4,3 ) # change data into 4 rows 3 columns Matrix
print(matrix)

matrix = np.arange(0,12).reshape(3,4) # change data into 3 rows 4 columns Matrix
print(matrix)


matrix = np.arange(0,9).reshape(3,3)
print(matrix)

print("=" * 100)

matrix = np.arange(1,17).reshape(4,2,2)
print(matrix)

print("=" * 100)

Sum_matrix = np.sum(matrix,axis=0)
print(Sum_matrix)

print("=" * 100)

Sum_matrix = np.sum(matrix,axis=1)
print(Sum_matrix)

print("=" * 100)

Sum_matrix = np.sum(matrix,axis=2)
print(Sum_matrix)

print("=" * 100)

# 4 D

matrix = np.arange(1,17).reshape(1,4,2,2)
print(matrix)


print("=" * 100)

import numpy as np
A = [   [[1,2],[2,3],[3,4]],
        [[2,2],[3,3],[4,2]]   ]

arr = np.sum(A,axis=0)
print(arr)

arr = np.sum(A,axis=1)
print(arr)

arr = np.sum(A,axis=2)
print(arr)

print("=" * 100)

A = [  [[1,10],[2,20],[3,30]], [[4,40],[5,50],[6,60]], [[7,70],[8,80],[9,90]]  ]

"""Scalar values does not have any shapes"""

print("len(A) is" ,len(A))

print("np.array(A)", np.array(A))

print("np.shape(A)",np.shape(A))

print("A[0] is ",A[0])

print("A[0][0] is", A[0][0])

print("A[0][0][0] is", A[0][0][0])

print("np.shape(A[0]) is", np.shape(A[0]))

print("np.shape(A[0][0]) is", np.shape(A[0][0]))

print("np.shape(A[0][0][0]) is", np.shape(A[0][0][0]))

print("A[2][1][2] is",A[1][1][1])

print("np.shape(A[1][1][1] is",np.shape(A[1][1][1]))

print("=" * 100)

# Accessing and testing the data type of an object in list

List = [1,2,3,4,5,6]
print(len(List))
print("List[2] is : ", List[2])
print(type(List[2]))

print("List[2:5] is : ",List[2:5])
print(type(List[2:5]))

print("=" * 100)

# Accessing and testing the data type of an object in ndarray

import numpy as np

a = np.arange(2,10).reshape(4,2)
print(a)

print("a[1]:",a[1])
print(type(a[1]))

print("a[0,0]:", a[0,0])
print(type(a[0,0]))

print("=" * 100)

print("based on how many dimensions are there - np.ndim(a):",np.ndim(a))      # based on how many dimensions are there

print("in ndarray length is based on the vectors - len(a):",len(a))       # in ndarray length is based on the vectors

print("=" * 100)

# In 3D

A = np.arange(28).reshape(2,2,7)
print(A)
print("In 3Dnp.ndim(A):",np.ndim(A))
print("In 3D len(A):",len(A))

print("=" * 100)

A = np.arange(28).reshape(1,2,2,7)
print(A)
print("np.ndim(A):",np.ndim(A))
print("In 4D len(A):",len(A))

# linspace

import numpy as np
arr = np.arange(12)
print(arr)

array = np.arange(10,20,2)
print(array)


array = np.linspace(10,20,6)  # Returns only float
print("linspace:",array)

import numpy as np
arr = np.array([11,22,33,44,55])
print(arr)
print(type(arr))
x = arr[np.array([2,3,4,0])]
print(x)
print(type(x))

print("="*100)
# Basic Operators in ndarray
print(" Basic Operators in ndarray")

# add

import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print("add:",a+1)

# Sub

b = np.array([1,2,3,4,5])
print("sub:",b-2)

# Multiply

c = np.array([1,2,3,4,5])
print("multiply:",c*10)

# square root

d = np.array([1,2,3,4,5])
print("Square root:", d**10)

# modify existing array
ab = np.array([2,3,4,5,6])
ab *= 2
print("double each element :",ab)

# Transpose of an array

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nOriginal array:\n", x)
print("\nTranspose of arrayx:\n", x.transpose())

print("="*100)

# Multiply two lists == not possible
# so , we convert list into numpy array to multiply both

# list1 = [2,3,4,5,6]
# list2 = [2,3,4,5,6]
# print(list1*list2)

import numpy as np

arr1 = np.array([2,3,4,5,6])
arr2 = np.array([2,3,4,5,6])
print("Multiplication b/w 2 np array is possible, but not two lists:", arr1*arr2)

print("="*100)

# creating two array in 2 dimensions

matrix1 = np.array([[2,3,4,5,6],[3,4,5,6,7]])

print(matrix1)

matrix2 = np.array([[6,5,4,3,2],[7,6,5,4,3]])

print(matrix2)

print("="*100)

# adding 5 to matrix 1

new_matrix1 = (matrix1 + 5)
print("adding 5 to matrix 1:",new_matrix1)

print("="*100)

# sum of matrix2

sum_matrix2 = matrix2.sum()
print("sum of matrix2:",sum_matrix2)

print("="*100)

# Adding 2 matrix

add_matrix = matrix1 + matrix2
print("Adding 2 matrix:",add_matrix)



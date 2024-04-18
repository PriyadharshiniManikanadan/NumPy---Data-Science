# Broadcasting
""" Treats array with different shapes during arithmetic operations
    The smaller array "Broadcast" across the larger array, so that they have a compatible shapes"""

import numpy as np
a = np.array([1.0,2.0,3.0])
b = np.array([2.0,2.0,2.0])
c = (a*b)
print(c)

# print("======================================")

# print("Broadcast with different shapes")
# a = np.array([1.0,2.0])
# b = np.array([2.0,2.0,2.0])
# c = (a*b)
# print(c)
#operands could not be broadcast together with shapes (2,) (3,)

# print("======================================")

print("when an array & * scalar * value is combined in an operation")

a = np.array([1.0,2.0,3.0])
b = np.array([2.0])    # b is a scalar ,, this unneccessary increase the memory usage for the code,
                       # rather use single value.
c = (a*b)
print(c)

# the value b get duplicated in order to strech with array a like ([2.0,2.0,2.0])

# print("======================================")

print("when an array & values are combined in an operation")

a = np.array([1.0,2.0,3.0])
b = 2.0    # b is a value
c = (a*b)
print(c)

# any arrays with any dimensions can be broadcasted with values...
# This example(array & value) is more efficient than before example (array & scalar) because,
# "Broadcasting moves less memory around during the multiplication ( b is a value rather than array)"

print("======================================")

# Rules  of  Broadcasting For 2D array

# 1. They are equal (shapes should be equal)  or
# 2. One of them should be equal.

# Either
"""  A array is  (4,3)
     B array is (4,1) or (1,3) """

# Example :

import numpy as np
X = np.array([[1,2,3],[2,3,4],[4,5,6],[5,6,7]])
print(X)
print(X.ndim)
print(X.shape)
Y = np.array([[2,0,3],[2,5,1],[2,1,2],[3,2,1]])
print(Y)
print(Y.ndim)
print(Y.shape)

XY = (X*Y)
print(X*Y)
print(XY.ndim)
print(XY.shape)

print("======================================")

x = np.array([[1,2,3],[2,3,4],[4,5,6],[5,6,7]])
print(x)
print(x.shape)
print(x.ndim)

print("======================================")

y = np.array([[2.0,2.0,3.0]])
Y1 = np.array([[1],[2],[3],[4]])

print(y)
print(Y1)
print(y.shape)
print(y.ndim)
print(Y1.shape)
print(Y1.ndim)

print("======================================")

C = (x*y) # EAch row of array x is multiplied by corresponding row of array y
print(C)
print(C.ndim)
print(C.shape)


print("======================================")

# Rules of Broadcasting for more than 2D array -- 7 rules

# Rule No 1
print("Rule No 1\n")
# 2D array
# 1D array (It is value)
A = np.array([[1,2,3],[0,1,2],[2,0,1]])
print(A)
print(A.ndim)
print(A.shape)
B = 5
print(B)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 2
print("Rule No 2\n")
# 2d array
# 1D array (Group of scalars)
import numpy as np
A = np.array([[1,2,3],[0,1,2],[2,0,1],[3,0,1]])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([1,2,3])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 3
print("Rule No 3\n")
# ndim & column must be the same for both arrays
import numpy as np
A = np.array([[1,2,3],[0,1,2],[2,0,1],[3,0,1]])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([[2,2,2]])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 4
print("Rule No 4\n")
# ndim are different
# column must be the same for both arrays
import numpy as np
A = np.array([[[[1,2,3],[0,1,2],[2,0,1],[3,0,1]]]])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([[2,2,2]])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 5
print("Rule No 5\n")
# ndim are same for both arrays
# Row & Column - diagonal must be 1

import numpy as np
A = np.array([[1,2,3]])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([[2],
              [1],
              [2],
              [5],
              [2]])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 6
print("Rule No 6\n")
# ndim are different
# Column & Row - diagonal must be 1
import numpy as np
A = np.array([[[[1],[2],[3],[4]],
               [[0],[2],[3],[4]],
               [[2],[2],[3],[4]]] ])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([[[2,2,2,2]]])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)

print("======================================")

# Rule No 7
print("Rule No 7\n")
# Rows must be same
# either A or B column must be 1
import numpy as np
A = np.array([[[1,2,3],[2,3,2]]])
print(A)
print(A.ndim)
print(A.shape)
B = np.array([[1],[2]])
print(B)
print(B.ndim)
print(B.shape)
C = (A*B)
print(C)
print(C.ndim)
print(C.shape)
print("======================================")
# np.newaxis:
   # if 2 arrays cannot be broadcasted, because of mismatching shape --- we use np.newaxis
   # Increases 1 dimension either in Row or Column wise


import numpy as np
a = np.array([1,2,3,4],dtype=int)
print(a)
print(a.shape)
print("======================================")
b = np.array([5,6,7],dtype=int)
print(b)
print(b.shape)

# c = (a*b)
# print(c)  # Broadcating is NOT POSSIBLE, But now see below

print("======================================")
a1 = a[:,np.newaxis]  # column wise increasing 1 dimension, after comma
print(a1)
print(np.shape(a1))
print(np.ndim(a1))
print("======================================")
a2 = b[np.newaxis,:]  # Row wise increasing 1 dimension, before comma
print(a2)
print(np.shape(a2))
print(np.ndim(a2))

# Now a1 & a2 can be broadcasted

ab = (a1*a2)
print(ab)
print(np.shape(ab))
print(np.ndim(ab))





















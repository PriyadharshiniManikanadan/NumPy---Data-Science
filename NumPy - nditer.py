# np.nditer

"""np.nditer method TRAVERSE/Tavel on numpy array"""

# Parameters of np.nditer- 9
"""
 1. op
 2. flags  -  13 values
 3. op_flags  - 12 values
 4. op_dtype  - 6 values
 5. op_axes
 6. order  - 4 values
 7. casting  - 5 values
 8. itershape
 9. buffersize  - 13 values
 """

import numpy as np
a = np.arange(0,30,5)
print(a)
print("=========================================================")
a = a.reshape(3,2)  # Row major by default
print(a)

# for x in np.nditer(op=a,):  # (Apply np.nditer to find how the array values are stored in memory)
#     # print(x)
#     print(x,end=" ")

print("=========================================================")

print("'C' - Row major")
for x in np.nditer(a,order = "C"):
    # print(x)
    print(x,end=" ")

print("=========================================================")

print("'F' - Column major")
for x in np.nditer(a,order = "F"):
    # print(x)
    print(x,end=" ")

print("=========================================================")

print("without order - default it take Row major")
for x in np.nditer(a):
    # print(x)
    print(x,end=" ")

print("=========================================================")
print("'K' - Row major")
for x in np.nditer(a,order = "K"):   # Simillar to Row major
    # print(x)
    print(x,end=" ")

print("=========================================================")
print("'A' - Row major")
for x in np.nditer(a,order = "A"):   # Simillar to Row major
    # print(x)
    print(x,end=" ")

print("=========================================================")

# Tranpose  -- check the result

"""If Tranpose occurs the memory layout (output) will not change, it will be constant"""

import numpy as np
a = np.arange(0,30,5)
print(a)
print("=========================================================")
a = a.reshape(3,2)  # Row major by default
print(a)
print("=========================================================")
print("'C' - Row major")
for x in np.nditer(a,order = "C"):
    # print(x)
    print(x,end=" ")
print("=========================================================")
print(a)
print("=========================================================")
b = a.T
print(b)
print(id(b))
print("=========================================================")

for items in np.nditer(b):
    print(items,end=" ")

print("=============================================================\n")

import numpy as np
a = np.arange(0,60,5)
print(a)
print("=========================================================\n")
a = a.reshape(4,3)  # Row major by default
print(a)
print(a.shape)
print(id(a))

print("=========================================================\n")

for items in np.nditer(a):  # Takes column major 'C'
  print(items,end=" ")

print("=========================================================\n")

b = a.T
print(b)
print(b.shape)
print(id(b))
#
print("=========================================================\n")

for items in np.nditer(b):  # Takes column major 'F'
  print(items,end=" ")
#
print("=========================================================\n")
#
c = b.copy()
print(c) # same as like Transpose data
#
for items in np.nditer(c):   # After copying the data -- Takes default - Row major 'C', since it takes different memory location,
  print(items,end=" ")

print("=========================================================\n")

for items in np.nditer(c,order='F'):   # After copying the data -- Takes default - Row major 'C', since it takes different memory location,
  print(items,end=" ")

print("=========================================================\n")

# Modifying array values - op_flags

print("Modifying array values - op_flags")
print("\n")
import numpy as np
a = np.arange(0,60,5)
print(a)
print("=========================================================\n")

for items in np.nditer(op=a,op_flags=['readwrite']):
# for items in np.nditer(op=a):
    items[...]=2*items    # Syntax
    print(items,end=" ")

print("=========================================================\n")

# External_loop value is part of flag parameter in nditer :

print("External_loop value is part of flag parameter in nditer")

# Converts the 2D & nd array into 1D array:
x = np.arange(0,60,5).reshape(3,4)
print(x)

for items in np.nditer(op=x,flags=['external_loop']):  # Default Row Major = 'C'
    print(items)
print("=========================================================\n")
# Tranpose the Row and Column if the order is given as F - column major

print("Tranpose the Row and Column if the order is given as F - column major")

x = np.arange(0,60,5).reshape(3,4)
print(x)

for items in np.nditer(op=x,flags=['external_loop'],order='F'):
    print(items)
print("=========================================================\n")
# Make 1D array if the order is C

print("Make 1D array if the order is C")
x = np.arange(0,60,5).reshape(3,4)
print(x)

for items in np.nditer(op=x,flags=['external_loop'],order='C'):
    print(items)

print("=========================================================\n")

# Example

import numpy as np
Y = np.arange(36).reshape([3,3,4])
print(Y)
print(np.ndim(Y))
print(np.shape(Y))
print(len(Y))
print("=========================================================\n")

for x in np.nditer(op=Y,flags=['external_loop'],order='C'):
    print(x)
print(np.ndim(x))
print(np.shape(x))
print(len(x))
print("=========================================================\n")

for x in np.nditer(op=Y, flags=['external_loop'], order='F'):
        print(x)
print(np.ndim(x))
print(np.shape(x))
print(len(x))

print("=========================================================\n")


# BROADCASTING ITERATION :

# Example
print("Array 1")
import numpy as np
y = np.arange(12).reshape([3,4])
print(y)
print("Array 2")
z = np.array([1,2,3,4],dtype=int)
print(z)

print("=========================================================\n")

for a,b in np.nditer([y,z],order='C'):
    print(a,b),
#
print("=========================================================\n")

for a,b in np.nditer([y,z],order='F'):
    print(a,b),

print("=========================================================\n")

print("Array 1")
import numpy as np
y = np.arange(12).reshape([3,4])
print(y)
print("Array 2")
z = np.array([1,2,3,4],dtype=int)
print(z)

print("Modify the 2 arrays using operations")

for a,b in np.nditer([y,z],order='C'):
    print(a+b,end=" "),
print("=========================================================\n")
# import math
# print(math.)

a = np.array([5,5,5,5],dtype=int)
print(a)
print("=========================================================\n")
for a,b,c in np.nditer([y,z,a],order='C'):
    print(a+b+c,end=" "),

print("=========================================================\n")

print("With comma & without comma")

for a,b,c in np.nditer([y,z,a],order='C'):
    A = ('%d:%d:%d' %(a,b,c)),
    print(A)
    print(type(A))
    # B = ('%d:%d:%d' %(a,b,c))
    # print(B)
    # print(type(B))
print("=========================================================\n")

# Flat - attribute
# Gives iterator object
#
import numpy as np
a = np.arange(6).reshape(2,3)
print(a)

fl=iter(a)
print(fl)

b = a.flat
print(b)
print(type(b))
#
# Changing from 2D to 1D using external_loop in flags in nd.nditer

for i in np.nditer(op=a,order='C',flags=['external_loop']):
    print(i)
print("====================================")

# In 5 types 'Flat' can return an iterator object

print(next(b))
print(next(b))
print(next(b))
print(next(b))

print("====================================")

print(b[:])
print(b[0:3])
print(b[-1:])


print("====================================")

# for i in b:
#     print(i)

print("====================================")

# for i in enumerate(b):
#     print(i)

print("====================================")

print(list(b))

print("====================================")

x = np.arange(5,65,5).reshape(4,3)
print(x)

y = x.flat   # this is attribute
print(y)

x.flat[0]=500
print(x)  # impacts the original array

print("====================================")

# np.flatten() - is a method
# Gives 1D array

A = np.arange(36).reshape(3,3,4)
print(A)
print(A.ndim)
print(A.shape)
print(A.dtype)
print(A.nbytes)
print(id(A))

print("====================================")

B = A.flatten(order='F')  # changes the 3D to 1D
print(B)
print(B.ndim)
print(B.shape)
print(B.dtype)
print(B.nbytes)
print(id(A))

print("====================================")

print(B[2])
B[2]=200
print(B)

print("====================================")

print(A)   # it does not change in original array
print(id(A))

print("====================================")

print(B)
c = print(B[2:5]) # slicing possible in flatten method

# Reshape : using reshape we can make array to 1D

S = np.arange(16).reshape(4,4)
print(S)
X = S.reshape(-1)
print(X) # Results in 1D as vector

print("====================================")

# Ravel -- simillar as flat

array = np.arange(16).reshape(4,4)
print(array)
print(id(array))

print("====================================")

X = array.ravel
print(X)
print(type(X))
print(id(X))

print("====================================")

X = array
print(X)

print("====================================")

X[0]=100
print(X)

print("====================================")

print(array)

print("====================================")


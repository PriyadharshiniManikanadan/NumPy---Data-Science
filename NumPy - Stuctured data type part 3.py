# np.fromiter

"""Purpose of fromiter ----- is to iterator an object, and to take required num of items by using Count keyword"""

print("np.fromiter\n")

import numpy as np

a = np.arange(5)
print(a)
print(type(a))

a = np.arange(5)
it = iter(a)
print(it)

# b = np.fromiter(it,dtype=float,count=2)
# print(b)
# print(type(b))

b = np.fromiter(it,float,3)
print(b)

c = np.fromiter(np.arange(12),dtype=object,count=8)
print(c)

print("="*100)

# NumPy - Array from Numerical Ranges

# 4 paramaters ---- start, stop, step, dtype

a = np.arange(start=0,stop=12,step=2,dtype=float)
print(a)

a = np.arange(start=0,stop=12,step=2,dtype=float).reshape(3,2)
print(a)

print("="*100)

## np.full ()

# parameters - shape & fill values

student = np.full((5,5),50)
print(student)

print("="*100)

student = np.full((4,5,5),5,dtype=str)
print(student)

print("="*100)

students = np.full((4,3),'present',dtype=object)
print(students)
students[0][2]='Fail'
print(students)

print("="*100)

"""will be used in Broadcasting method """

import numpy as np
passmark = np.full((4),'Pass',dtype= object)
print(passmark)

internal = np.full((4),20,dtype=int)
print(internal)


print("="*100)

student = np.full((3,2),'Present',dtype='S2')
print(student)

print("="*100)

student = np.full((3,2),'Present',dtype='S4')
print(student)

# Random in Python

import random
print(random.random())

"""Give random values between o and 1"""

print(random.randint(5,10))

"""Give random values between the given start and stop values
python it is inclusive"""



# In NumPy

"""Give random values between the given start and stop values
NumPy it is exclusive for last mentioned value"""

# np.random

import numpy as np
x = np.random.rand(4,2)
print("rand:",x)

print("="*100)

x1=np.random.randint(low=0,high=12,size=(3,3))
print(x1)

print("="*100)

x1=np.random.randint(12,size=(3,3))
print(x1)

print("="*100)

x1=np.random.randint(2,10,size=(3,3))
print(x1)

print("="*100)

# Automatically it takes from 0-4
x1=np.random.randint(5,size=(3,3))
print(x1)

print("="*100)

# what happens if i missed high paramater ?

# it considers as ===   ( 0,low,size - as parameter )

x1=np.random.randint(low=5,size=(3,3))
print("Missing high parameter:\n", x1)

# OR

x1=np.random.randint(low=5,high=None,size=(3,3))
print(x1)

print("="*100)

x1=np.random.randint(low=0,high=2,size=(3,3))
print(x1)

print("="*100)

# np. identity matrix:

""" In Broadcasting it is used  - 
            The effect of multiplying the given matrix bt identity matrix
            results in -- Unchanged Matrix  """

import numpy as np
A = np.identity(3)
print(A)     # result always be in float

# np.repeat() method

"""Each scalar value is repeated"""

import numpy as np

a = np.array([1,2,3])
print(a)
b = np.repeat(a,5)
print(b)

print("="*100)

# To check the order how it is stored based on Row major & Column Major

list =[[1,2,3],[3,2,1]]  # nested list
print(list)
print(type(list))

a = np.asarray(list,order="F")
print(a)
print(type(a))
print("="*100)

order = np.nditer(a,order = "F")
print(order)
print(type(order))

print("="*100)

for i in order:
    print(i)

print("="*100)

order = np.nditer(a,order = "C")
print(order)
for i in order:
    print(i)

print("="*100)

# Reshape with parameters:

import numpy as np
a = np.arange(12)
print(a)
print("="*100)
xx = a.reshape((4,3), order="C")
print(xx)
print("="*100)
yy = a.reshape((4,3), order="F")
print(yy)
print("="*100)











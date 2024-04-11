# np.asarray
import matplotlib.pyplot as plt

# Changing list to nd array

print("Changing list to asarray")
print("="*100)

import numpy as np
a = [1,2,3,4,5]
print(a*5)   # cannot multipy list through python. it will replicate the list 5 times.
print(type(a))


b = np.asarray(a)
print(b*5)  # when list is converted into nd array, then we can able to multiply each items.
print(type(b))

# now we can use any scientific calculations for nd array

# Example

print(np.log(b))
print(np.sin(b))

print("="*100)

# Changing nd array to asarray

print("Changing nd array to asarray below")
print("="*100)

a = np.array([1,2,3])
print(type(a))

b = np.asarray(a)
print(type(b))
print(a is b)

if type(a) == type(b):
    print("Yes both are same type")
else:
    print("No both are not same")

print(np.asarray(a)is a)

print("="*100)

# Difference b/w np.array(), np.asarray(), np.asanyarray()
print("# Difference b/w np.array(), np.asarray(), np.asanyarray()")
print("="*100)

a = np.array([1,2,3,4,5])    # Original array

print("Original array:",a)
print("Memory space no:",id(a))

print("="*100)

b = np.array(a)
b[1]=100
print("np.array(a):",b)
print("Memory space no:",id(b))

# Opens up a new memory space,
# Make a copy of original array
# if we  do any changes in b
# It will not affect the original array a

print("="*100)

c = np.asarray(a)
c[2]=200
print(a)
print("np.asarray(a):",c)
print("Memory space no:",id(c))

# Still use the original memory space,
# Make a copy of original array
# if we  do any changes in c
# It will affect the original array a

print("="*100)

d =  np.asanyarray(a)
d[3]=300
print(a)
print("np.asanyarray(a):",d)
print("Memory space no:",id(d))


# Still use the original memory space,
# if we  do any changes in b
# It not affect the original array a

print("="*100)

# Now check the original array a

print("Now the original array a is changed based on asarray() & asanyarray():",a)

# But one Condition for the above is:

import numpy as np
a = np.array([1,2,3], dtype=np.float32)
print(np.asarray(a,dtype=np.float32)is a)   # Should have same data type
print(a)

a = np.array([1,2,3],dtype=np.float32)
print(np.asarray(a,dtype=np.int16)is a)
print(a)

a = np.array([1,2,3],dtype=np.float32)
print(np.asarray(a,dtype=np.float64)is a)
print(a)

print("="*100)

print("Example:")

import numpy as np

a = np.array([1,2,3],dtype=np.int16)

b = np.asarray(a,dtype=np.int32)
b[1]=100

print("original array:",a)
print("="*100)

print("np.asarray:",b)
print("="*100)

print("if the data types are different, changes in b will not affect a")
print("Original array:",a)
print("="*100)

## Just recollecting for further topics

# Super class  & Sub Class

print(issubclass(np.recarray,np.ndarray))

# We can change any sequence of data into ndarray

"""
Lists
lists of lists
list of tuples
Tuples
Tuples of Tuples
Tuples of List
ndarray"""


# one of this example

import numpy as np

a = ( [ "Mani", "Priya", "Utsav", "Inbav"], [ "Marks-10","Marks-20","Marks-30", "Marks-40"] )
print(a)
print(type(a))

print("="*100)
b = np.asarray(a,dtype=str,order="F")
print(b)
print(b.ndim)
print(b.shape)
print(b.reshape(4,2))
print(type(b))


print("="*100)

# Changing nd array to np.frombuffer

import numpy as np

s = b"Studying NumPy"

# dtype must be a multiple of element size

a = np.frombuffer(s,dtype='S1',offset=0,count=-1)
print(a)
print(len(a))
print(a.shape)
print(a.dtype)
print(a.ndim)
b = a.reshape(7,2)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)
print(b.nbytes)
print(b.dtype)
print(type(b))


print("="*100)

# Example 1

# s = b"Studying NumPy"
#
# # Buffer size must be a multiple of element size
#
# a = np.frombuffer(s,dtype='S3',offset=0,count=-1)
# print(a)

# Example 2

x = b"Studying NumPy"

# Buffer size must be a multiple of element size

A = np.frombuffer(x,dtype='S4',offset=0,count=3)
print(A)

print("="*100)

# From the Result - how to remove the prefix b from each bytes



Y = np.frombuffer(b"Iam learning NumPy",dtype='S1',offset=0,count=-1)
print(Y)
print(type(Y))

b = list(Y)
print(b)
print(type(b))
print(len(b))

emptylist = []

for item in b:
    item = str(item)
    # print(type(item))
    # print(len(item))
    emptylist.append(item[2])

c = "".join(emptylist)
print(c)


print("="*100)



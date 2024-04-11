# Normal basic data type
import PIL
# Example

import numpy as np
from PIL import Image

a = np.array([[1,2,3,4,5]],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(type(a))
print(a.dtype)

print("="*100)


# Structured data type

""" Structured data will been declared and data will be supplied inside the array object """

""" 
Method / Formula for structued data type is below

1. FIELD NAME AND THEIR CORRESPONDING DATA TYPE SHOULD BE DECLARED

2. Must be in Tuple"""


# Example

# Mention the dtype first
# Create an array object next


dt = np.dtype([('age',np.int8), ('Name',np.str_),('Population',np.int32)])
A = np.array([(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)],dtype=dt)
print("('Name',np.str_):---------------",A)

dt = np.dtype([('age',np.int8), ('Name','S15'),('Population',np.int32)])
A = np.array([(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)],dtype=dt)
print("('Name','S15')------------",A)

# dt = np.dtype([('age',np.int8), ('Name','S15'),('Population',np.int8)])
# A = np.array([(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)],dtype=dt)
# print("Population',np.int8)---------------",A)

dt = np.dtype([('age',np.int8), ('Name','S15'),('Population',np.int16)])
A = np.array([(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)],dtype=dt)
print("('Population',np.int16)------------",A)

print("="*100)

# There are 2 ways to write data type

# way 1

import numpy as np

student = np.dtype([('Name',np.str_),('Age',np.int8),('Marks',np.float_)])
print(student)

# Way 2

Student = np.dtype([('Name','S15'),('Age','i1'),('Marks','f4')])
print(Student)

print("="*100)

# To Access the index

dt = np.dtype([('age',np.int8), ('Name','S15'),('Population',np.int16)])
A = np.array([(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)],dtype=dt)
print(A)

print(A[1])
print(A[2][1])
print(A['age'])
A['age'][0] = 35
print(A)
print(A.shape)

dt = np.dtype([('age','i1'),('Name','S15'),('Population','i2')])
B = np.array([[(34,'Manikandan',100),(31,'Priya',200),(8,'Utsav',300)]],dtype=dt)
print(len(B))


Student = np.dtype([('Name','S15'),('Age','i1'),('Marks','f4')])
print(Student)
X = np.array([('Chezhiyan',20,100),('Ezhil',25,150),('Iniya',18,80)])
print(X)

print("="*100)

# Object supports the string
Student = np.dtype([('Name','object'),('Age','object'),('Marks','object')])
print(Student)
X = np.array([('Chezhiyan',20,100),('Ezhil',25,150),('Iniya',18,80)],dtype=Student)
print(X)
print(type(X))
y = ((X[0][1]))
print("y:",y)
print(type(y))
print(y*100)
y = ((X[0][0]))
print(y.upper())
print(type(y))



print("="*100)

# Unicode ( for different languages)

Student = np.dtype([('Name','U15'),('Age','i1'),('Marks','f4')])
print(Student)
X = np.array([('Chezhiyan',20,100),('Ezhil',25,150),('Iniya',18,80)])
print(X)

print("="*100)

# Attributes of NumPy Array

# 1. shape

a = np.array([[1,2,3],[3,2,1]])
print(a)
print(a.shape)

# Reshape - want to change the shape into 3,2
# After reshape

a.shape = (3,2)
print("\nReshape - want to change the shape from (2,3) into (3,2) :\n", a)

# After reshaping use index

Student = np.dtype([('Name','S15'),('Age','i1'),('Marks','f4')])
print(Student)
a = np.array([('Chezhiyan',20,100),('Ezhil',25,150),('Iniya',18,80),('Mani',20,75),('Iniya',18,80),('Mani',20,75)],dtype=Student)
print("----------------------------")
print(a)
print(a.shape)
print("----------------------------")
print(a['Name'])
print("----------------------------")
print(a.ndim)
print("---------------------------")
print(a.shape)
print("---------------------------")
a.shape = (3,2)
print(a)
print("---------------------------")
print(a['Name'])

print("="*100)

# 2nd Method of creating nd array

# np.empty

import numpy as np
dt = np.dtype('i2')
a = np.empty(shape=(3,3),dtype=dt,order='F')
print(a)

print("="*100)

np.put(a,[0,1,2],[100,200,300])
print("put:",a)

print("="*100)

dt = np.dtype('i1')
b = np.empty(shape=(3,4),dtype=dt,order='C')
print(a)

dt = np.dtype('i1')
c = np.empty(shape=(3,4),dtype=dt,order='F')
print(a)

print("="*100)

# int values

a = np.empty(shape=(3,4),dtype=int,order='C')
print("int:",a)

print("="*100)

# Float values

a = np.empty(shape=(3,4),dtype=float,order='C')
print("float:",a)

print("="*100)

# String Values
a = np.empty(shape=(3,4),dtype=str,order='C')
print("String:",a)

print("="*100)

# Boolean values

a = np.empty(shape=(3,4),dtype=bool,order='C')
print("bool:",a)

print("="*100)

# Complex values

a = np.empty(shape=(3,4),dtype=complex,order='C')
print("complex:",a)

print("="*100)

# Object dtype

a = np.empty(shape=(3,4),dtype=object,order='C')
print("object:",a)

print("="*100)

# None values

a = np.empty(shape=(3,4),dtype=None,order='C')
print("None:",a)

print("="*100)

# bytes values

a = np.empty(shape=(3,4),dtype=bytes,order='C')
print("bytes:",a)

print("="*100)

# bytearray values

a = np.empty(shape=(3,4),dtype=bytearray,order='C')
print("bytearray:",a)

print("="*100)

# Create nd array with empty()

import numpy as np

A = np.empty(shape=(4,3),dtype=int,order='C')
print("\nnp.empty:\n",A)

# initializing by providing values

A[1] = (1,2,3)
print(A)

print("="*100)

# Initialize array with Bytes  values

AB = np.array(object = np.arange(12).reshape(3,4),dtype=bytes,order='F')
print(AB)

print("="*100)

AB = np.array(object = np.arange(12).reshape(3,4),dtype=bytearray,order='F')
print(AB)
print(type(AB))
x = AB[0][2]
print(x)
print(type(x))

print("="*100)

# np.zeros method
# output is always in zero

np_zeros = np.zeros(shape=(4,3),dtype=int,order='F')
print(np_zeros)

print("="*100)

# np.ones method
# output is always in float
dt = np.dtype(np.int8)
np_ones = np.ones(shape=(4,3),dtype=dt)
print(np_ones)
print(type(np_ones))
print(np_ones.size)
print(np_ones.itemsize)
print(np_ones.nbytes)
print(np_ones.shape)

print("="*100)
#
# # print(PIL.__version__)
# #
# # import PIL
# # import numpy as np
# #
# # img = PIL.open("C:\\Users\\priya\\Desktop\\priya.jpg").convert("L")
# # imgarr = np.array(img)
#
# print("="*100)
#
# import PIL
# import numpy as np
# from PIL import image
# from numpy import asarray
# image = Image.open("C:\\Users\\priya\\Desktop\\priya.jpg")
# print(image.format)
# print(image.size)
# print(image.mode)
#
# npdata = asarray(image)
# print(npdata)
# print(np.ndim(image))
# print(np.shape(image))

print("="*100)

# np.frombuffer method to create nd array

import numpy as np
s = b"ABCDEFG"
array = np.frombuffer(s,dtype='S1',offset=5,count=2)
print(array)
print(len(array))
print(array.ndim)
print(array.size)
print(array.itemsize)
print(array.nbytes)
print(array.shape)

print("="*100)

s = b"ABCDEFG"
array = np.frombuffer(s,dtype='S1',offset=0,count=-1)
print(array)
print(len(array))
print(array.ndim)
print(array.size)
print(array.itemsize)
print(array.nbytes)
print(array.shape)

print("="*100)

# np.asarray() method to create nd array

a = [1,2]
arr = np.asarray(a)
print(arr)
print(type(arr))

# np.asfarray - converting input to a floating point nd array

import numpy as np
arr = np.arange(12).reshape(4,3)
print(arr)
print(type(arr))
print(arr.dtype)


b = np.asfarray(arr)
print(b)
print(b.dtype)

# np.asarray_chkfinite() -
# checks the input is infinite / nan    or
# convert the input into an ndarray then check the infs/nans

import numpy as np

a = [1,2,np.nan,np.inf]
print(a)

# if a[2] == np.nam:
#    print("Yes it is nan")

                           # OR

try:
    np.asarray_chkfinite(a)
except ValueError:
    print("Value Error")






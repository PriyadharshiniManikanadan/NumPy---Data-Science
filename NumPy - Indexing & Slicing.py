# Index with List in NumPy:

""" In python we can access only the index or sequencial index
    But if we need index value for example : [0,5,10], this is not applicable in Python.
    So, in NumPy """

import numpy as np
a = np.array([4,6,8,9,3,2,1,4,7,5,6,3])
print(a[5])

for i in enumerate(a):   # prints all index with values
    print(i)

print("="*100)

# In NumPy it is possible

print("Index with List in Numpy:",a[[0,5,8]])

print("="*100)



# Indexing & Slicing :

# Advance slicing for multidimensional array

# Basic to understand Advance Indexing & Slicing:

""" By default it takes row wise indexing """

import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(a[2])

s = slice(1,4)
print(a[s])

print(a[0:3])
print(a[:2])
print(a[3:])
print(a[:-1])

print("="*100)

# Advance Indexing & slicing --- for column wise slicing

""" Slicing can also include <   ELLIPSES  (...)   > for multidimensional array """

# 2D array

A = np.array([[1,2,3],[5,6,7],[10,50,60]])
print(A)

print("="*100)

print(A[1])  # row indexing
#
print("="*100)

print(A[1:])  # row slicing

print("="*100)

print(A[...,2])  # column slicing but output is in vector

print("*"*100)

print(A[1,...])  # row slicing so obviously output is in vector

print("="*100)

# 3D array  -- Ellipses (...)

import numpy as np
x = np.random.randint(0,28,size= (3,3,3))
print(x)
print(len(x))

print("="*100)

print(x[...,2])

print("="*100)

print(x[0,...])

print("="*100)

print(x[1,2,...])

print("="*100)

print(x[...,1:])

print("="*100)

# Example in Real time data for slicing

import numpy as np
Data = np.array( [["Priya","31","2000"],
                 ["Mani", "34", "5000"],
                 ["Utsav", "7", "1000"]])

print("Person Names")
print(Data[...,0])

print("Age of Person")
print(Data[...,1])

print("Steps count of individual")
steps_count = Data[...,2]
print(steps_count)
print(type(steps_count))
sumofstepcount = (steps_count.astype(int)) # changing from str - int
print(sum(sumofstepcount ))

print("="*100)

#{OR}

print("change the dtype from string to list to summ all")
data = list(steps_count)
print(data)
print(type(data))

print("="*100)

sumofsteps = 0
for i in data:
   i = int(i)
   sumofsteps = sumofsteps + i
print("{} is the sum of all persons steps count".format(sumofsteps))

print("="*100)

# (OR)

import numpy as np
Data1 = np.array( [["Priya","31",2000],
                 ["Mani", "34", 5000],
                 ["Utsav", "7", 1000]],dtype = object)

print(Data1)
print(type(Data1))
steps = (Data1[...,2])
print(steps)
print(sum(steps))

print("="*100)

# Ellipses can be used in negative inex also:

import numpy as np

arr = np.array([[1,2,3],[2,1,3],[2,4,5]],dtype='i1')
print(arr)
print(arr.ndim)
print(len(arr))
print(type(arr))
print(arr.dtype)
print(arr.shape)
print(arr.size)
print(arr.itemsize)
print(arr.nbytes)

print("="*100)

print(arr[...,-1])  # without colon, output is in vector format
print(arr[...,-1:]) # with colon, output is in matrix format
                    #  we are not loosing the original dimensions of ndarray
print("="*100)

print(arr[...,-2])
print(arr[...,-2:])

print("="*100)

# np.view -- Creating View Using Slice

import numpy as np

print("# np.view -- Creating View Using Slice")
arr = np.array([[1,2,3],[2,1,3],[2,4,5]],order = 'F',dtype='int8')
print(arr)
print(id(arr))
print("==================")
a = arr.view(np.int8)  # View - view is created for arr as a
print(a)
print(id(a))
print("==================")
a[0][2] = 50  # it changes the value in view
print(a)
print("==================")
print(arr)   # It is also reflected in original array 'arr'
print("==================")

# np.copy -- Creating copy Using Slice

print("np.copy -- Creating copy Using Slice")
arr1= np.array([[1,2,3],[2,1,3],[2,4,5]])
print(arr1)
print(id(arr1))
print("****************")
a1 = arr1.copy()  # View - view is created for arr as a
print(a1)
print(id(a1))
print("****************")
a1[0][2] = 50  # it changes the value in view
print(a1)
print("****************")
print(arr1)   # It is also reflected in original array 'arr'

print("="*100)

# Advance Indexing for multidimensional array

""" This mechanism helps in selecting the arbitrary items in an array based on their N dimensional index
    It is very powerfull than ellipses slicing """

import numpy as np
testarray = np.array([[1,2,3],[3,2,1],[5,2,4]])
print(testarray)

x = testarray[[0,1,2],[1,2,0]]  # integer indexing ( it takes as 0th row 1st index, 1st row 2nd index, 2nd row 0th index.
print(x)

y = testarray[...,2]  # slicing Ellipses - column wise slicing - it takes the whole column
print(y)

print("==================================")

# Example :

# Advance Integer Indexing :

# To get all corner values ?  0,8,0,0

x = np.array([[0,1,8],
              [10,150,200],
              [52,63,74],
              [0,1,0]])
print(x)

Rows = ([[0,0],[3,3]])
print(Rows)
Columns = ([[0,2],[0,2]])
print(Columns)

y = x[Rows,Columns]  # Main Syntax
print(y)

print("==================================")
# Example for the above

import numpy as np
a =np.array([[0,1,8],[10,150,200],[52,63,74],[0,1,0]])
print(a)
print("==================================")
b = a[1:4]  # Row slicing
print(b)
print("==================================")
c = a[1:4,1:3] # It takes as 1:4 - Row slicing &  1:3 - Column slicing
print(c)
# print("==================================")
# print(a)
# print("==================================")
# d = a[0:3][1:2] # if it is given in seperate square bracket - it takes both as ie: [0:3][1:2] as row slicing
# print(d)
print("==================================")
E = a[0:3,1:2]
# if it is given in Same square bracket - it takes [0:3] as roe slicing & [1:2] as column slicing

#Concept NO : 1 , output : syntax ==  y = x[Rows : column] ie : y=x([0:3,1:2])
# it doesnot includes the 2nd column in the output

print(E)
print("==================================")

# Using advance indexing for choosing particular COLUMN

# Another New Concept NO : 2  = different output : syntax ==  y = x[Rows,[columns in comma]] ie : y=x([0:3,[1,2]])
# Thwe main difference is - it includes the 2nd column also in the output
print(a)
print("==================================")
F = a[0:3,[0,2]]
print(F)
print("==================================")
G = a[[0,2],[1,2]]
print(G)

# 2. Boolean Indexing   -  Comparison Operators

import numpy as np
bool = np.array([[100,200,300],
                [400,500,600],
                [700,800,900],
                [300,200,100]])
print(bool > 500)
print(bool[bool>500])

print("====================================================")

# Another way by taking 2nd index

y = bool[2]
print(y)
print(y > 800)
print(y[y > 800])

print("==================================================")

# Find NaN values :

array = np.array([np.nan,2,3,np.nan,5,6])
print(array)
print(len(array))

print("==================================================")

a = np.isnan(array)
print(a)
print(len(a))

print("==================================================")

# boolean indexing

b = array[a] # Indexing with boolean array is possible because both the array length are same
print(b)

print("================================================")

c = array[~a] # (~ is opposite) boolean indexing to remove all NaN values
print(c)

print("==================================================")

# Complex

X = np.array([11,2+5j,22,3+10j])
print(X)

print("=====================================================")

ab = np.iscomplex(X)
print(ab)

ab = ~np.iscomplex(X)
print(ab)

y = X[np.iscomplex(X)]  # Using boolean array we are using the original array for getting non complex values
# But because numpy is homogeneous, th output is the int values of original array is converted to complex datatype

print(y)

Z = X[~np.iscomplex(X)]
print(Z)
#
print(np.real(Z))
print(np.imag(Z))

# flat attribut




















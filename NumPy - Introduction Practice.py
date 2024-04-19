import numpy as np
a = [1,2,3,4,5]
print(type(a))

"""   There are many methods to create ndarray, one of the method is np.array   """

b = np.array(a)
print(type(b))

# OR

c = np.array([2,4,6,8,10])
print(type(c))


print("=" * 100)

# 1.  np.array method

# Example 1 - dtype = int, float, str, bool

a = np.array([[1,2],[2,1]], dtype =int, copy=True, order='A', subok=False, ndmin=0)
print("int",a)

a = np.array([[1,2],[2,1]], dtype =float, copy=True, order='A', subok=False, ndmin=0)
print("Float",a)

a = np.array([[1,2],[2,1]], dtype =str, copy=True, order='A', subok=False, ndmin=0)
print("Str",a)

a = np.array([[1,-2],[1.2,0]], dtype =bool, copy=True, order='A', subok=False, ndmin=0)
print("bool",a)

a = np.array([[1,-2],[1.2,0]], dtype =complex, copy=True, order='A', subok=False, ndmin=0)
print("complex",a)

a = np.array([[1,-2j],[1.2,0]], dtype =complex, copy=True, order='A', subok=False, ndmin=0)
print("complex",a)   ### Complex takes highest Memory

print("=" * 100)
# Example 2

# Attributes of NumPy - itemsize, Size, nbytes

A = np.array([["DataScience", "A"]],dtype =str, copy=True, order='F', subok=False, ndmin=0)
print(A)

print("Attributes of numpy")

print(A.itemsize)
print(A.size)
print("itemsize * size = nbytes")
print(A.nbytes)

# Object dtype = contains heterogenous data

A = np.array([["DataScience", 1],[2.5,True]],dtype =object, copy=True, order='F', subok=False, ndmin=0)
print(A)
print(type(A))
print(A.itemsize)
print(A.size)
print(A.nbytes)


# None dtype = takes which occupies more memory space

A = np.array([["DataScience", 1],[2.5j,True]],dtype = None, copy=True, order='F', subok=False, ndmin=0)
print(A)
print(type(A))
print(A.itemsize)
print(A.size)
print(A.nbytes)

print("="*100)

""" These are called Metadata, === means DATA about data ==== Exmaple below """



ndarray = np.array([[1,2],[2,1]], dtype =int, copy=True, order='A', subok=False, ndmin=0)


print("METADATA - Data about Data")
print("="*100)
print("ndarray) : ",ndarray)
print("="*100)
print("type(ndarray) : ",type(ndarray))
print("="*100)
print("ndarray.ndim:",ndarray.ndim)
print("="*100)
print("ndarray.shape:",ndarray.shape)
print("="*100)
print("ndarray.size:",ndarray.size)
print("="*100)
print("ndarray.itemsize:",ndarray.itemsize)
print("="*100)
print("ndarray.nbytes:",ndarray.nbytes)
print("="*100)
print("ndarray.data:",ndarray.data)
print("="*100)
print("ndarray.flags:",ndarray.flags)
print("="*100)

# put() method -- Replacing the original values as another value through Index

a = np.array([1,2,3,4,5], dtype= object)

print("ndarray:",a)

# np.put(a,[0,2,4],[10,20,True])
# print("put method:",a)

print("="*100)

# Modes for put() method - wrap , Raise , Clip

# np.put(a,[0,2,10],[10,20,True], mode = 'clip')
# print("puy method -> mode - clip:",a)

# np.put(a,[0,2,10],[100,20,"data"], mode = 'wrap')       # [1,2,3,4,5]
# print("put method -> mode - wrap:",a)

# print(help(np.put))

# np.put(a,[0,2,5],[10,20,True], mode = 'raise')
# print("puy method -> mode - raise:",a)


# 2. dtype parameter -- ndmin

ndarray = np.array([0,1,2,3,4,5], dtype =int, ndmin=2)
print(ndarray)
print(type(ndarray))
print(ndarray.reshape(2,3))

print("="*100)

# what happens if the memory space is not enough to store data ?

""" In int 8 we can able to store numbers 1 - 127 """

import numpy as np

dt = np.dtype('i1')
a = np.array([(1,),(2,),(3,),(4,),(127,)], dtype=dt)

print(a)
print(dt)
print(a.size)
print(a.itemsize)
print(a.nbytes)

""" So, i can keep only 0 - 127  numbers in 1 byte (by default in comp architechture) 

But if we need to keep more than 127, for example 500 , i need to change the byte inti i2"""

dt = np.dtype('i2')
b = np.array([(1,),(2,),(3,),(4,),(500,)], dtype=dt)

print(b)
print(dt)
print(b.size)
print(b.itemsize)
print(b.nbytes)

print("="*100)

# Parameter - Order

"""
C - Row major
F - Column major ( Fortran)
A - Default
"""
ndarray = np.array([[0,1,2,3,4,5]], dtype =int, ndmin=2, copy=True, order='F', subok=False)

print("="*100)
import numpy as np

A = np.arange(0,16).reshape(2,4,2)

print(A)
print(A.ndim)
print(A.shape)
print(A.size)
print(A.itemsize)
print(A.nbytes)
print(A.dtype)

dt = np.dtype('i1') # i1 is called Notation

a = np.array([1,2,3,4,5], dtype=dt,copy=True,ndmin=2,order='C',subok=False)
print(a)
print("a.size:",a.size)
print("a.itemsize:",a.itemsize)
print("a.nbytes:",a.nbytes)
print("a.dtype:",a.dtype)
print("a.shape:",a.shape)
print("a.ndim:",a.ndim)

print("="*100)

"""-128 to 127 = int 8"""

dt = np.dtype('i1')
a = np.array([1,2,3,4,-128], dtype=dt,copy=True,ndmin=2,order='C',subok=False)
print(a)
print("a.size:",a.size)
print("a.itemsize:",a.itemsize)
print("a.nbytes:",a.nbytes)
print("a.dtype:",a.dtype)
print("a.shape:",a.shape)
print("a.ndim:",a.ndim)

print("="*100)

dt = np.dtype('i2')
a = np.array([1,2,3,4,500], dtype=dt,copy=True,ndmin=2,order='C',subok=False)
print(a)
print("a.size:",a.size)
print("a.itemsize:",a.itemsize)
print("a.nbytes:",a.nbytes)
print("a.dtype:",a.dtype)
print("a.shape:",a.shape)
print("a.ndim:",a.ndim)

print("="*100)

# Parameter - Order

"""
C - Row major
F - Column major ( Fortran)
A - Default
"""
dt = np.dtype('i1')
b = np.array([(0,),(1,),(2,),(3,),(4,),(5,)], dtype=dt, ndmin=3, copy=True, order='A', subok=False)
print(b)
print("b.size:",b.size)
print("b.itemsize:",b.itemsize)
print("b.nbytes:",b.nbytes)
print("b.dtype:",b.dtype)
print("b.shape:",b.shape)
print("b.ndim:",b.ndim)

print("="*100)

dt = np.dtype('i1')
b = np.array([[1,2,3],[3,2,1]], dtype=dt, ndmin=3, copy=True, order='F', subok=False)
print(b)
print("b.size:",b.size)
print("b.itemsize:",b.itemsize)
print("b.nbytes:",b.nbytes)
print("b.dtype:",b.dtype)
print("b.shape:",b.shape)
print("b.ndim:",b.ndim)

print("="*100)

# dtype - parameters

# example

dt = np.dtype(np.int32,align=True, copy=False)

c = np.array([1,-2,3,-4], dtype = dt)               # int 32 = byte 4
print(c)
print(c.shape)
print(c.ndim)
print("c.size;",c.size)
print("c.itemsize;",c.itemsize)
print("c.nbytes:",c.nbytes)

print("="*100)

dt = np.dtype(np.int16,align=True, copy=False)      # int 16 = byte 2

c = np.array([1,-2,3,-4], dtype = dt)
print(c)
print(c.shape)
print(c.ndim)
print("c.size;",c.size)
print("c.itemsize;",c.itemsize)
print("c.nbytes:c",c.nbytes)

print("="*100)

dt = np.dtype(np.int8,align=True, copy=False)  # int 8 = byte 1

c = np.array([1,-2,3,-4], dtype = dt)
print(c)
print(c.shape)
print(c.ndim)
print("c.size;",c.size)
print("c.itemsize;",c.itemsize)
print("c.nbytes:c",c.nbytes)
print("="*100)

dt = np.dtype('i1',align=True, copy=False)

c = np.array([1,-2,3,-4], dtype = dt)
print(c)
print(c.shape)
print(c.ndim)
print("c.size;",c.size)
print("c.itemsize;",c.itemsize)
print("c.nbytes:c",c.nbytes)







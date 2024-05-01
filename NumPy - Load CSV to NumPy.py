# we can able to change the data type of the data here itself

# astype - keyword

# Example

# By default the dtype is float

# np.genfromtxt() method to read file

import numpy as np

x = np.genfromtxt("C:\\Users\\priya\\Desktop\\DATA SCIENCE\\DATASET\\corr_data.csv", delimiter = ",")
print(x)

a = x.astype("str")
print(a)

# b = x.astype('int32')
# print(b)

# Boolean Masking:

# print(healthdata > 200)  # Get the output as True / False
#
# # Instead of getting Boolean values , show the Real values
#
# y = healthdata[healthdata > 500]
# print(y)

print("="*100)

print("="*100)

# import numpy as np
# data = np.genfromtxt("Sleepdata.csv", dtype = 'str',delimiter=',')

# (OR)

""" *********   genfromtxt method has 25 parameters    **************"""

from numpy import genfromtxt
data = genfromtxt("Sleepdata.csv", dtype = 'str',delimiter=',')
print(data)
print(type(data))
print(data.shape)

print("="*100)

a = (data[0])
print(a)
print(type(a))

# a = (data[1:3])
# print(a)

# Using python change string into list, now we can access the index.

b = list(a)
print(b)
print(type(b))
print("len of b :",len(b))
# print(b[[2,5,6]])   # Error - no option in list


ndarray = np.asarray(b)
print(ndarray)
print(ndarray.ndim)
print(ndarray.shape)
print(ndarray.size)
print(ndarray.itemsize)
print(ndarray.nbytes)
print(type(ndarray))
print(ndarray.dtype)
print(ndarray[[1,5,9,12,1]]) # List allows duplicates

print("="*100)

# another parameter for genfromtxt: ---   comments (any symbols for comments is applicable)
# Multiline commets is also valid.

from numpy import genfromtxt
x = genfromtxt("Sleepdata.csv",dtype='U',delimiter=',',comments='&')
print(x)

print("="*100)

x = genfromtxt("Sleepdata.csv",dtype='U',delimiter=',',comments='&')
print(x)

print("="*100)

# another parameter for genfromtxt is ---- skip_header = True/False

x1 = genfromtxt("Sleepdata1.csv",dtype='U',delimiter=',',skip_header=True)
print(x1)

print("="*100)

x1 = genfromtxt("Sleepdata1.csv",dtype='U',delimiter=',',skip_header=False)
print(x1)

print("="*100)

# another parameter for genfromtxt is ---- skip_footer = True/False/count

x1 = genfromtxt("Sleepdata1.csv",dtype='U',delimiter=',',skip_footer=True)
print(x1)

print("="*100)

x1 = genfromtxt("Sleepdata1.csv",dtype='U',delimiter=',',skip_footer=2)
print(x1)

print("="*100)

# another parameter for genfromtxt is ---- missing_values{column index:"" },filling_values{column index : values}

# will take simple example for understanding:

from numpy import genfromtxt

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",") # missing values are taken as -1
print(testdata)

print("="*100)

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",",missing_values={1:""},filling_values={1:111})
print(testdata)

# for the above , the values are filled in the missing columns based on index.

print("="*100)

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",",missing_values={1:"",3:""},filling_values={1:111,3:999})
print(testdata)

# for the above , the values are filled in the 2 missing columns based on index 1 & 3.

print("="*100)

# another parameter for genfromtxt is --- replace_space

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",")
print(testdata)

print("="*100)

# another parameter for genfromtxt is --- defaultfmt="f%i"

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",",)
print(testdata)

print("="*100)

# another parameter for genfromtxt is --- encoding='bytes'

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",",encoding='bytes')
print(testdata)

# another parameter for genfromtxt is --- ndmin

print("="*100)

testdata = genfromtxt("sample.csv",dtype=int,delimiter=",",ndmin=2)
print(testdata)

print("="*100)

# Write or store a nparray to csv :

testdata.tofile("numpy2csvfile.csv",sep="\n",format="%s")
print(testdata)

print("="*100)

x = genfromtxt("Sleepdata.csv",dtype='U',delimiter=',',comments='&')
print(x)

#
# x.tofile("xnumpy2csvfile.csv",sep="\n",format="%s")
# print(x)


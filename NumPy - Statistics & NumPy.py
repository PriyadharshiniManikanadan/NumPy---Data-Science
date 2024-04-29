
# STATISTICS

# Max & MIn in 2D

import numpy as np
a = np.array([[1,-2,3],[2,-3,-4],[5,-2,-6]])
print(a)
print(type(a))

print(np.max(a))
print(np.min(a))

print("="*100)

# Max & MIn in 2D based on axis:

import numpy as np
b = np.array([[1,-2,1],
              [2,-3,-3],
              [1,-2,-6]])
print(b)
print(type(b))
print("=============================")

print("Max & MIn in 2D based on axis")

print(np.max(b,axis=0))
print(np.min(b,axis=1))


# Find - Mean, Median, Mode, STD ?


# There is no function for finding mode in NumPy library.
# So, we are using SciPy library for getting the mode value.

# SciPy :

"""    SciPy is a free and open-source Python library used for scientific computing and technical computing.
        SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions,
        FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.    """


import scipy
print(scipy.__version__)

import numpy as np
from scipy import stats
healthdata = np.genfromtxt("C:\\Users\\priya\\Desktop\\DATA SCIENCE\\DATASET\\corr_data.csv", dtype = int, delimiter = ",")
print(healthdata)
print("healthdata.ndim:",healthdata.ndim)

print("type(healthdata:",type(healthdata))

print("healthdata.shape:",healthdata.shape)

print("np.min(healthdata):",np.min(healthdata))

print("np.max(healthdata):",np.max(healthdata))

print("np.mean(healthdata):",np.mean(healthdata))

print("np.median(healthdata):",np.median(healthdata))

print("stats.mode(healthdata, axis = 0):",stats.mode(healthdata, axis = 0))   # Note : NumPy does not have mode function

print("np.std(healthdata):",np.std(healthdata))

print("np.average:",np.average(healthdata))

print("="*100)

print("=================================================")

# Statistical functions based on axis

A = np.array([[1,2,3],
              [3,4,5],
              [0,2,8]])
print(A)

print("=================================================")

print("np.amax,in axis 0:",np.amax(A,axis=0))

print("np.amax,in axis 1:",np.amax(A,1))

print("=================================================")

print("np.amin,in axis 0:",np.amin(A,axis=0))

print("np.amin,in axis 1:",np.amin(A,1))

print("=================================================")

# np.ptp (Peak to Peak)

# Max value _minus_ Min value

B = np.array([[1,2,3],
              [3,4,5],
              [0,2,8]])
print("np.ptp:",np.ptp(A,0))  # in column wise  3-0 = 3 , 4-2 = 2, 8-3 = 5

print("np.ptp:",np.ptp(A,1)) # in rows

print("=================================================")
print(np.percentile(A,8))

print("=================================================")

# np.avarage()

# can also find by axis between 2 arrays

A = np.array([1,2,3,4,5])
print(A)

print(np.average(A))

wts = np.array([2,3,4,5,6])
print(wts)
#
print("np.average:",np.average(A,weights=wts,returned=False))  # without weighted avearge

print("np.average:",np.average(A,weights=wts,returned=True)) # with weighted avearge

print("=================================================")

# np.std()

A = np.array([1,2,3,4,5])
print(A)

print(np.std(A))

print("=================================================")





























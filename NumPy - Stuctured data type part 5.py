# Functions around

# np.around()

import numpy as np
a = np.array([1.2,0.956,3.456,11.26558,12.56914])
print(a)
print(a.dtype)

b = np.around(a)
print("around:",b)
print(b.dtype)
print("=================================================================")
c = np.around(a,decimals=1) # round of near to 10
print("around - decimal :",c)
print(c.dtype)
print("=================================================================")
d = np.around(a,decimals=2) # round of near to 100
print("around - decimal :",d)
print(d.dtype)
print("=================================================================")
e = np.around(a,decimals=3) # round of near to 1000
print("around - decimal :",e)
print(e.dtype)
print("=================================================================")

# np.floor()

A = np.array([1.2,0.956,3.456,11.26558,12.56914])
print(A)
print(A.dtype)

B = np.floor(A)
print("floor:", B)
print(B.dtype)
print("=================================================================")

# np.ceil()

A = np.array([1.2,0.956,3.456,11.26558,12.56914])
print(A)
print(A.dtype)

B = np.ceil(A)
print("ceil:", B)
print(B.dtype)
print("=================================================================")


#

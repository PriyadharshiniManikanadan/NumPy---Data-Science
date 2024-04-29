# Stacking :

""" All the dimensions should be the same for stacking """

import numpy as np

a = np.array([[1,2,3],[3,2,1]])
print(a)
print(a.shape)
print(a.ndim)
print("===============================================================")

b = np.array([[10,20,30],[30,20,30]])
print(b)
print(b.shape)
print(b.ndim)
print("===============================================================")

c = np.array([[11,22,33],[44,55,66]])
print(c)
print(c.shape)
print(c.ndim)
print("===============================================================")

Horizontalstack = np.hstack((a,b,c))
print(Horizontalstack)
print(Horizontalstack.shape)
print(Horizontalstack.ndim)
print("===============================================================")

Verticalstack = np.vstack((a,b,c))
print(Verticalstack)
print(Verticalstack.shape)
print(Verticalstack.ndim)

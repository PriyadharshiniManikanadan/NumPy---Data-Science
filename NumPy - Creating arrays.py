"""
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".
"""

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print(np.__version__)

# Create a NumPy ndarray Object

"""
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function."""

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# type(): This built-in Python function tells us the type of the object passed to it.
# Like in above code it shows that arr is " numpy.ndarray " type


"""
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
and it will be converted into an ndarray:
"""

import numpy as np
arr = np.array((1,2,3,4,5))
print(arr)
print(arr.ndim)

#






# String comparisons :

# 1. np.equal()

# print("In 1D Array")

# import numpy as np
# a =np.array([0,1,2,0,12,0,3,5])
# print("Equal:\n",a)
# print(np.equal(a,0))  # will check the value is 0 or not
#
# # In 2D array
#
# print("In 2D array")
#
# b = np.random.randint(10,20,size=(5,5))
# print(b)
# print(np.equal(b,19))
#
# print("==================================================")

# 2. np.not_equal

print("In 1D Array")

import numpy as np
a =np.array([0,1,2,0,12,0,3,5])
print("not_Equal:\n",a)
print(np.not_equal(a,0))  # will check the value is 0 or not

# In 2D array

print("In 2D array")

b = np.random.randint(10,20,size=(5,5))
print(b)
print(np.not_equal(b,19))

print("==================================================")

# 3. np.greater()

a = np.array([1,2,0,3,0,2,50,4])
print("greater:\n", a)
print(np.greater(a,2))

print("==================================================")

# 4. np.less()

import numpy as np
a = np.array([1,2,0,3,0,2,0,1,0,2,0,2])
print("less:\n", a)

b = np.less(a,2)
print(b)

print("==================================================")

# 5. np.greater_equal()

a = np.array([0,1,2,0,3,5,6,1,2])
print("greater_equal:\n", a)
print(np.greater_equal(a,3))

print("==================================================")

# 5. np.less_equal()

a = np.array([0,1,2,0,3,5,6,1,2])
print("less_equal:\n", a)
print(np.less_equal(a,3))

print("==================================================")

# 6. np.less_equal()

a = np.array([0,1,2,0,3,5,6,1,2])
print("less_equal:\n", a)
print(np.less_equal(a,3))

print("==================================================")


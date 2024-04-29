# String Informations :

import numpy as np

# np.char.count()

# Returns the Number of occurence of given values based on index ( 0 , 1 )

# ar = np.array(["geeks","for","geeks"])
# print("Count:\n", ar)
# count = np.char.count(ar,'gee')
# print(count)
#
# count1 = np.char.count(ar,'fo')
# print(count1)

# print("==========================================================")

# np.char.find()

# Returns the index value in each string

# Arr = np.array(['xczdjnidpriyadvjsklv','asjfndsipriyajndcs','jdpriyaxznvjs'])
# print(Arr)
#
# print(np.char.find(Arr,'priya'))

# print(np.char.rfind(Arr,'priya'))

# print("==========================================================")

# np.char.isalpha()

# a =np.array(["red","blue","gree n", "yello3"])
# print("isalpha:\n", a)
# print(np.char.isalpha(a))

# print("==========================================================")

# np.char.isdecimal()

# isdecimal is only available for Unicode strings and arrays

# a =np.array(["10","20.1",'12345'])
# print("isdecimal:\n", a)
# print(np.char.isdecimal(a))

# print("==========================================================")

# np.char.isdigit()

# array should be continuous digit or else false
#
# a =np.array(["10","20.1",'12345','562nb'])
# print("isdigit:\n", a)
# print(np.char.isdigit(a))

# print("==========================================================")

# np.char.islower()

# all the alphabets should be in lowercase

# string = "python in Data Science"
# print("islower:\n",string)
# a = np.char.islower(string)
# print(a)
#
# string = "python in data science"
# print("islower:\n",string)
# a = np.char.islower(string)
# print(a)

# print("==========================================================")

# np.char.isupper()

# string = "python in data science"
# print("islower:\n",string)
#
# a = np.char.isupper(string)
# print(a)
#
# b = string.upper()
# print(b)
#
# c = np.char.isupper(b)
# print(c)

# print("==========================================================")

# np.char.isspace()

# a = np.array(['\n', '\t', ' ', ' abc d'])
# print("isspace:\n",a)
# print(np.char.isspace(a))

# print("==========================================================")

# np.char.istitle()

# Only the starting letter of string should be in capital or else false

# a = np.array(["APPLE","Mango is fruit", "Tomato","guava"])
# print("isspace:\n",a)
# print(np.char.istitle(a))

# print("==========================================================")
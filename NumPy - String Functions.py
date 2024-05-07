# # NumPy - String Functions:
#
# # NumPy.char
# """ Array class
#     NumPy array package
#     Used for Vectorized string operations"""
#
# # Many numpy string functions are available
#
# # 1. np.char.add()
#
import numpy as np
#
# # In List
#
# fname = ["Priyadharshini ","Manikandan ","Utsav ","Inbav "]
# lname = ["Manikandan","Ravi","Ravimanya","Ravimanya"]
#
# Fullname = np.char.add(fname , lname)
#
# print("add:",Fullname)
# print(type(Fullname))
#
# print("==========================================================")
#
# x = print(fname + lname)
# print(type(x))
#
# print("==========================================================")
#
# # In NumPy array
#
# fname1 = np.array(["Priyadharshini ","Manikandan ","Utsav ","Inbav "], dtype=str, ndmin = 2)
# lname1 = np.array(["Manikandan","Ravi","Ravimanya","Ravimanya"],dtype=str,ndmin = 2)
#
# Fullname1 = np.char.add(fname1,lname1)
# print("add:",Fullname1)
# print(type(Fullname1))
# print(Fullname1.shape)
# print(Fullname1.ndim)
#
# print("==========================================================")
#
# # 2. np.char.multiply()
#
# fname1 = np.array(["Priyadharshini ","Manikandan ","Utsav ","Inbav "], dtype=str, ndmin = 2)
# print(fname1)
# lname1 = np.array(["Manikandan","Ravi","Ravimanya","Ravimanya"],dtype=str,ndmin = 2)
#
# Fullname1 = np.char.multiply(fname1,3)
# print("multiply:",Fullname1)
#
# print("==========================================================")
#
# # Multiply values can be in List in order to change them into Tuple / set
#
# print(" Multiply values can be in List in order to change them into Tuple / set\n")
#
# X = np.char.multiply(["Priya","Mani"], 3)
# print("multiply:",X)
# print(type(X))
# print("==========================================================")
# Y = (list(X))
# print("multiply:",Y)
# print(type(Y))
# print("==========================================================")
# Z = (tuple(X))
# print("multiply:",Z)
# print(type(Z))
# print("==========================================================")
# S = (set(X))
# print("multiply:",S)
# print(type(S))
# print("==========================================================")
#
# # 3. np.char.center()
#
# # In python
#
# name = "Priya"
# N = name.center(20,"*")  # Fill character (must be only one)
# print(N)
#
# # In NumPy nornaml data given
#
# A = np.char.center("Data Science",20,fillchar="*")
# print("center:",A)
#
# B = np.char.center("Data Science",20,fillchar="\n")
# print("center:",B)
# print("==========================================================")
#
#
# # In NumPy Array data given
#
# a = np.array(["Data ","Python ","Machine "],dtype=str,ndmin = 2)
# b = np.array(["science","language","learning"],dtype=str,ndmin = 2)
# Studies = np.char.add(a,b)
# print(Studies)
# # Studies = np.char.multiply(a,3)
# # print(Studies)
#
# x = np.char.center(Studies,30,"*")
# print("center:",x)
#
# print("==========================================================")
#
# # 4. np.char.join()
#
# x = np.char.join("-",b)
# print("join:",x)
#
# print("==========================================================")
#
# # 5. np.char.capitalize()
#
# x = np.char.capitalize("data science")
# print("capitalize:",x)
#
# print("==========================================================")
#
# # 6. np.char.title()
#
# x = np.char.title("data science")
# print("Title:",x)
#
# print("==========================================================")
#
# # 7. np.char.swapcase()
#
# x = np.char.swapcase("data science")
# print("swapcase:",x)
#
# x = np.char.swapcase("DATA SCIENCE")
# print("swapcase:",x)
#
# print("==========================================================")

# 8. np.char.split()

# It deletes the characters which is mentioned in the parameter

# a = np.array(["My aim is to become Data Scientist"])
# print("Split:\n",a)
# Z = np.char.split("   datascience    ")
# print("split:",Z) # Output will be in list
#
# Z = np.char.split(a,'i')  # It takes away all 'i' characters
# print("split:",Z) # Output will be in list
#
# Z = np.char.split(a,'t')  # It takes away all 'i' characters
# print("split:",  Z) # Output will be in list
#
# c = (np.char.split(a))
# print(repr(c))  # Representation af an object

# np.char.splitlines() - takes only \n & \r for seperating

# a = np.array(["DS\nML",'PCU\nCPU'])
# print("splitlines:\n",a)
# print(np.char.splitlines(a))
#
# a = np.array(["DS\rML",'PCU\rCPU'])
# print("splitlines:\n",a)
# print(np.char.splitlines(a))
#
# print("==========================================================")

#np.char.expandtabs()

# a = np.array(["DS\tML",'PCU\tCPU'])
# print("expandtabs:\n",a)
# print(np.char.expandtabs(a))
#
# print("==========================================================")

# np.char.just()  -  Justified Array
#
# array = np.array(["Python","Data Science"])
# print("justified:\n",array)
# a = np.char.rjust(array,20)
# print(a)
# a = np.char.rjust(array,20,'-')
# print(a)

# print("==========================================================")
#
# array = np.array(["Python","Data Science"])
# a = np.char.ljust(array,20)
# print(a)
#
# a = np.char.ljust(array,20,'-')
# print(a)
# print("==========================================================")
#
# # np.char.decode() & encode()
#
# """Using the 'Codeen' symbol we can able to decode & encode based on their countries
#    Ex : cp500 for Western Europe
#         hz for simplified chinese"""
#
# ec = np.char.encode(a, encoding='utf-8')
# print("Encode Decode:\n",ec)
# print(np.char.decode(ec,encoding='utf-8'))
# print("==========================================================")
# ec1 = np.char.encode(a,encoding='cp500')
# print(ec1)
# print(np.char.decode(ec1,encoding='cp500'))
#
# print("==========================================================")
#
# # np.char.replace()
# arr = np.array(["NumPython","Python","SciPython"])
# print("'replace:\n",arr)
# rp = np.char.replace(arr,'Python', 'Py')
# print(rp)
# print("==========================================================")
# arr1 = np.array(["PythonNumPython","PythonPython","SciPython"])
# print(arr1)
# rp1 = np.char.replace(arr,'Python','Py',count=1)
# print(rp1)
#
# print("==========================================================")
#
# # np.char.partition()
#
# b = np.array(['datascience','database','datastructures'])
# print('Partition:\n',b)
# part = np.char.partition(b,'ta')
# print(part)  # output is in lists of array seperately & changes from 1D-2D
#
# print("==========================================================")
#
# c = np.array(['datascience','database','datastructures'])
# print('Partition:\n',c)
# part1 = np.char.partition(c,'a')  # from right
# print(part1)
# print('rPartition:\n',c)
# part2 = np.char.rpartition(c,'a')  # from left
# print(part2)
#
# print("==========================================================")
#
# # np.char.zfill()
#
# a = np.array(['ds'])
# print('zerofill:\n',a)
# print(np.char.zfill(a,10))
#
# print("==========================================================")

# np.char.translate() - for translation

# inarray = np.array(["sata", 'An', 'Tamil'])
# print("Translate:\n", inarray)
#
# data_changes = {"s" : "D", "A" : "i"}    # store the changes in a variable
#
# Trans_change = 'sA'.maketrans(data_changes)  # creating translation table from dictionary
#
# print(Trans_change)  # stored in the form of - ASCII (American Standard Code for Information Interchange)  value
#
# """The ascii value represents the character variable in numbers,
#  and each character variable is assigned with some number range from 0 to 127.
#  For example, the ascii value of 'A' is 65."""
#
# outarray = np.char.translate(inarray,Trans_change)
# print(outarray)
#
# print("==========================================================")

# NumPy - Arithmetic Functions

a = np.arange(9,dtype=np.float_).reshape([3,3])
print(a)

b = np.array([10,10,10])
print(b)

print("=================================================================")

# np.add()

add = np.add(a,b)
print("add:\n",add)

print("=================================================================")

#np.subtract()

sub = np.subtract(a,b)
print("subtract:\n",sub)
print("=================================================================")

#np.multiply()

mul = np.multiply(a,b)
print("multiply:\n",mul)
print("=================================================================")

#np.division()

div = np.divide(a,b)
print("divide:\n",div)

print("=================================================================")

# Absolute values

a = -10
print("Absolute:",abs(a))  # gives the neg values as positive value

print("=================================================================")

# np.resciprocal()

A = np.array([1.2,0.9,3.4,11,12.56])
print(A)

B = np.reciprocal(A,dtype=float)
print("Reciprocal:",B)
print("=================================================================")

Aa = np.array([1,2,3,4,5,7,8,9])
print(Aa)
#
Bb = np.reciprocal(Aa,dtype=int) # after reciprocal it gives thr int values
print("Reciprocal:",Bb)

print("=================================================================")

# np.power()

# no negative powers
# possible between 2 arrays also

Aa = np.array([1,2,3,4,5,7,8,9])
print(Aa)

Bb = np.array([2,2,2,2,2,2,2,2,])

print(np.power(Aa,3))

print(np.power(Aa,5))

print(np.power(Aa,0))

print(np.power(Aa,Bb))
print("=================================================================")

#np.mod()

# modulus = reminder

x= np.array([1,2,3,4,5,7,8,9,10,11])
print(x)

print("modulus:",np.mod(x,3))

print("=================================================================")

#np.remainder()

# Same result as modulus

x= np.array([1,2,3,4,5,6,7,8,9,10,11])
print(x)

y = np.array([1,2,1,2,4,2,5,3,6,6,8])

print("remainder:",np.remainder(x,y))

print("=================================================================")

a = ([-5.6j,0.2j,11,1+1j])

print("np.real:",np.real(a))  # np.real()

print("np.imag:",np.imag(a))  # np.imag()

print("np.conj:",np.conj(a))   # np.conj()

print("np.angle:",np.angle(a))  # np.angle()

print("=================================================================")

# Arithmetic Operators
print("Arithmetic Operators")
print("4 + 4 =",4 + 4)
print("4 - 4 =",4 - 4)
print("4 * 4 =",4 * 4)
print("4 ** 4 =",4 ** 4)
print("15 / 4 =",15 / 4)
print("15 // 4 =",15 // 4) # // It converts float value into integer Or it ignores value agter point
print("7 % 4 =",7 % 4) # It divides and gives us remainder

# Assignment Operators

print("Assignment Operators")
x = 5
print(x)
x += 10
print(x)
x -= 10
print(x)
x *= 10
print(x)
x **= 10
print(x)
x %= 10
print(x)
x /= 10
print(x)
x //= 10
print(x)
y = 5
y &= 1
print(y)
z = 3
z |= 3
print(z)
a = 5
a ^= 3
print(a)
b = 5
b >>= 3
print(b)
c = 5
c <<= 3
print(c,"\n")

# Comparision Operators

print("Comparision Operators")
i = 5
print("i == 5",i == 5)
print("i != 5",i != 5)
print("i > 5",i > 5)
print("i < 5",i < 5)
print("i >= 5",i >= 5)
print("i <= 5",i <= 5,"\n")

# Logical Operators
print("Logical Operators")
n = True
m = False

print(n and m)
print(n or m)
print(not(n and m),"\n")

# Identity Operators

print("Identity Operators")
p = 5
q = 10
print(p is q)
print(p is not q,"\n")


# Membership Operators

print("Membership Operators")
list1 = [10,15,20,25,30,35,40]
print(30 in list1)
print(29 not in list1)


# Bitwise Operatpors works in binary form
"""
0 = 00
1 = 01
2 = 10
3 = 11
"""

print("Bitwise Operatpors")
print(0 & 1)
print(0 | 3)

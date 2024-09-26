from math import *

# Программы написаны сразу с данными для проверки


# 1
print(1)


x = 14.26
y = -1.22
z = 3.5 * 10**(-2)

s = ( (2 * cos(x - (2/3)) ) / ((1/2) + pow((sin(y)), 2)) ) * (1 + ( (pow(z, 2)) / (3 - pow(z, 2) / 5) ))

print(round(s,2))

# 3
print(3)
x = 3.74*10**(-2)
y = -0.825
z = 0.16 * 10**(2)

a1 = (1 + sin(x+y)**2)/(abs(x - ( (2*y) / (1 + x**2 * y**2) ))) * x**abs(y)
a2 =  cos(atan(1/z))**2

s = a1 + a2

print(round(s,2))
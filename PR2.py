from math import *

# Программы написаны сразу с данными для проверки


# 1
print("Задание 1")


x = 14.26
y = -1.22
z = 3.5 * 10**(-2)

s = ( (2 * cos(x - (2/3)) ) / ((1/2) + pow((sin(y)), 2)) ) * (1 + ( (pow(z, 2)) / (3 - pow(z, 2) / 5) ))

print(round(s,6))

# 2
print("Задание 2")
x = -4.5
y = 0.75*10**(-4)
z = -0.845 * 10**(2)

a1 = (9+(x-y)**2)**(1/3)
a2 = x**2 + y**2 + 2

s = a1/a2 - exp(abs(x-y))*(tan(z)**3)

print(round(s,6))


# 3
print("Задание 3")
x = 3.74*10**(-2)
y = -0.825
z = 0.16 * 10**(2)

a1 = (1 + sin(x+y)**2)/(abs(x - ( (2*y) / (1 + x**2 * y**2) ))) * x**abs(y)
a2 =  cos(atan(1/z))**2

s = a1 + a2

print(round(s,6))

# 4
print("Задание 4")
x = 0.4*10**(4)
y = -0.875
z = -0.475* 10**(-3)

a1 = abs(cos(x) - cos(y))**(1 + 2 * sin(y)**2)
a2 = 1 + z + (z**2 / 2) + (z**4 / 4) + (z**4 / 4) 

s = a1*a2

print(round(s,6))


# 5
print("Задание 5")
x = -15.246
y = 4.642 * 10**-2
z = 21

a1 = log(y**(-1*sqrt(abs(x)))) * (x - (y/2))
a2 = sin(atan(z))**2

s = a1*a2

print(round(s,3))

# 6
print("Задание 6")
x = 16.55 * 10**-3
y = -2.75
z = 0.15

a1 = sqrt(10*((x)**(1/3) + x**(y+2)))
a2 = (asin(z)**2) - abs(x-y)
s = a1*a2
print(round(s, 4))

# 7
print("Задание 7")
x = 0.1722
y = 6.33
z = 3.25 * 10**-4

s = (5 * (atan(x))) - (1/4*(acos(x)) * ((x + 3 * abs(x-y) + x**2)/(abs(x-y) * z + x**2)))

print(round(s, 3))

# 8
print("Задание 8")
x = -2.235 * 10**-2
y = 2.23
z = 15.221

a1 = (exp(abs(x-y)) * abs(x-y)**(x+y)) / (atan(x) + atan(z))
a2 = (x**6 + log(y)**2)**(1/3)
s = a1+a2
print(round(s, 4))

# 9
print("Задание 9")
x = 1.825 * 10**2
y = 18.225
z = -3.296 * 10**-2

a1 = abs(x**(y/x) - (y/x)**(1/3))
a2 = (y-x) * ((cos(y) - (z/(y-x))) / (1+(y-x)**2))
s = a1+a2
print(round(s, 5))

# 10
print("Задание 10")
x = 3.981 * 10**(-2)
y = -1.625 * 10**(3)
z = 0.512

s = 2**(-1*x) * sqrt(x + (abs(y))**(1/4)) * ((exp(x - (1/sin(z))))**(1/3))

print(round(s, 5))

# 11
print("Задание 11")
x = 6.251
y = 0.827
z = 25.001

s = y**((abs(x))**(1/3)) + (cos(y)**3 * ((abs(x-y) * (1 + (sin(z)**2 / sqrt(x+y)))) / (exp(x-y) + (x/2))))
print(round(s, 6))

# 12
print("Задание 12")
x = 3.251
y = 0.325
z = 0.66 * 10**-5

s = 2**(y**x) + (3**x)**y - ((y * (atan(z) - (1/3)))/(abs(x) + (1 /(y**2 + 1))))

print(round(s, 5))

# 13
print("Задание 13")
x = 17.421
y = 10.362 * 10**-3
z = 0.828 * 10**5

a1 = (y + (x-1)**(1/3))**(1/4)
a2 = abs(x-y)*(sin(z)**2 + tan(z))
s = a1/a2

print(round(s, 6))

# 14
print("Задание 14")
x = 12.3 * 10**-1
y = 15.4
z = 0.252 * 10**3

a1 = (y**(x+1))/((abs(y-2))**(1/3) + 3)
a2 = ((x + (y/2)) / (2 * abs(x+y))) * (x+1)**(-1/sin(z))

s = a1 + a2

print(round(s, 4))

# 15
print("Задание 14")
x = 2.444
y = 0.869 * 10**-2
z = -0.13 * 10**3

a1 = (( x**(y+1) + exp(y-1)) / (1 + x*abs(y-tan(z)))) * (1 + abs(y-x))
 

s = a1 + ((abs(y-x)**2) / 2) - ((abs(y-x)**3)/3)

print(round(s, 6))

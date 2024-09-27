def fact(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i+=1

    return f

def fibonacci(n):
    if n in (1, 2):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib_sum(n, k):
  a = 0
  b = 1

  for i in range(k):
    a, b = b, a + b

  sum = a

  for i in range(n - 1):
    a, b = b, a + b
    sum += a

  return sum

# 1
print("Задание 1")
print("Введите данные:")
a = int(input("Начало отрезка: "))
b = int(input("Конец отрезка: "))

i = a

while i <= b:
    print(i, end='')
    i+=1

print()

# 2
print("Задание 2")
print("Введите данные:")
a = int(input("Начало отрезка: "))
b = int(input("Конец отрезка: "))

if a < b:
    i = a
    while i <= b:
        print(i, end=' ')
        i+=1

    print()


if a > b:
    i = a
    while i >= b:
        print(i, end=' ')
        i-=1

    print()

if a == b:
    print('Числа равны')

# 3
# Нечетные
print("Задание 3")
print("Введите данные:")
a = int(input("Начало отрезка: "))
b = int(input("Конец отрезка: "))

if a < b:
    for i in range(b, a-1, -1):
       if i % 2 != 0:
          print(i, end=' ')

    print()

if a == b:
    print('Числа равны')


# 4
print('Задание 4')
n = int(input("Кол-во чисел: "))
sum = 0
for i in range(0, n):
    tmp = int(input(f"Число №{i+1}: "))
    sum += tmp

print(f"Сумма чисел: {sum}")

# 5
print("Задание 5")
n = int(input("Последнее число: "))
sum = 0
for i in range(1, n+1):
    sum += i**3

print(f"Сумма чисел: {sum}")

# 6
print("Задание 6")
n = int(input("Введите число: "))

print(f"Факториал числа: {fact(n)}")

# 7
print("Задание 6")
n = int(input("Введите число: "))

sum = 0
for i in range(1, n+1):
    sum += fact(i)

print(f"Сумма факториалов: {sum}")

# 8
print("Задание 8")
n = int(input("Кол-во ступенек: "))

if n <= 9 and n >= 1:
    for i in range(1, n+1):
        print('-'*i)

# 9
print("Задание 9")
n = int(input("Кол-во чисел фибоначчи: "))

print(fibonacci(n))

# 10
n = int(input("Кол-во чисел Фибоначчи (N): "))
k = int(input("Порядковый номер числа Фибоначчи, с которого начать (K): "))

# Вывод результата
result = fib_sum(n, k)
print(f"Сумма {n} чисел Фибоначчи, начиная с {k}-го: {result}")
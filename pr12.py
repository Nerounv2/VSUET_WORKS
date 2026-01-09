# Практическая работа №12
# Чайкин А. У-255

# Блок А
# 1
def fac(n):
    if n == 0:
        return 1
    
    return fac(n-1) * n


def a_func1(x, n):
    if n == 0:
        return 1
    
    return (x**(n))/fac(n)

# 2
def mod(a, b):
    if a < b:
        return a
    return mod(a - b, b)

# 3
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

# 4
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

# 5
def print_digits_reverse(n):
    if n == 0:
        return
    print(n % 10, end=" ")
    print_digits_reverse(n // 10)

# 6
def is_prime(n, divisor=2):
    if n <= 2:
        return "YES" if n == 2 else "NO"
    if n % divisor == 0:
        return "NO"
    if divisor * divisor > n:
        return "YES"
    return is_prime(n, divisor + 1)

# 7
def print_range(a, b):
    if a == b:
        print(a)
        return
    print(a, end=" ")
    if a < b:
        print_range(a + 1, b)
    else:
        print_range(a - 1, b)


# Блок Б
# 1
def find_max():
    n = int(input())
    if n == 0:
        return 0
    next_max = find_max()
    return n if n > next_max else next_max
# 2
def second_max(current_max=0, second_max_val=0):
    n = int(input())
    if n == 0:
        return second_max_val
    if n > current_max:
        return second_max(n, current_max)
    elif n > second_max_val:
        return second_max(current_max, n)
    return second_max(current_max, second_max_val)

# 3
# Не совсем понял задание, поэтому выводил нечетные элементф сразу после ввода
def print_odd_positions(counter=1):
    n = int(input())
    if n == 0:
        return
    if counter % 2 == 1:
        print(n, end=" ")
    print_odd_positions(counter + 1)

# 4
def is_prime_optimized(n, divisor=2):
    if n <= 1:
        return "NO"
    if n <= 3:
        return "YES"
    if n % divisor == 0:
        return "NO"
    if divisor * divisor > n:
        return "YES"
    return is_prime_optimized(n, divisor + 1)


print("Блок А")
print("""
1. Дано натуральные числа Х,N Вычислить выражение вида: x^n / n!. 
2. Дано натуральные числа a,b Вычислить остаток от деления a на b 
3. Вывести число в обратном порядке 
4. Дано натуральное число N. Вычислите сумму его цифр. При решении 
этой задачи нельзя использовать строки, списки, массивы 
5. Дано натуральное число N. Выведите все его цифры по одной, в обратном 
порядке, разделяя их пробелами или новыми строками. При решении этой 
задачи нельзя использовать строки, списки, массивы. Разрешена только 
рекурсия и целочисленная арифметика. 
6. Дано натуральное число n>1. Проверьте, является ли оно простым. 
Программа должна вывести слово YES, если число простое и NO, если число 
составное.  
7. Даны два целых числа A и В (каждое в отдельной строке). Выведите все 
числа от A до B включительно, в порядке возрастания, если A < B, или в 
порядке убывания в противном случае. 
""")

print("1")
x = int(input("Введите x: "))
n = int(input("Введите n: "))
print(a_func1(x, n))


print("2")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(mod(a, b))


print("3")
rev = int(input("Введите число: "))
print(reverse_number(rev))


print("4")
n = int(input("Введите n: "))
print(sum_digits(n))


print("5")
n = int(input("Введите n: "))
print_digits_reverse(n)
print()

print("6")
n = int(input("Введите n: "))
print(is_prime(n))


print("7")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(print_range(a, b))

print("Блок Б")
print("""
1. Вводим последовательность натуральных чисел (одно число в строке), 
завершающаяся числом 0. Определите наибольшее значение числа в этой 
последовательности. В этой задаче нельзя использовать глобальные 
переменные и передавать какие-либо параметры в рекурсивную функцию. 
Функция получает данные, считывая их с клавиатуры. Функция 
возвращает единственное значение: максимум считанной последовательности. 
Гарантируется, что последовательность содержит хотя бы одно число (кроме нуля). 
2. Дана последовательность натуральных чисел (одно число в строке), 
завершающаяся числом 0. Определите значение второго по величине 
элемента в этой последовательности, то есть элемента, который будет 
наибольшим, если из последовательности удалить наибольший элемент. 
3. Дана последовательность натуральных чисел (одно число в строке), 
завершающаяся числом 0. Выведите первое, третье, пятое и т.д. из 
введенных чисел. Завершающий ноль выводить не надо. 
В этой задаче нельзя использовать глобальные переменные и передавать 
какие-либо параметры в рекурсивную функцию. Функция получает 
данные, считывая их с клавиатуры. Функция не возвращает значение, а 
сразу же выводит результат на экран. Основная программа должна 
состоять только из вызова этой функции. 
4. Дано натуральное число n>1. Проверьте, является ли оно простым. 
Программа должна вывести слово YES, если число простое и NO, если 
число составное. Алгоритм должен иметь сложность O(logn). 
Указание. Понятно, что задача сама по себе нерекурсивна, т.к. проверка 
числа n на простоту никак не сводится к проверке на простоту меньших 
чисел. Поэтому нужно сделать еще один параметр рекурсии: делитель 
числа, и именно по этому параметру и делать рекурсию.
""")


print("1")
print("Вводите числа (0 для завершения):")
max_value = find_max()
print(f"Максимальное значение: {max_value}")


print("2")
print("Вводите числа (0 для завершения):")
result = second_max()
print(f"Второй максимум: {result}")

print("3")
print("Вводите числа (0 для завершения):")
print_odd_positions()
print()

print("4")
num = int(input("Введите число: "))
print(f"{num} простое? {is_prime_optimized(num)}")


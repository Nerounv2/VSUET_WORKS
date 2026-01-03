from math import * # type: ignore

# # Практическая работа №8
# Чайкин А. У-255


# #1
# 1.1
def S_circle(r: float): 
    """Площадь круга"""
    return pi*(r**2)

def S_rect(a:float, b: float):
    """Площадь прямоугольника"""
    return a*b

def S_square(a: float):
    """Площадь квадрата"""
    return a**2

def S_triangle_side(a: float, h: float):
    """Площадь треугольника через высоту(h) и сторону(a). Можно использовать как для равностороннего так и прямоугольного треугольника."""
    return 0.5 * a * h

def S_right_triangle(a: float, b: float):
    """Площадь прямоугольного треугольника через 2 стороны
    Переменные: 
    a, b - катеты
    """
    return (a*b)/2

def S_triangle_Heron(a: float, b: float, c: float):
    """Площадь треугольника по теореме Герона"""
    p = (a + b + c)/2
    return (sqrt(p * (p-a) * (p-b) * (p-c)))

# 1.2 | 9.2
def avg(mas):
    """Среднее арифметическое массива"""
    return (sum(mas)/len(mas))

def max_avg_in_mas(mas):
    print("Максимальное значение и среднее арифметическое ")
    print(f"{max(mas)} --- {avg(mas)}")


# 2
# 2.1
def S_hexagon(a: float):
    """S шестиугольника через S треугольника"""
    return 6 * S_triangle_Heron(a, a, a)


# 3
# 3.1
def Hypotenuse(a: float, b: float):
    """Формула гипотенузы"""
    return sqrt(a**2 + b**2)

# 3.2
def str_sort(s: str) -> str:
    s = s.lower()
    tmp_list = s.split(" ")

    for i in range(0, len(tmp_list)):
        s_tmp = ''.join(sorted(tmp_list[i]))
        tmp_list[i] = s_tmp


    s_new = ' '.join(tmp_list)
    
    return s_new


# 4
# 4.1
# комментарии написаны для меня как пояснение

def Evklid(a: float, b: float):
    """НОД"""
    while b != 0:           # Пока второе число не станет нулём
        a, b = b, a % b     # a получает старое значение b, 
                            # b получает остаток от деления a на b
    return abs(a)           # Возвращаем абсолютное значение a (НОД)

def simplyfy4(a:float, b:float, c:float, d:float):
    """Упрощение результата деления дробей до несократимого результата. Переменные a, b, c, d - float"""
    if b == 0 or d == 0:
        return "Ошибка: знаменатель равен нулю!"

    if c == 0:
        return "Ошибка: нулевая дробь!"
    
    # при делении перемножение крест на крест X
    top = a*d
    bottom = b*c

    # делитель
    divisor = Evklid(top, bottom)
    
    # //= целочисленное деление с присваиванием
    top //= divisor
    bottom //= divisor

    if bottom < 0:
        top = -top
        bottom = -bottom

    if bottom == 1:
        return top
    
    else:
        return (f"{top}/{bottom}")


# 4.2
# комментарии написаны для меня как пояснение

# возвращаем только True/False
def point_in_circle(x: float, y: float, a: float, b: float, R: float) -> bool:
    """ Проверка лежит ли точка (x, y) внутри окружности (x-a)^2 + (y-b)^2 = R^2

    Параметры: \n
    x, y - координаты проверяемой точки \n
    a, b - координаты центра окружности \n
    R - радиус окружности
    
    """

    # сравнение квадрата расстояния с квадратом радиуса
    distanse_squared = (x-a)**2 + (y-b)**2

        # по условию точно внутри окружности поэтому строго <
    return distanse_squared < R**2

def count_points_in_circle(a:float, b: float, R: float, points: list):
    """Проверка лежат ли заданные условием точки Р(р1, р2), F(f1, f1), L(l1,l2) внутри окружности.
    
    Параметры: \n
    a, b - координаты центра окружности \n
    R - радиус окружности
    points - список точек, каждый элемент которого имеет вид ('название точки', x, y)    
    """

    print(f"Окружность: (x-{a})^2 + (y-{b})^2 = {R}^2")
    print("Проверяемые точки:")

    kol = 0

    for name, x, y in points:
        if point_in_circle(x, y, a, b, R):
            kol += 1
            status = "внутри"

        else:
            status = "снаружи"

        print(f"{name}, ({x}, {y}) - {status}")

    print(f"Кол-во точек внутри окружности: {kol}")

# 5
# 5.1

def simplyfy5(a:float, b:float, c:float, d:float):
    """Упрощение результата вычитания дробей до несократимого результата. Переменные a, b, c, d - float"""
    if b == 0 or d == 0:
        return "Ошибка: знаменатель равен нулю!"

    if c == 0:
        return (f"{a}/{b}")
    

    top = a * d - c * b
    bottom = b*d
            

    print(f"Изначальная дробь -- {top}/{bottom}")


    # делитель
    divisor = Evklid(top, bottom)
    
    # //= целочисленное деление с присваиванием
    top //= divisor
    bottom //= divisor

    if bottom < 0:
        top = -top
        bottom = -bottom

    if bottom == 1:
        return top
    
    else:
        return (f"{top}/{bottom}")

# 5.2
def divisors(num: int):
    for i in range(1, num):
        if num % i == 0:
            print(i, end=' ')



# 6
# 6.1
def NOK(a: float, b: float) -> float:   
    """НОК - наименьшее общее кратное"""
    return (a*b)/Evklid(a, b)

# 6.2
def S_convex_quadrilateral(a: float, b: float, c: float, d: float, q: float) -> float:
    """Площадь выпуклого четырехугольника по 4 сторонам и диагонали. Расчитывается путем сложения площадей двух треугольников.

    Переменные:
    a, b, c, d - Длины сторон четырехугольника
    q - длина диагонали
    """
    return S_triangle_Heron(a, b, q) + S_triangle_Heron(c, d, q)


# 7
# 7.1

# Не совсем понял задание
# Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его 
# площадь, если угол между сторонами длиной X и У — прямой. Использовать 
# две подпрограммы для вычисления площадей: прямоугольного треугольника и 
# прямоугольника. 

# Если речь идет о прямоугольной трапеции тогда решение будет следующим
def S_rectangular_trapezoid(x: float, y: float, z: float, t = sqrt(2**2 + 2**2)) -> float:
    """Площадь прямоугольной трапеции с использованием площадей прямоугольника и треугольника
    Переменные:
    x, y, z, t - стороны трапеции
    """
    # Находим самую длинную сторону - большое основание
    # Предположим что порядок сторон будет соблюдаться как в условии т.е. X > Y > Z > T
    # если угол между X и Y 90 градусов -> основаниями могут быть только X > Y > Z
    # Необходимо понять какие из сторон основания
    
    # По т. Геррона найдем примерное Т
    
    # 1 вариант Х - нижнее основание Y - высота
    diff1 = x - z
    T_expected1 = sqrt(diff1**2 + (y**2))
    
    # 2 вариант Y - нижнее основание X - высота
    diff2 = y - z
    T_expected2 = sqrt(diff2**2 + (x**2))

    # Выбираем вариант с меньщей погрешностью
    e1 = abs(T_expected1 - t)
    e2 = abs(T_expected2 - t)

    s1 = 0
    s2 = 0
    if e1 < e2:
        # 1 вариант Х - нижнее основание Y - высота
        s1 = S_rect(z, y)
        s2 = S_right_triangle(x-z, y)

    else:
        # 2 вариант Y - нижнее основание X - высота
        s1 = S_rect(z, x)
        s2 = S_right_triangle(y-z, x)
        
    return s1+s2

# Если речь идет о четырехугольнике в котором только 1 угол 90 градусов подпрограмма площади прямоугольника использоваться не будет
def task7_1(x: float, y: float, z: float, t: float) -> float:
    s1 = S_right_triangle(x, y)

    ac = sqrt(x**2 + y**2)
    s2 = S_triangle_Heron(ac, z, t)

    return round((s1 + s2), 3)


# 7.2
def octal_code(num: str):
    if int(num) > 0:
        s = []
        x = int(num, base=8)
        x = str(x)

        for i in x:
            s.append(i)
        
        s.reverse()

        while len(s) < 10:
            s.append('0')

        s.reverse()
        x = ''
        for i in s:
            x += i

        print(x)
    
    else:
        print("Введено отрицательное число")


# 8
# 8.1
def dividing_by_numbers(num: int):
    """Находит все натуральные числа, не превосходящие заданного n, которые 
делятся на каждую из своих цифр"""
    for i in range(1, num):
        tmp_list = []
        for k in str(i):
            tmp_list.append(int(k))
               
        for j in tmp_list:
            if j != 0:
                if i % j != 0:
                    is_dividing = False
                    break
                
                elif i % j == 0:
                    is_dividing = True

        if is_dividing == False:
            continue

        if is_dividing == True:
            print(i)


# 8.2
def moves_in_list(m):
    A = []

    for i in range(0, m):
        A.append(int(input(f"Число №{i+1}: ")))

    print(f"Исходный массив:\n{A}")

    tmp = A[0]
    A[0] = A[-1]
    A[-1] = tmp

    print(f"Преобразованный массив: {A}")

# 9
# 9.1
def nums(num: int) -> int:
    """Из заданного числа вычли сумму его цифр. Из результата вновь вычли 
сумму его цифр и т. д. Результат - кол-во шагов до получения 0 """
    kol = 0
    x = num
    while x > 0:
        s = str(x)
        tmp_list = list(s)
        for i in tmp_list:
            x -= int(i)
        kol += 1

    return kol

# 9.2
def mas_pow(mas) -> float:
    power = 1

    for i in mas:
        power *= i

    return power


# 10
# 10.1
def consists_from_nums(*array, n: int) -> int:
    """Вычисляет кол-во цисел в промеждутке [100, N] состоящих из цифр a, b, c"""
    kol = 0

    if len(array) == 3:
        for i in range(100, n+1):
            tmp_list = []
            for k in str(i):
                tmp_list.append(int(k))

            if sorted(tmp_list) == sorted(array):
                kol += 1
                print(i)
    
    else:
        print("Ошибка ввода")

    return kol


# 10.2
def reverse_words(s: str) -> str:

    tmp_list = s.split(' ')

    tmp_list = reversed(tmp_list)

    new_s = ' '.join(tmp_list)

    return new_s


# 11
# 11.1
def find_twins(n: int):
    """Выводит все пары близнецов на отрезке от n до 2n, где n - натуальное число > 2"""
    if n > 2:
        for i in range(n, (n*2)-1):
            print(i, i+2)


# 11.2
def max_in_matrix(matrix):
    max_value = matrix[0][0]

    for i in matrix:
        for j in i:
            if max_value < j:
                max_value = j

    return max_value


# 12
# 12.1
def sum_of_divisors(n: int):
    """Находит сумму делителей числа"""
    if n < 2:
        return 0
    
    total = 1

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            total += i
            
            if i != n // i:  # избегаем повторения для квадратов например 5|25
                total += n // i
    
    return total

def find_amicable_pairs(n):
    """Находит все пары дружественных чисел в диапазоне [2, N]."""
    if n < 220:
        return []
    
    pairs = []
    checked = set()     # множество чисел, которые уже проверили (чтобы не выводить пару дважды)
    
    for a in range(2, n + 1):
        if a in checked:    # если число уже было в какой-то паре - пропускаем
            continue

        b = sum_of_divisors(a)

        if b > a and b <= n:
            if sum_of_divisors(b) == a:
                pairs.append((a, b))
                checked.add(a)
                checked.add(b)
    
    return pairs

# 13
# 13.1
def armstrong_num(num: int, n: int) -> bool:
    """Проверяет является ли число num со степенью nчислом армстронга"""
    tmp_list = []
    for k in str(num):
        tmp_list.append(int(k))
    tmp_sum = 0

    for i in tmp_list:
        tmp_sum += (i**n)

    if tmp_sum == num:
        return True
    
    else:
        return False

# 13.2
def compute_angle(x, y):
    """Возвращает абсолютный угол (в радианах) между осью OX и вектором (x, y)."""
    return abs(atan2(y, x))

def find_min_angle_point(points):
    """
    points: список кортежей [(x1, y1), (x2, y2), ...]
    Возвращает точку с минимальным углом.
    """

    min_angle = float('inf')
    result_point = ()
    
    for (x, y) in points:
        angle = compute_angle(x, y)
        if angle < min_angle:
            min_angle = angle
            result_point = (x, y)
    
    return result_point

# 14
# 14.1
def kol_of_divisors(n: int) -> int:
    if n < 2:
        return 0
    
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += 1
    
    return total

def max_kol_of_divisors_in_range(m: int, n: int):
    list_of_nums = []
    max_kol = float("-inf")
    for i in range(m , n+1):
        if max_kol < kol_of_divisors(i):
            max_kol = kol_of_divisors(i)

    for i in range(m , n+1):
        if max_kol == kol_of_divisors(i):
            list_of_nums.append(i)

    print(f"Число делителей: {max_kol}")
    return list_of_nums

# 14.2
def distance(p1, p2):
    """     
    Возвращает евклидово расстояние между точками p1=(x1, y1) и p2=(x2, y2).
    """
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def find_max_distance(points):
    """
    Возвращает максимальное расстояние между любыми двумя точками из списка points.
    """
    max_dist = 0.0
    
    # Перебираем все уникальные пары точек
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist > max_dist:
                max_dist = dist
    
    return max_dist

# 15
# 15.1
def palindrom_bit(n) -> bool:
    binnary = bin(n)[2:] #Запись без '0b'
    if binnary == binnary[::-1]:
        return True
    
    else:
        return False

# 15.2
def find_min_distance(points):
    """
    Возвращает максимальное расстояние между любыми двумя точками из списка points.
    """
    min_dist = float('inf')

    # Перебираем все уникальные пары точек
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    
    return min_dist

# 1
print("""
Задание 1
1. Составить программу для вычисления площади разных геометрических 
фигур.  
2. Даны 3 различных массива целых чисел (размер каждого не превышает 
15). В каждом массиве найти сумму элементов и среднеарифметическое 
значение. """)

print("1.1")
print('-'*60)
print(f"Площадь круга r = 2: {round(S_circle(2), 4)}")
print(f"Площадь прямоугольника со сторонами a = 2, b = 3: {S_rect(2, 3)}")
print(f"Площадь квадрата со стороной a = 5: {S_square(5)}")
print(f"Площадь треугольника через высоту(h = 4) и сторону(a = 3): {S_triangle_side(3, 4)}")
print(f"Площадь прямоугольного треугольника через 2 стороны a = 2, b = 3: {S_right_triangle(2, 3)}")
print(f"Площадь треугольника по теореме Герона со сторонами a = 2, b = 3, c = 4: {S_triangle_Heron(2, 3, 4)}")
print('-'*60)

print()
print("1.2")
l1, l2, l3 = [], [], []

print('-'*60)
print(f"Массив №1")
n = int(input("Введите размер массива (<15): "))
if n > 15:
    print("Ошибка ввода, размер массива > 15")

else:
    for i in range(0, n):
        l1.append(float(input(f"Число №{i+1}: ")))

    
    print(f"Максимальное значение массива №1: {max(l1)}; Среднее арифместическое: {avg(l1)}")


print(f"Массив №2")
n = int(input("Введите размер массива (<15): "))
if n > 15:
    print("Ошибка ввода, размер массива > 15")

else:
    for i in range(0, n):
        l2.append(float(input(f"Число №{i+1}: ")))
    
    print(f"Максимальное значение массива №2: {max(l2)}; Среднее арифместическое: {avg(l2)}")



print(f"Массив №3")
n = int(input("Введите размер массива (<15): "))
if n > 15:
    print("Ошибка ввода, размер массива > 15")

else:
    for i in range(0, n):
        l3.append(float(input(f"Число №{i+1}: ")))
    
    print(f"Максимальное значение массива №3: {max(l3)}; Среднее арифместическое: {avg(l3)}")


print('-'*60)

# 2
print("""
Задание 2
1. Вычислить площадь правильного шестиугольника со стороной а, 
используя подпрограмму вычисления площади треугольника.  
2. Пользователь вводит две стороны трех прямоугольников. Вывести их 
площади.   
""")

# 2.1
print("2.1")
print('-'*60)

a = float(input("Введите сторону a правильного треугольника: "))

print(f"Площадь правильного шестиугольника: {round(S_hexagon(a), 4)}")

print('-'*60)
print()

# 2.2
print("2.2")
print('-'*60)

for i in range(0, 3):
    print(f"Данные для прямоугольнрика №{i+1}")

    a = float(input("Введите первую сторону прямоугольника: "))
    b = float(input("Введите вторую сторону прямоугольника: "))
    
    print(f"Площать прямоугольника №{i+1}: {S_rect(a, b)}")
    
print('-'*60)
print()


# 3
print("""
Задание 3
1. Даны катеты двух прямоугольных треугольников. Написать функцию 
вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из 
гипотенуз больше, а какая меньше.  
2. Преобразовать строку так, чтобы буквы каждого слова в ней были 
отсортированы по алфавиту.   
""")

# 3.1
print("3.1")
print('-'*60)
print("Треугольник №1")
a1 = float(input("Введите катет а: "))
b1 = float(input("Введите катет b: "))

print(f"Гипотенуза 1 треугольника: {Hypotenuse(a1, b1)}")

print("Треугольник №1")
a2 = float(input("Введите катет а: "))
b2 = float(input("Введите катет b: "))

print(f"Гипотенуза 2 треугольника: {Hypotenuse(a2, b2)}")

print(f"Большая гипотенуза: {max(Hypotenuse(a1, b1), Hypotenuse(a2, b2))}")
print(f"Меньшая гипотенуза: {min(Hypotenuse(a1, b1), Hypotenuse(a2, b2))}")
print('-'*60)


# 3.2
print("3.2")
print('-'*60)
s = input("Введите строку: ")
print(str_sort(s))
print('-'*60)


print("""
Задание 4
1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить 
программу деления дроби на дробь. Ответ должен быть несократимой дробью. 
Использовать подпрограмму алгоритма Евклида для определения НОД.  
2. Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2). 
Выяснить и вывести на экран, сколько точек лежит внутри окружности.  
Проверку, лежит ли точка внутри окружности, оформить в виде процедуры.     
""")

# 4.1
print("4.1")
print('-'*60)
data1 = input("Введите первую дробь в формате 'a/b': ")
data2 = input("Введите вторую дробь в формате 'c/d': ")
try:
    a, b = data1.split('/')
    c, d = data2.split('/')
    
    a, b, c, d = float(a), float(b), float(c), float(d),
    
    print(f"Деление дробей ({data1}) / ({data2}) -----> {simplyfy4(a, b, c, d)}")     # для 1/2  3/4 результат 3/2

except:
    print(TypeError)
    print("Ошибка ввода")
    




# 4.2
print("4.2")
print('-'*60)

# Параметры для проверки 
# a, b = 2.0, 3.0  # центр
# R = 5.0          # радиус
# points = [
#         ("P", 1.0, 2.0),   
#         ("F", 4.0, 4.0),   
#         ("L", 6.0, 1.0)   
#     ]


a = float(input("Введите координату X центра окружности: "))
b = float(input("Введите координату Y центра окружности: "))
R = float(input("ВВедите радиус окружности: "))
x1 = float(input("Введите x для точки P: "))
y1 = float(input("Введите y для точки P: "))
x2 = float(input("Введите x для точки F: "))
y2 = float(input("Введите y для точки F: "))
x3 = float(input("Введите x для точки L: "))
y3 = float(input("Введите y для точки L: "))


points = [
        ("P", x1, y1),   
        ("F", x2, y2),   
        ("L", x3, y3)   
    ]
count_points_in_circle(a, b, R, points)
print('-'*60)


print("""
Задание 5
1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить 
программу вычитания из первой дроби второй. Ответ должен быть 
несократимой дробью. Использовать подпрограмму алгоритма Евклида для 
определения НОД.  
2. Напишите программу, которая выводит в одну строчку все делители 
переданного ей числа, разделяя их пробелами.     
""")


# 5.1
print("5.1")
print('-'*60)

data1 = input("Введите первую дробь в формате 'a/b': ")
data2 = input("Введите вторую дробь в формате 'c/d': ")

try:
    a, b = data1.split('/')
    c, d = data2.split('/')

    a, b, c, d = float(a), float(b), float(c), float(d),

    print(f"Вычитание дробей ({data1}) / ({data2}) -----> {simplyfy5(a, b, c, d)}")         # simplyfy5(3, 4, 2, 5)     # результат 7/20

except:
    print("Ошибка ввода")
print('-'*60)


# 5.2
print("5.2")
print('-'*60)
n = int(input("Введите число для проверки: "))
print("Все делители данного числа:")
divisors(n)
print()
print('-'*60)

# 6
print("""
Задание 6
1. Составить программу нахождения наибольшего общего делителя (НОД) и 
наименьшего общего кратного (НОК) двух натуральных чисел НОК(А, В) = 
(A*B)/НОД(A,B). Использовать подпрограмму алгоритма Евклида для 
определения НОД.  
2. Cоставить программу вычисления площади выпуклого четырехугольника, 
заданного длинами четырех сторон и диагонали.
""")

# 6.1
print("6.1")
print('-'*60)

a = float(input("Введите А: "))
b = float(input("Введите B: "))

print(f"НОД: {Evklid(a, b)}")
print(f"НОК: {NOK(a, b)}")

print('-'*60)

# 6.2
print("6.2")
print('-'*60)
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
d = float(input("Введите длину стороны d: "))
q = float(input("Введите длину диагонали q: "))

print(f"Площадь выпуклого четырехугольника: {S_convex_quadrilateral(a, b, c, d, q)}")
print('-'*60)

# 7
print("""
Задание 7
1. Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его 
площадь, если угол между сторонами длиной X и У — прямой. Использовать 
две подпрограммы для вычисления площадей: прямоугольного треугольника и 
прямоугольника.  
2. Напишите программу, которая переводит переданное ей 
неотрицательное целое число в 10-значный восьмеричный код, сохранив 
лидирующие нули.   
""")

# 7.1
print("7.1")
print('-'*60)

print("Решение с прямоугольной трапецией:")
x = float(input("Введите длину стороны X:"))    # x = 5
y = float(input("Введите длину стороны Y:"))    # y = 2
z = float(input("Введите длину стороны Z:"))    # z = 3
print(f"Площадь прямоугольной трапеции: {S_rectangular_trapezoid(x, y, z)}")  # результат = 8 пример из интернета

print("Решение с четырехугольником:")           # пример
x = float(input("Введите длину стороны X:"))    # x = 1
y = float(input("Введите длину стороны Y:"))    # y = 4 
z = float(input("Введите длину стороны Z:"))    # z = 3 
t = float(input("Введите длину стороны T:"))    # t = 5

print(f"Площадь четырехугольника: {task7_1(x, y, z, t)}")  # пример - 8.18
print('-'*60)


# 7.2
print("7.2")
print('-'*60)
n = str(input("Введите число для проверки: ")) 
octal_code(n)
print('-'*60)



# 8
print("""
Задание 8
1. Найти все натуральные числа, не превосходящие заданного n, которые 
делятся на каждую из своих цифр.  
2. Ввести одномерный массив A длиной m. Поменять в нём местами первый 
и последний  элементы. Длину массива и его элементы ввести с клавиатуры. В 
программе описать процедуру для замены элементов массива. Вывести 
исходные и полученные массивы.   
""")

# 8.1
print("8.1")
print('-'*60)
n = int(input("Введите число n: "))
print("Числа, которые делятся на каждую из своих цифр")
dividing_by_numbers(n)
print('-'*60)

# 8.2
print("8.2")
print('-'*60)
m = int(input("Кол-во элементов в массиве: "))
moves_in_list(m)
print('-'*60)




# 9
print("""
Задание 9
1. Из заданного числа вычли сумму его цифр. Из результата вновь вычли 
сумму его цифр и т. д. Через сколько таких действий получится нуль?  
2. Даны 3 различных массива целых чисел. В каждом массиве найти 
произведение элементов и среднеарифметическое значение.    
""")

# 9.1
print("9.1")
print('-'*60)
n = int(input("Введите число для расчета: "))
print(f"Кол-во действий для досижения значения 0: {nums(n)}")
print('-'*60)

# 9.2
print("9.2")
print('-'*60)

l1, l2, l3 = [], [], []

print(f"Массив №1")
n = int(input("Введите размер массива: "))

for i in range(0, n):
    l1.append(float(input(f"Число №{i+1}: ")))


print(f"Произведение значений массива №1: {mas_pow(l1)}; Среднее арифместическое: {avg(l1)}")


print(f"Массив №2")
n = int(input("Введите размер массива: "))

for i in range(0, n):
    l2.append(float(input(f"Число №{i+1}: ")))

print(f"Произведение значений массива №2: {mas_pow(l2)}; Среднее арифместическое: {avg(l2)}")



print(f"Массив №3")
n = int(input("Введите размер массива: "))
    
for i in range(0, n):
    l3.append(float(input(f"Число №{i+1}: ")))

print(f"Произведение значений массива №3: {mas_pow(l3)}; Среднее арифместическое: {avg(l3)}")


print('-'*60)


# 10
print("""
Задание 10
1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных 
из цифр а, b, с.  
2. Составить программу, которая изменяет последовательность слов в 
строке на обратную.  
""")

# 10.1
print("10.1")
print('-'*60)

a =int(input("Введите цифру a: "))
b =int(input("Введите цифру b: "))
c =int(input("Введите цифру c: "))
n =int(input("Введите конец отрезка n: "))

print(f"Кол-во чисел, составленных из введенных цифр: {consists_from_nums(a, b, c, n = n)}")
print('-'*60)


# 10.2
print("10.2")
print('-'*60)
s = input("Введите строку для редактирования: ")
print("Отредактированная строка")
print(reverse_words(s))
print('-'*60)


# 11
print("""
Задание 11
1. Два простых числа называются «близнецами», если они отличаются друг 
от друга на 2 (например, 41 и 43). Напечатать все пары «близнецов» из отрезка 
[n, 2n], где n — заданное натуральное число, большее 2..  
2. Даны две матрицы А и В. Написать программу, меняющую местами 
максимальные элементы этих матриц. Нахождение максимального элемента 
матрицы оформить в виде процедуры.  
""")

# 11.1
print("11.1")
print('-'*60)

n = int(input("Введите n: "))
print("Вывод всех пар близнецов на отрезке [n, 2n]")
find_twins(n)
print('-'*60)


# 11.2
print("11.2")
print('-'*60)
matrix1 =   [  
                [1, 2, 3],
                [2, 10, 4],
                [5, 6, 1]
            ]

matrix2 =   [
                [3, 10, 14],
                [4, 11, 13],
                [1, 25, 9],
            ]

print("Матрица 1")
for i in matrix1:
    print(i)

print("Матрица 2")
for i in matrix2:
    print(i)

print(f"Максимальное число в матрице №1:{max_in_matrix(matrix1)}")
print(f"Максимальное число в матрице №2: {max_in_matrix(matrix2)}")

max_in_m1 = max_in_matrix(matrix1)
max_in_m2 = max_in_matrix(matrix2)

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] == max_in_m1:
            matrix1[i][j] = max_in_m2

for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        if matrix2[i][j] == max_in_m2:
            matrix2[i][j] = max_in_m1

print()

print("Измененная матрица 1")
for i in matrix1:
    print(i)



print("Измененная матрица 2")
for i in matrix2:
    print(i)
    
print('-'*60)


# 12
print("""
Задание 12
1. Два натуральных числа называются «дружественными», если каждое из 
них равно сумме всех делителей (кроме его самого) другого (например, числа 
220 и 284). Найти все пары «дружественных» чисел, которые не больше 
данного числа N.  
2. Даны длины сторон треугольника a, b, c. Найти медианы треугольника, 
сторонами которого являются медианы исходного треугольника. Для 
вычисления медианы проведенной к стороне а, использовать формулу 
Вычисление медианы оформить в виде процедуры.  
""")

# 12.1
print("12.1")
print('-'*60)

n = int(input("Введите n: "))
result = find_amicable_pairs(n)
    
if result:
    print(f"Пары дружественных чисел до {n}:")
    for a, b in result:
        print(f"{a} и {b} (сумма делителей {a} = {b}, сумма делителей {b} = {a})")
else:
    print(f"Дружественных чисел до {n} не найдено.")

print('-'*60)



# 12.2
print("12.2")
print('-'*60)
def median(side: float, a: float, b: float) -> float:
    """
    Возвращает длину медианы, проведённой к стороне side, где a и b — две другие стороны треугольника.
    """
    return  0.5 * sqrt(2 * (a**2 + b**2) - side**2)

# # 12.2
a = 3
b = 4
c = 5

# Медианы исходного треугольника
m_a = median(a, b, c)  # медиана к стороне a
m_b = median(b, a, c)  # медиана к стороне b
m_c = median(c, a, b)  # медиана к стороне c

print(f"\nМедианы исходного треугольника:")
print(f"m_a = {m_a:.6f}")
print(f"m_b = {m_b:.6f}")
print(f"m_c = {m_c:.6f}")

# Проверка существования треугольника из медиан
if m_a + m_b <= m_c or m_a + m_c <= m_b or m_b + m_c <= m_a:
    print("Треугольник из медиан не существует.")

# Медианы треугольника, составленного из медиан исходного
mm_a = median(m_a, m_b, m_c)  # медиана к стороне m_a нового треугольника
mm_b = median(m_b, m_a, m_c)  # медиана к стороне m_b
mm_c = median(m_c, m_a, m_b)  # медиана к стороне m_c

print(f"\nМедианы треугольника из медиан исходного:")
print(f"mm_a = {mm_a:.6f}")
print(f"mm_b = {mm_b:.6f}")
print(f"mm_c = {mm_c:.6f}")

print('-'*60)


# 13
print("""
Задание 13
1. Натуральное число, в записи которого n цифр, называется числом 
Армстронга, если сумма его цифр, возведенная в степень n, равна самому 
числу. Найти все числа Армстронга от 1 до к.  
2. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
Найти и напечатать координаты точки, для которой угол между осью абсцисс и 
лучом, соединяющим начало координат с точкой, минимальный. Вычисления 
оформить в виде процедуры.  
""")

# 13.1
print("13.1")
print('-'*60)

k = int(input("Введите k: "))
n = int(input("Введите степень n: "))

print(f"Числа Армстронга на отрезке [1, {k}]:")

for i in range(1, k):
    if armstrong_num(i, n):
        print(i)
        
print('-'*60)


# 13.2
print("13.2")
print('-'*60)

x1 = float(input("Введите x1 для точки X: "))
y1 = float(input("Введите y1 для точки X: "))
x2 = float(input("Введите x2 для точки Y: "))
y2 = float(input("Введите y2 для точки Y: "))
x3 = float(input("Введите x3 для точки Z: "))
y3 = float(input("Введите y3 для точки Z: "))

points = [(x1, y1), (x2, y2), (x3, y3)]

# Находим точку с минимальным углом
min_point = find_min_angle_point(points)

print(f"\nТочка с минимальным углом между осью OX и лучом из (0,0):")
print(f"{min_point}")

print('-'*60)


# 14
print("""
Задание 14
1. Составить программу для нахождения чисел из интервала [М, N], имеющих 
наибольшее количество делителей.  
2.Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, 
p2). Выяснить, какие из них находятся на максимальном расстоянии друг от 
друга и вывести на экран значение этого расстояния. Вычисление расстояния 
между двумя точками оформить в виде процедуры.   
""")

# 14.1
print("14.1")
print('-'*60)

m = int(input("Начало отрезка m: "))
n = int(input("Конец отрезка n: "))

print("Элементы с самым большим кол-вом делителей: ")
for i in max_kol_of_divisors_in_range(m, n):
    print(i, end=' ')
print()

print('-'*60)


# 14.2

# тест
# Точка X: (0, 0)
# Точка Y: (3, 0)
# Точка Z: (0, 4)
# Точка P: (3, 4)
# Результат 5

print("14.2")
print('-'*60)
x1 = float(input("Введите x1 для точки X: "))
y1 = float(input("Введите y1 для точки X: "))

x2 = float(input("Введите x2 для точки Y: "))
y2 = float(input("Введите y2 для точки Y: "))

x3 = float(input("Введите x3 для точки Z: "))
y3 = float(input("Введите y3 для точки Z: "))

x4 = float(input("Введите x4 для точки P: "))
y4 = float(input("Введите y4 для точки P: "))

points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

max_dist = find_max_distance(points)

print(f"\nМаксимальное расстояние между двумя из данных точек: {max_dist:.6f}")
print('-'*60)


print("""
Задание 15
1. Составить программу для нахождения чисел из интервала [М, N], имеющих 
наибольшее количество делителей.  
2.Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, 
p2). Выяснить, какие из них находятся на максимальном расстоянии друг от 
друга и вывести на экран значение этого расстояния. Вычисление расстояния 
между двумя точками оформить в виде процедуры.   
""")

# 15.1
print("15.1")
print('-'*60)

n = int(input("Введите число n: "))
for i in range(0, n):
    if palindrom_bit(i):
        print(i)

print('-'*60)


# 15.2
# тест
# Точка X: (0, 0)
# Точка Y: (3, 0)
# Точка Z: (0, 4)
# Точка T: (3, 4)
# Результат 3

print("15.1")
print('-'*60)

x1 = float(input("Введите x1 для точки X: "))
y1 = float(input("Введите y1 для точки X: "))

x2 = float(input("Введите x2 для точки Y: "))
y2 = float(input("Введите y2 для точки Y: "))

x3 = float(input("Введите x3 для точки Z: "))
y3 = float(input("Введите y3 для точки Z: "))

x4 = float(input("Введите x4 для точки T "))
y4 = float(input("Введите y4 для точки T: "))

points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

min_dist = find_min_distance(points)

print(f"\nМинимальное расстояние между двумя из данных точек: {min_dist:.6f}")
print('-'*60)
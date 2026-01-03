from math import * # type: ignore

# # Практическая работа №8
# Чайкин А. У-255


# #1

# # 1.1
# def S_circle(r: float): 
#     """Площадь круга"""
#     return pi*(r**2)

def S_rect(a:float, b: float):
    """Площадь прямоугольника"""
    return a*b

# def S_square(a: float):
#     """Площадь квадрата"""
#     return a**2

# def S_triangle_side(a: float, h: float):
#     """Площадь треугольника через высоту(h) и сторону(a). Можно использовать как для равностороннего так и прямоугольного треугольника."""
#     return 0.5 * a * h

def S_right_triangle(a: float, b: float):
    """Площадь прямоугольного треугольника через 2 стороны
    Переменные: 
    a, b - катеты
    """
    return (a*b)/2

# def S_triangle_1sin(a: float, b: float, corner: float):
#     """Площадь треугольника через 2 стороны (a, b) и sin угла между ними(corner)"""
#     return 0.5*a*b*sin(corner)

# def S_triangle_2sin(a: float, b: float, side: float):
#     """Площадь треугольника через 2 sin углов и сторону между ними"""
#     return ((a**2) * (sin(a) * sin(b))/2 * sin(a+b))

def S_triangle_Heron(a: float, b: float, c: float):
    """Площадь треугольника по теореме Герона"""
    p = (a + b + c)/2
    return (sqrt(p * (p-a) * (p-b) * (p-c)))

# # 1.2
# def avg(mas):
#     """Среднее арифметическое массива"""
#     return (sum(mas)/len(mas))


# # 2
# # 2.1
# def S_hexagon(a: float):
#     """S шестиугольника через S треугольника"""
#     return 6 * S_triangle_Heron(a, a, a)


# # 3
# # 3.1
# def Hypotenuse(a: float, b: float):
#     """Формула гипотенузы"""
#     return sqrt(a**2 + b**2)

# # 3.2
# def str_sort(s: str):
#     s_tmp = sorted(s)
#     s_new = ''
#     for i in s_tmp:
#         s_new += str(i)
#     return s_new

# # 4
# # 4.1
# # комментарии написаны для меня как пояснение

def Evklid(a: float, b: float):
    """НОД"""
    while b != 0:           # Пока второе число не станет нулём
        a, b = b, a % b     # a получает старое значение b, 
                            # b получает остаток от деления a на b
    return abs(a)           # Возвращаем абсолютное значение a (НОД)

# def simplyfy4(a:float, b:float, c:float, d:float):
#     """Упрощение результата деления дробей до несократимого результата. Переменные a, b, c, d - float"""
#     if b == 0 or d == 0:
#         return "Ошибка: знаменатель равен нулю!"

#     if c == 0:
#         return "Ошибка: нулевая дробь!"
    
#     # при делении перемножение крест на крест X
#     top = a*d
#     bottom = b*c

#     # делитель
#     divisor = Evklid(top, bottom)
    
#     # //= целочисленное деление с присваиванием
#     top //= divisor
#     bottom //= divisor

#     if bottom < 0:
#         top = -top
#         bottom = -bottom

#     if bottom == 1:
#         return top
    
#     else:
#         return (f"{top}/{bottom}")


# # 4.2
# # комментарии написаны для меня как пояснение

# # возвращаем только True/False
# def point_in_circle(x: float, y: float, a: float, b: float, R: float) -> bool:
#     """ Проверка лежит ли точка (x, y) внутри окружности (x-a)^2 + (y-b)^2 = R^2

#     Параметры: \n
#     x, y - координаты проверяемой точки \n
#     a, b - координаты центра окружности \n
#     R - радиус окружности
    
#     """

#     # сравнение квадрата расстояния с квадратом радиуса
#     distanse_squared = (x-a)**2 + (y-b)**2

#         # по условию точно внутри окружности поэтому строго <
#     return distanse_squared < R**2

# def count_points_in_circle(a:float, b: float, R: float, points: list):
#     """Проверка лежат ли заданные условием точки Р(р1, р2), F(f1, f1), L(l1,l2) внутри окружности.
    
#     Параметры: \n
#     a, b - координаты центра окружности \n
#     R - радиус окружности
#     points - список точек, каждый элемент которого имеет вид ('название точки', x, y)    
#     """

#     print(f"Окружность: (x-{a})^2 + (y-{b})^2 = {R}^2")
#     print("Проверяемые точки:")

#     kol = 0

#     for name, x, y in points:
#         if point_in_circle(x, y, a, b, R):
#             kol += 1
#             status = "внутри"

#         else:
#             status = "снаружи"

#         print(f"{name}, ({x}, {y}) - {status}")

#     print(f"Кол-во точек внутри окружности: {kol}")

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
def S_rectangular_trapezoid(x: float, y: float, z: float, t: float) -> float:
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

# # 8.2
# m = int(input("Кол-во элементов в массиве: "))
# moves_in_list(m)



# # 8.1
# dividing_by_numbers(20)

        











# # 4.1 тест значения 
# print(f"Деление дробей 3/4 и 1/2 -----> {simplyfy4(3, 4, 1, 2)}")     # результат 3/2


# # 4.2
# # Параметры окружности
# a, b = 2.0, 3.0  # центр
# R = 5.0          # радиус

# points = [
#         ("P", 1.0, 2.0),   
#         ("F", 4.0, 4.0),   
#         ("L", 6.0, 1.0)   
#     ]

# count_points_in_circle(a, b, R, points)



# # 5.1
# print("Вычитание дробей 3/4 и 2/5")
# simplyfy5(3, 4, 2, 5)     # результат 7/20



# # 7.1 прямоугольная трапеция
# print(f"Площадь прямоугольной трапеции: {S_rectangular_trapezoid(5, 2, 3, sqrt(2**2 + 2**2))}")  # результат = 8 пример из интернета
# print(f"Площадь четырехугольника: {task7_1(1, 4, 3, 5)}")


# # 7.2
# octal_code('111')
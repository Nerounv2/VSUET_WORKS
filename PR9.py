from copy import deepcopy

def input_matrix(n, m):
    matrix = []
    for i in range(0, n):
        tmp_mas = []
        print(f"Введите данные для строки № {i+1}: ")
        for j in range(0, m):
            tmp_mas.append(int(input(f"Введите число №{j+1}: ")))
        
        matrix.append(tmp_mas)
    
    return matrix

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(f"{j}", end=' ')
        print()

def max_in_matrix(matrix):
    tmp_max = matrix[0][0]
    for i in range(0, len(matrix)):        
        for j in range(0, len(matrix[i])):
            if tmp_max < matrix[i][j]:
                tmp_max = matrix[i][j]

    return tmp_max



# # 1
# # 1.1
# print("""
# Задание 1
# 1. Вычислить сумму и число положительных элементов матрицы A[N, 
# N], находящихся над главной диагональю.  
# 2. Дана матрица B[N, М]. Найти в каждой строке матрицы 
# максимальный и минимальный элементы и поменять их с первым и 
# последним элементами строки соответственно.  
# """)

# # 1.1
# print("1.1")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# print("Исходная матрица")
# print_matrix(matrix)

# kol = 0
# s = 0
# for i in range(0, n):
#     for j in range(0, n):
#         if i==j:
#             if matrix[i][j] > 0:
#                 kol += 1   
#                 s += matrix[i][j]

# print(f"Кол-во положительных элементов на главной диагонали: {kol}")
# print(f"Сумма положительных элементов на главной диагонали: {s}")
# print('-'*60)


# # 1.2
# print("1.2")
# print('-'*60)
# n = int(input("Введите кол-во строк для матрицы: "))
# m = int(input("Введите кол-во столбцов для матрицы: "))

# matrix = input_matrix(n, m)

# print("Исходная матрица")
# print_matrix(matrix)

# for i in range(0, n):
#     max_value = max(matrix[i])
#     min_value = min(matrix[i])

#     matrix[i][0] = max_value
#     matrix[i][-1] = min_value

# print("Измененная матрица: ")
# print_matrix(matrix)

# print('-'*60)



# # 2
# # 2.1
# print("""
# Задание 2
# 1. Дана целая квадратная матрица n-го порядка. Определить, 
# является ли она магическим квадратом, т. е. такой матрицей, в которой 
# суммы элементов во всех строках и столбцах одинаковы.  
# 2. Дана прямоугольная матрица A[N, N]. Переставить первый и 
# последний столбцы местами и вывести на экран. 
# """)

# # 2.1
# print("2.1")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# print("Исходная матрица")
# print_matrix(matrix)


# is_magic = True
# for i in range(1, n):
#     tmp_prev_set = set(matrix[i-1])
#     tmp_set = set(matrix[i])

#     if len(tmp_set) == 1 and tmp_set == tmp_prev_set:
#         is_magic = True

#     else:
#         is_magic = False
#         break
       
# if is_magic:
#     print("Матрица - магический квадрат")

# else:
#     print(print("Матрица - не магический квадрат"))
    
# print('-'*60)


# # 2.2
# print("2.2")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# print("Исходная матрица")
# print_matrix(matrix)

# for i in range(0, n):
#     tmp_value = matrix[i][0]
#     matrix[i][0] = matrix[i][-1]
#     matrix[i][-1] = tmp_value

# print("Измененная матрица: ")
# print_matrix(matrix)

# print('-'*60)

# # 3
# print("""
# Задание 3
# 1. Определить, является ли заданная целая квадратная матрица n-го 
# порядка симметричной (относительно главной диагонали).  
# 2. Дана вещественная матрица размером n х m. Переставляя ее 
# строки и столбцы, добиться того, чтобы наибольший элемент (или один 
# из них) оказался в верхнем левом углу.   
# """)

# # 3.1
# print("3.1")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# print("Исходная матрица")
# print_matrix(matrix)


# is_simmetric = True
# for i in range(0, n):
#     for j in range(0, n):
#         if matrix[i][j] == matrix[j][i]:
#             is_simmetric = True

#         else:
#             is_simmetric = False
#             break

# if is_simmetric:
#     print("Матрица симметрична")

# else:
#     print(print("Матрица не симметрична"))
    
# print('-'*60)


# # 3.2
# print("3.2")
# print('-'*60)
# n = int(input("Введите кол-во строк для матрицы: "))
# m = int(input("Введите кол-во столбцов для матрицы: "))

# matrix = input_matrix(n, m)

# print("Исходная матрица")
# print_matrix(matrix)


# tmp_value = matrix[0][0]
# m = max_in_matrix(matrix)
# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         if matrix[i][j] == m:
#             matrix[i][j] = tmp_value

# matrix[0][0] = m

# print("Измененная матрица: ")
# print_matrix(matrix)

# print('-'*60)


# 4
# print("""
# Задание 4
# 1. Дана прямоугольная матрица. Найти строку с наибольшей и строку 
# с наименьшей суммой элементов. Вывести на печать найденные строки и 
# суммы их элементов.  
# 2. Дана квадратная матрица A[N, N], Записать на место 
# отрицательных элементов матрицы нули, а на место положительных — 
# единицы.  
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде.    
# """)

# # 4.1
# print("4.1")
# print('-'*60)
# n = int(input("Введите кол-во строк для матрицы: "))
# m = int(input("Введите кол-во столбцов для матрицы: "))

# matrix = input_matrix(n, m)

# print("Исходная матрица")
# print_matrix(matrix)

# max_sum = float("-inf")
# min_sum = float("inf")
# for i in matrix:
#     if sum(i) > max_sum:
#         max_sum = sum(i)

#     elif sum < min_sum:
#         min_sum = sum(i)

# for i in matrix:
#     if sum(i) == max_sum:
#         print(f"Строка с максимальной суммой элементов {max_sum}: {i}")
    
#     elif sum(i) == min_sum:
#         print(f"Строка с минимальной суммой элементов {max_sum}: {i}")
# print('-'*60)


# # 4.2

# print("4.2")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# # Копировать значения а не создавать ссылку на объект
# matrix2 = deepcopy(matrix)

# print("Исходная матрица")
# print_matrix(matrix)


# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         if j > i:
#             matrix[i][j] = 0

# print("Нижняя треугольная матрица")
# print_matrix(matrix)


# for i in range(0, len(matrix2)):
#     for j in range(0, len(matrix2[i])):
#         if matrix2[i][j] <= 0:
#             matrix2[i][j] = 0

#         else:
#             matrix2[i][j] = 1

# print("Измененная матрица")
# print_matrix(matrix2)

# print('-'*60)


# 5
# print("""
# Задание 5
# 1. Упорядочить по возрастанию элементы каждой строки матрицы 
# размером n х m.  
# 2. Дана действительная матрица размером n х m, все элементы 
# которой различны. В каждой строке выбирается элемент с наименьшим 
# значением. Если число четное, то заменяется нулем, нечетное - 
# единицей. Вывести на экран новую матрицу. 
# """)

# print("5.1")
# print('-'*60)
# n = int(input("Введите кол-во строк для матрицы: "))
# m = int(input("Введите кол-во столбцов для матрицы: "))

# matrix = input_matrix(n, m)

# print("Исходная матрица")
# print_matrix(matrix)

# for i in range(0, len(matrix)):
#     matrix[i] = sorted(matrix[i])


# print("Измененная матрица")
# print_matrix(matrix)

# print('-'*60)

# print("5.2")
# print('-'*60)
# n = int(input("Введите кол-во строк для матрицы: "))
# m = int(input("Введите кол-во столбцов для матрицы: "))

# matrix = input_matrix(n, m)

# print("Исходная матрица")
# print_matrix(matrix)

# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         if  matrix[i][j] == min(matrix[i]):
#             if min(matrix[i]) % 2 == 0:
#                 matrix[i][j] = 0
            
#             elif min(matrix[i]) % 2 != 0:
#                 matrix[i][j] = 1


# print("Измененная матрица")
# print_matrix(matrix)

# print('-'*60)


# 6
print("""
Задание 6
1. Дана целочисленная квадратная матрица. Найти в каждой строке 
наибольший элемент и в каждом столбце наименьший. Вывести на 
экран.  
2. Дана действительная квадратная матрица порядка N (N — 
нечетное), все элементы которой различны. Найти наибольший элемент 
среди стоящих на главной и побочной диагоналях и поменять его 
местами с элементом, стоящим на пересечении этих диагоналей. 
""")

# print("6.1")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

# matrix = input_matrix(n, n)

# print("Исходная матрица")
# print_matrix(matrix)

# for i in range(0, len(matrix)):
#     print(f"Наибольший элемент в строке №{i+1}: {max(matrix[i])}")

# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         matrix[i][j] = matrix[j][i]

# for i in range(0, len(matrix)):
#     print(f"Наименьший элемент в столбце №{i+1}: {min(matrix[i])}")

# print('-'*60)


# print("6.2")
# print('-'*60)
# n = int(input("Введите кол-во строк/столбцов для квадратной матрицы (нечетное): "))
# if n % 2 != 0:
#     matrix = input_matrix(n, n)

#     print("Исходная матрица")
#     print_matrix(matrix)

#     tmp_max = float("-inf")

#     for i in range(0, len(matrix)):
#         for j in range(len(matrix[i])):
#             if i == j:
#                 if tmp_max < matrix[i][j]: 
#                     tmp_max = matrix[i][j]

#     j = len(matrix[0])-1
#     for i in range(0, len(matrix)):
#         if tmp_max < matrix[i][j]:
#             tmp_max = matrix[i][j]
        
#         j-=1

#     mid = int(n/2)

#     matrix[mid][mid] = tmp_max

#     print("Измененная матрица")
#     print_matrix(matrix)

# elif n % 2 == 0:
#     print("Ошибка. Введено четное число")

# print('-'*60)



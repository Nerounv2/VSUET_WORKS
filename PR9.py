from copy import deepcopy
from numpy import trace

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



# 1
# 1.1
print("""
Задание 1
1. Вычислить сумму и число положительных элементов матрицы A[N, 
N], находящихся над главной диагональю.  
2. Дана матрица B[N, М]. Найти в каждой строке матрицы 
максимальный и минимальный элементы и поменять их с первым и 
последним элементами строки соответственно.  
""")

# 1.1
print("1.1")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

kol = 0
s = 0
for i in range(0, n):
    for j in range(0, n):
        if i==j:
            if matrix[i][j] > 0:
                kol += 1   
                s += matrix[i][j]

print(f"Кол-во положительных элементов на главной диагонали: {kol}")
print(f"Сумма положительных элементов на главной диагонали: {s}")
print('-'*60)


# 1.2
print("1.2")
print('-'*60)
n = int(input("Введите кол-во строк для матрицы: "))
m = int(input("Введите кол-во столбцов для матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

for i in range(0, n):
    max_value = max(matrix[i])
    min_value = min(matrix[i])

    matrix[i][0] = max_value
    matrix[i][-1] = min_value

print("Измененная матрица: ")
print_matrix(matrix)

print('-'*60)



# 2
# 2.1
print("""
Задание 2
1. Дана целая квадратная матрица n-го порядка. Определить, 
является ли она магическим квадратом, т. е. такой матрицей, в которой 
суммы элементов во всех строках и столбцах одинаковы.  
2. Дана прямоугольная матрица A[N, N]. Переставить первый и 
последний столбцы местами и вывести на экран. 
""")

# 2.1
print("2.1")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)


is_magic = True
for i in range(1, n):
    tmp_prev_set = set(matrix[i-1])
    tmp_set = set(matrix[i])

    if len(tmp_set) == 1 and tmp_set == tmp_prev_set:
        is_magic = True

    else:
        is_magic = False
        break
       
if is_magic:
    print("Матрица - магический квадрат")

else:
    print(print("Матрица - не магический квадрат"))
    
print('-'*60)


# 2.2
print("2.2")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

for i in range(0, n):
    tmp_value = matrix[i][0]
    matrix[i][0] = matrix[i][-1]
    matrix[i][-1] = tmp_value

print("Измененная матрица: ")
print_matrix(matrix)

print('-'*60)

# 3
print("""
Задание 3
1. Определить, является ли заданная целая квадратная матрица n-го 
порядка симметричной (относительно главной диагонали).  
2. Дана вещественная матрица размером n х m. Переставляя ее 
строки и столбцы, добиться того, чтобы наибольший элемент (или один 
из них) оказался в верхнем левом углу.   
""")

# 3.1
print("3.1")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)


is_simmetric = True
for i in range(0, n):
    for j in range(0, n):
        if matrix[i][j] == matrix[j][i]:
            is_simmetric = True

        else:
            is_simmetric = False
            break

if is_simmetric:
    print("Матрица симметрична")

else:
    print(print("Матрица не симметрична"))
    
print('-'*60)


# 3.2
print("3.2")
print('-'*60)
n = int(input("Введите кол-во строк для матрицы: "))
m = int(input("Введите кол-во столбцов для матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)


tmp_value = matrix[0][0]
m = max_in_matrix(matrix)
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == m:
            matrix[i][j] = tmp_value

matrix[0][0] = m

print("Измененная матрица: ")
print_matrix(matrix)

print('-'*60)


4
print("""
Задание 4
1. Дана прямоугольная матрица. Найти строку с наибольшей и строку 
с наименьшей суммой элементов. Вывести на печать найденные строки и 
суммы их элементов.  
2. Дана квадратная матрица A[N, N], Записать на место 
отрицательных элементов матрицы нули, а на место положительных — 
единицы.  
Вывести на печать нижнюю треугольную матрицу в общепринятом виде.    
""")

# 4.1
print("4.1")
print('-'*60)
n = int(input("Введите кол-во строк для матрицы: "))
m = int(input("Введите кол-во столбцов для матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

max_sum = float("-inf")
min_sum = float("inf")
for i in matrix:
    if sum(i) > max_sum:
        max_sum = sum(i)

    elif sum < min_sum:
        min_sum = sum(i)

for i in matrix:
    if sum(i) == max_sum:
        print(f"Строка с максимальной суммой элементов {max_sum}: {i}")
    
    elif sum(i) == min_sum:
        print(f"Строка с минимальной суммой элементов {max_sum}: {i}")
print('-'*60)


# 4.2

print("4.2")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

# Копировать значения а не создавать ссылку на объект
matrix2 = deepcopy(matrix)

print("Исходная матрица")
print_matrix(matrix)


for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if j > i:
            matrix[i][j] = 0

print("Нижняя треугольная матрица")
print_matrix(matrix)


for i in range(0, len(matrix2)):
    for j in range(0, len(matrix2[i])):
        if matrix2[i][j] <= 0:
            matrix2[i][j] = 0

        else:
            matrix2[i][j] = 1

print("Измененная матрица")
print_matrix(matrix2)

print('-'*60)


5
print("""
Задание 5
1. Упорядочить по возрастанию элементы каждой строки матрицы 
размером n х m.  
2. Дана действительная матрица размером n х m, все элементы 
которой различны. В каждой строке выбирается элемент с наименьшим 
значением. Если число четное, то заменяется нулем, нечетное - 
единицей. Вывести на экран новую матрицу. 
""")

print("5.1")
print('-'*60)
n = int(input("Введите кол-во строк для матрицы: "))
m = int(input("Введите кол-во столбцов для матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

for i in range(0, len(matrix)):
    matrix[i] = sorted(matrix[i])


print("Измененная матрица")
print_matrix(matrix)

print('-'*60)

print("5.2")
print('-'*60)
n = int(input("Введите кол-во строк для матрицы: "))
m = int(input("Введите кол-во столбцов для матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if  matrix[i][j] == min(matrix[i]):
            if min(matrix[i]) % 2 == 0:
                matrix[i][j] = 0
            
            elif min(matrix[i]) % 2 != 0:
                matrix[i][j] = 1


print("Измененная матрица")
print_matrix(matrix)

print('-'*60)


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

print("6.1")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

for i in range(0, len(matrix)):
    print(f"Наибольший элемент в строке №{i+1}: {max(matrix[i])}")

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        matrix[i][j] = matrix[j][i]

for i in range(0, len(matrix)):
    print(f"Наименьший элемент в столбце №{i+1}: {min(matrix[i])}")

print('-'*60)


print("6.2")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы (нечетное): "))
if n % 2 != 0:
    matrix = input_matrix(n, n)

    print("Исходная матрица")
    print_matrix(matrix)

    tmp_max = float("-inf")

    for i in range(0, len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                if tmp_max < matrix[i][j]: 
                    tmp_max = matrix[i][j]

    j = len(matrix[0])-1
    for i in range(0, len(matrix)):
        if tmp_max < matrix[i][j]:
            tmp_max = matrix[i][j]
        
        j-=1

    mid = int(n/2)

    matrix[mid][mid] = tmp_max

    print("Измененная матрица")
    print_matrix(matrix)

elif n % 2 == 0:
    print("Ошибка. Введено четное число")

print('-'*60)



# 7
print("""
Задание 7
1. Квадратная матрица, симметричная относительно главной 
диагонали, задана верхним треугольником в виде одномерного массива.  
Восстановить исходную матрицу и напечатать по строкам.  
2. Для заданной квадратной матрицы сформировать одномерный 
массив из ее диагональных элементов. Найти след матрицы, 
просуммировав элементы одномерного массива. Преобразовать 
исходную матрицу по правилу: четные строки разделить на полученное 
значение, нечетные оставить без изменения.  
""")

print("7.1")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = []
line_matrix = []

for i in range(0, n*n):
    line_matrix.append(int(input(f"Введите №{i} элемент матрицы: ")))

print("Исходная матрица в виде одномерного массива: ")
print(line_matrix)

num = 0
for i in range(0, n):
    tmp_mas = []
        
    for j in range(0, n):
        tmp_mas. append(line_matrix[num])
        num +=1
    matrix.append(tmp_mas)
        

print("Восстановленная исходная матрица")
print_matrix(matrix)

print('-'*60)


print("7.2")
print('-'*60)
n = int(input("Введите кол-во строк/столбцов для квадратной матрицы: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

matrix_trace = trace(matrix)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if (i+1) % 2 == 0:
            matrix[i][j] = round((matrix[i][j] / matrix_trace), 2)
    

print(f"Cлед матрицы: {matrix_trace}")

print("Измененная матрица")
for i in matrix:
    print()
    for j in i:
        print('{:>4}'.format(j), end=" ")
    print()

print('-'*60)



# 8
print("""
Задание 8
1. Задана матрица порядка n и число к. Разделить элементы k-й 
строки на диагональный элемент, расположенный в этой строке.  
2. Задана квадратная матрица. Получить транспонированную 
матрицу (перевернутую относительно главной диагонали) и вывести на 
экран.  
""")

print("8.1")
print('-'*60)

n = int(input("Введите порядок матрицы n: "))
k = int(input(f"Введите номер строки k (от 1 до {n}): "))

if 1 <= k <= n:
    matrix = input_matrix(n, n)
    
    print("Исходная матрица")
    print_matrix(matrix)
    
    diagonal_element = matrix[k-1][k-1]
    
    if diagonal_element != 0:
        for j in range(n):
            matrix[k-1][j] = matrix[k-1][j] / diagonal_element
        
        print(f"Измененная матрица (элементы строки №{k} разделены на {diagonal_element}):")
        print_matrix(matrix)
    else:
        print(f"Ошибка: диагональный элемент в строке {k} равен 0, деление невозможно.")
else:
    print("Ошибка: номер строки должен быть от 1 до {n}")

print('-'*60)


print("8.2")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))
matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

transposed_matrix = []
for i in range(n):
    tmp_row = []
    for j in range(n):
        tmp_row.append(matrix[j][i])
    transposed_matrix.append(tmp_row)

print("Транспонированная матрица")
print_matrix(transposed_matrix)

print('-'*60)








# 9
# 9.1
print("""
Задание 9
1. Для целочисленной квадратной матрицы найти число элементов, 
кратных k, и наибольший из этих элементов.  
2. В данной действительной квадратной матрице порядка n найти 
наибольший по модулю элемент. Получить квадратную матрицу порядка 
n — 1 путем отбрасывания из исходной матрицы строки и столбца, на 
пересечении которых расположен элемент с найденным значением.  
""")

print("9.1")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))
k = int(input("Введите число k: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

count = 0
max_element = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] % k == 0:
            count += 1
            if max_element is None or matrix[i][j] > max_element:
                max_element = matrix[i][j]

print(f"Число элементов, кратных {k}: {count}")
if max_element is not None:
    print(f"Наибольший из элементов, кратных {k}: {max_element}")
else:
    print(f"Элементов, кратных {k}, не найдено")

print('-'*60)

# 9.2
print("9.2")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))

# Используем float для действительных чисел
matrix = []
for i in range(0, n):
    tmp_mas = []
    print(f"Введите данные для строки № {i+1}: ")
    for j in range(0, n):
        tmp_mas.append(float(input(f"Введите число №{j+1}: ")))
    matrix.append(tmp_mas)

print("Исходная матрица")
print_matrix(matrix)

max_abs_value = 0
max_i = 0
max_j = 0

for i in range(n):
    for j in range(n):
        abs_value = abs(matrix[i][j])
        if abs_value > max_abs_value:
            max_abs_value = abs_value
            max_i = i
            max_j = j

print(f"Наибольший по модулю элемент: {matrix[max_i][max_j]} (строка {max_i+1}, столбец {max_j+1})")

if n > 1:
    new_matrix = []
    for i in range(n):
        if i == max_i:
            continue  # Пропускаем строку с максимальным элементом
        
        tmp_row = []
        for j in range(n):
            if j == max_j:
                continue  # Пропускаем столбец с максимальным элементом
            
            tmp_row.append(matrix[i][j])
        
        new_matrix.append(tmp_row)
    
    print(f"Новая матрица порядка {n-1}:")
    print_matrix(new_matrix)
else:
    print("Матрица порядка 1, нельзя создать матрицу порядка 0")

print('-'*60)




# 10
# 10.1
print("""
Задание 10
1. Найти максимальный среди всех элементов тех строк заданной 
матрицы, которые упорядочены (либо по возрастанию, либо по 
убыванию).  
2. Расположить столбцы матрицы D[M, N] в порядке возрастания 
элементов k-й строки (1 <= k <= М).  
""")

print("10.1")
print('-'*60)

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

max_element = None

for i in range(n):
    is_ascending = True
    for j in range(m - 1):
        if matrix[i][j] > matrix[i][j + 1]:
            is_ascending = False
            break
    
    is_descending = True
    for j in range(m - 1):
        if matrix[i][j] < matrix[i][j + 1]:
            is_descending = False
            break
    
    if is_ascending or is_descending:
        row_max = max(matrix[i])
        
        if max_element is None or row_max > max_element:
            max_element = row_max
        
        print(f"Строка №{i+1} упорядочена (по {'возрастанию' if is_ascending else 'убыванию'}), максимальный элемент: {row_max}")

if max_element is not None:
    print(f"Максимальный среди элементов упорядоченных строк: {max_element}")
else:
    print("В матрице нет упорядоченных строк")

print('-'*60)

# 9.2
print("10.2")
print('-'*60)

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
k = int(input(f"Введите номер строки k (от 2 до {M}): "))

if 2 <= k <= M:
    D = input_matrix(M, N)
    
    print("Исходная матрица")
    print_matrix(D)
    
    k_row = D[k-1]
    
    columns_with_indices = [(k_row[j], j) for j in range(N)]
    
    columns_with_indices.sort(key=lambda x: x[0])
    
    new_matrix = []
    for i in range(M):
        new_row = []
        for value, original_index in columns_with_indices:
            new_row.append(D[i][original_index])
        new_matrix.append(new_row)
    
    print(f"Матрица после перестановки столбцов по возрастанию элементов строки №{k}:")
    print_matrix(new_matrix)

    print(f"Элементы строки №{k} после перестановки:")
    
    for j in range(N):
        print(f"{new_matrix[k-1][j]:6}", end=' ')
    print()
else:
    print(f"Ошибка: k должно быть в диапазоне от 2 до {M}")

print('-'*60)


# 11
print("""
Задание 11
1. В данной действительной квадратной матрице порядка п найти 
сумму элементов строки, в которой расположен элемент с наименьшим 
значением. Предполагается, что такой элемент единственный.  
2. Среди столбцов заданной целочисленной матрицы, содержащих 
только такие элементы, которые по модулю не больше 10, найти столбец 
с минимальным произведением элементов и поменять местами с 
соседним.  
""")

# 11.1
print("11.1")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

min_value = matrix[0][0]
min_row = 0
min_col = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row = i
            min_col = j

print(f"Наименьший элемент: {min_value:.2f} (строка {min_row+1}, столбец {min_col+1})")

row_sum = sum(matrix[min_row])

print(f"Сумма элементов строки №{min_row+1}: {row_sum:.2f}")

print('-'*60)

# 11.2
print("11.2")
print('-'*60)

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(0, n):
    tmp_mas = []
    print(f"Введите данные для строки № {i+1}: ")
    for j in range(0, m):
        tmp_mas.append(float(input(f"Введите число №{j+1}: ")))
    
    matrix.append(tmp_mas)

print("Исходная матрица")
print_matrix(matrix)

valid_columns = []

for j in range(m):
    is_valid = True
    for i in range(n):
        if abs(matrix[i][j]) > 10:
            is_valid = False
            break
    
    if is_valid:
        product = 1
        for i in range(n):
            product *= matrix[i][j]
        
        valid_columns.append((j, product))
        print(f"Столбец №{j+1}: произведение элементов = {product}")

if valid_columns:
    min_product_col = min(valid_columns, key=lambda x: x[1])   # ключ поиска по 2 элементу каждого элемента массива
    col_index = min_product_col[0]
    
    print(f"Столбец с минимальным произведением: №{col_index+1} (произведение = {min_product_col[1]})")
    
    if col_index < m - 1:
        for i in range(n):
            temp = matrix[i][col_index]
            matrix[i][col_index] = matrix[i][col_index + 1]
            matrix[i][col_index + 1] = temp
        
        print(f"Столбец №{col_index+1} поменяли местами со столбцом №{col_index+2}")

    elif col_index > 0:
        for i in range(n):
            temp = matrix[i][col_index]
            matrix[i][col_index] = matrix[i][col_index - 1]
            matrix[i][col_index - 1] = temp
        
        print(f"Столбец №{col_index+1} поменяли местами со столбцом №{col_index}")

    else:
        print(f"Столбец №{col_index+1} - крайний, нет соседнего столбца для замены")
    
    print("Измененная матрица:")
    print_matrix(matrix)
else:
    print("Нет столбцов, все элементы которых по модулю не больше 10")

print('-'*60)



# 12
print("""
Задание 12
1. Для заданной квадратной матрицы найти такие k, что k-я строка 
матрицы совпадает с k-м столбцом.  
2. Дана действительная матрица размером n х m. Требуется 
преобразовать матрицу: поэлементно вычесть последнюю строку из всех 
строк, кроме последней.  
""")

# 12.1
print("12.1")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))

matrix = input_matrix(n, n)

print("Исходная матрица")
print_matrix(matrix)

matching_indices = []

for k in range(n):
    is_matching = True
    
    for i in range(n):
        if matrix[k][i] != matrix[i][k]:
            is_matching = False
            break
    
    if is_matching:
        matching_indices.append(k + 1)  # +1 для нумерации с 1
        print(f"Строка №{k+1} совпадает со столбцом №{k+1}")

if matching_indices:
    print(f"Найдены совпадения для k = {matching_indices}")
else:
    print("Нет таких k, при которых k-я строка совпадает с k-м столбцом")

print('-'*60)

# 12.2
print("12.2")
print('-'*60)

n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

# Создаем копию матрицы для изменений
new_matrix = deepcopy(matrix)

last_row = matrix[n-1]

for i in range(n-1):
    for j in range(m):
        new_matrix[i][j] = matrix[i][j] - last_row[j]

print(f"Матрица после вычитания последней строки из всех строк (кроме последней):")
print_matrix(new_matrix)

print("Последняя строка (осталась без изменений):")
for j in range(m):
    print(f"{last_row[j]:10.2f}", end=' ')
print()

print('-'*60)


# 13
print("""
Задание 13
1. Определить наименьший элемент каждой четной строки матрицы 
А[М, N].  
2. Найти наибольший и наименьший элементы прямоугольной 
матрицы и поменять их местами.  
""")

# 13.1
print("13.1")
print('-'*60)

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

matrix = input_matrix(M, N)

print("Исходная матрица")
print_matrix(matrix)

print("Наименьшие элементы четных строк:")
for i in range(M):
    if (i + 1) % 2 == 0:
        min_element = min(matrix[i])
        print(f"Строка №{i+1}: наименьший элемент = {min_element:.2f}")

print('-'*60)

# 13.2
print("13.2")
print('-'*60)

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

matrix = input_matrix(M, N)

print("Исходная матрица")
print_matrix(matrix)

max_value = matrix[0][0]
min_value = matrix[0][0]
max_i, max_j = 0, 0
min_i, min_j = 0, 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_i, max_j = i, j
        
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_i, min_j = i, j

print(f"Наибольший элемент: {max_value:.2f} (строка {max_i+1}, столбец {max_j+1})")
print(f"Наименьший элемент: {min_value:.2f} (строка {min_i+1}, столбец {min_j+1})")

# Меняем элементы местами
matrix[max_i][max_j], matrix[min_i][min_j] = matrix[min_i][min_j], matrix[max_i][max_j]

print("Матрица после замены наибольшего и наименьшего элементов:")
print_matrix(matrix)

print('-'*60)


# 14
print("""
Задание 14
1. Задана квадратная матрица. Переставить строку с максимальным 
элементом на главной диагонали со строкой с заданным номером m.  
2. Составить программу, которая заполняет квадратную матрицу 
порядка п натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по 
спирали». 
""")

# 14.1
print("14.1")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))

matrix = input_matrix(n, n)

print("\nИсходная матрица")
print_matrix(matrix)

max_diag_value = matrix[0][0]
max_diag_row = 0

for i in range(n):
    if matrix[i][i] > max_diag_value:
        max_diag_value = matrix[i][i]
        max_diag_row = i

print(f"Максимальный элемент на главной диагонали: {max_diag_value:.2f} (строка {max_diag_row+1})")

m = int(input(f"Введите номер строки m для обмена (от 1 до {n}): "))

if 1 <= m <= n:
    m_index = m - 1
    
    if m_index != max_diag_row:
        matrix[max_diag_row], matrix[m_index] = matrix[m_index], matrix[max_diag_row]
        
        print(f"Матрица после перестановки строки {max_diag_row+1} и строки {m}:")
        print_matrix(matrix)
    else:
        print(f"Строка с максимальным элементом на диагонали и строка {m} совпадают, перестановка не требуется.")
else:
    print(f"Ошибка: номер строки должен быть от 1 до {n}")

print('-'*60)

# 14.2
print("14.2")
print('-'*60)

n = int(input("Введите порядок квадратной матрицы n: "))

# Создаем пустую матрицу n x n, заполненную нулями
spiral_matrix = [[0] * n for _ in range(n)]

# Начальные значения
num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while num <= n * n:
    # Заполняем верхнюю строку слева направо
    for i in range(left, right + 1):
        spiral_matrix[top][i] = num
        num += 1
    top += 1
    
    # Заполняем правый столбец сверху вниз
    for i in range(top, bottom + 1):
        spiral_matrix[i][right] = num
        num += 1
    right -= 1
    
    # Заполняем нижнюю строку справа налево
    for i in range(right, left - 1, -1):
        spiral_matrix[bottom][i] = num
        num += 1
    bottom -= 1
    
    # Заполняем левый столбец снизу вверх
    for i in range(bottom, top - 1, -1):
        spiral_matrix[i][left] = num
        num += 1
    left += 1

print(f"Матрица порядка {n}, заполненная по спирали:")
print_matrix(spiral_matrix)

print('-'*60)


# 15
print("""
Задание 15
1. Определить номера строк матрицы R[M, N], хотя бы один элемент 
которых равен с, и элементы этих строк умножить на d.  
2. Среди тех строк целочисленной матрицы, которые содержат только 
нечетные элементы, найти строку с максимальной суммой модулей 
элементов. 
""")

# 15.1
print("15.1")
print('-'*60)

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

matrix = input_matrix(M, N)

print("Исходная матрица")
print_matrix(matrix)

c = float(input("Введите значение c: "))
d = float(input("Введите значение d: "))

rows_with_c = []

for i in range(M):
    found = False
    for j in range(N):
        if matrix[i][j] == c:
            found = True
            break
    
    if found:
        rows_with_c.append(i)
        for j in range(N):
            matrix[i][j] *= d

if rows_with_c:
    print(f"Строки, содержащие значение {c}: {[row+1 for row in rows_with_c]}")
    print(f"Элементы этих строк умножены на {d}")
else:
    print(f"Нет строк, содержащих значение {c}")

print("Измененная матрица:")
print_matrix(matrix)

print('-'*60)

# 15.2
print("15.2")
print('-'*60)

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = input_matrix(n, m)

print("Исходная матрица")
print_matrix(matrix)

valid_rows = []

for i in range(n):
    all_odd = True
    for j in range(m):
        if matrix[i][j] % 2 == 0:  
            all_odd = False
            break
    
    if all_odd:
        sum_abs = sum(abs(x) for x in matrix[i])
        valid_rows.append((i, sum_abs))
        print(f"Строка №{i+1}: все элементы нечетные, сумма модулей = {sum_abs}")

if valid_rows:
    max_sum_row = max(valid_rows, key=lambda x: x[1])

    row_index, max_sum = max_sum_row
    
    print(f"Строка с максимальной суммой модулей элементов: №{row_index+1}")
    print(f"Элементы строки: {matrix[row_index]}")
    print(f"Сумма модулей элементов: {max_sum}")
else:
    print("Нет строк, содержащих только нечетные элементы")

print('-'*60)

# Практическая работа №10
# Чайкин А. У-255

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(f"{j}", end=' ')
        print()

def read_matrix_from_file(source: str):
    matrix = []
    with open(source, "r") as f:
        for i in f:
            i = i.rstrip("\n")
            if i != '':
                tmp_list = i.split()
                for j in range(0, len(tmp_list)):
                    if '.' in tmp_list[j]:
                        tmp_list[j] = float(tmp_list[j])
                    else:
                        tmp_list[j] = int(tmp_list[j])
                matrix.append(tmp_list)
    return matrix


def write_matrix_in_file(matrix, source: str):    
    with open(source, "w") as f:
        for i in matrix:
            tmp_s = ' '.join(map(str, i))    
            f.write(tmp_s+"\n")
        
        print(f"Данные в файл {source} записаны успешно!")


print("""
1. Для целочисленной квадратной матрицы найти число элементов, 
кратных k, и наибольший из этих элементов.  
2. В данной действительной квадратной матрице порядка n найти 
наибольший по модулю элемент. Получить квадратную матрицу порядка 
n — 1 путем отбрасывания из исходной матрицы строки и столбца, на 
пересечении которых расположен элемент с найденным значением.  
""")


print("Задание 1")
print('-'*60)
matrix = read_matrix_from_file("Chaykin_U-255_vvod_1.txt")
print("Исходная матрица")
print_matrix(matrix)


k = int(input("Введите число k: "))

count = 0
max_element = None

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] % k == 0:
            count += 1
            if max_element is None or matrix[i][j] > max_element:
                max_element = matrix[i][j]

print(f"Число элементов, кратных {k}: {count}")
if max_element is not None:
    print(f"Наибольший из элементов, кратных {k}: {max_element}")
else:
    print(f"Элементов, кратных {k}, не найдено")


write_matrix_in_file(matrix, "Chaykin_U-255_vivod_1.txt")


print('-'*60)

print("Задание 2")
print('-'*60)
matrix = read_matrix_from_file("Chaykin_U-255_vvod_2.txt")
print("Исходная матрица")
print_matrix(matrix)


max_abs_value = 0
max_i = 0
max_j = 0

n = len(matrix)

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

write_matrix_in_file(new_matrix, "Chaykin_U-255_vivod_2.txt")


print('-'*60)
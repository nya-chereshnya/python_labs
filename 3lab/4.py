import random

# функция для создания случайной матрицы


def create_matrix(m, n):
    return [[random.randint(1, 99) for j in range(n)] for i in range(m)]

# функция для вывода матрицы в наглядном виде


def print_matrix(matrix):
    for row in matrix:
        for num in row:
            if num >= 10:
                print(num, end="   ")
            elif num < 10:
                print(num, end="    ")
        print("")
        # print(num > 10 for num in row ? return num : return " " + num)

# функция для нахождения минимальных элементов каждого ряда матрицы


def find_min_in_rows(matrix):
    min_list = []
    for row in matrix:
        min_list.append(min(row))
    return min_list

# функция для нахождения среднего значения всех элементов матрицы


def find_average(matrix):
    count = 0
    total_sum = 0
    max_value = max([max(row) for row in matrix])
    min_value = min([min(row) for row in matrix])
    for row in matrix:
        for num in row:
            if (num == max_value) or (num == min_value):
                continue
            else:
                total_sum += num
                count += 1
    return total_sum / count


# создаем случайную матрицу 5x4
matrix = create_matrix(5, 4)

# выводим матрицу
print("Matrix:")
print_matrix(matrix)

# находим минимальные элементы каждого ряда матрицы и выводим их
min_list = find_min_in_rows(matrix)
print("Matrix minimums: ", min_list)

# находим среднее значение всех элементов матрицы и выводим его
avg = find_average(matrix)
print("Average value (excluding max and min): ", avg)

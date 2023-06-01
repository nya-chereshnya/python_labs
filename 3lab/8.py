import random

def create_matrix_arr():
    matrix1 = [[random.randint(-100, 100) for i in range(2)] for i in range(2)]
    matrix2 = [[random.randint(-100, 100) for i in range(2)] for i in range(3)]
    matrix3 = [[random.randint(-100, 100) for i in range(3)] for i in range(2)]
    return [matrix1, matrix2, matrix3]

def get_column_max(matrix):
    max_arr = []
    for column in range(len(matrix[0])):
        max = -100
        for elem in range(len(matrix)):
            if matrix[elem][column] > max: max = matrix[elem][column]
        max_arr.append(max)
    return (max_arr)

def print_matrix(matrix):
    for row in matrix:
        print(*row)

matrix_arr = create_matrix_arr()
print_matrix(matrix_arr[0])
print("\ncolumn maximums: ", *get_column_max(matrix_arr[0]), "\n")
print_matrix(matrix_arr[1])
print("\ncolumn maximums: ", *get_column_max(matrix_arr[1]), "\n")
print_matrix(matrix_arr[2])
print("\ncolumn maximums: ", *get_column_max(matrix_arr[2]), "\n")
get_column_max(matrix_arr[0])
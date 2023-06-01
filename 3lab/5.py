import random


def create_matrix(m, n):
    return [[random.randint(-99, 99) for j in range(n)] for i in range(m)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print("")


def reverse_matrix(matrix):
    new_matrix = [[0 for i in range(len(matrix))]
                  for j in range(len(matrix[0]))]
    for column in range(len(matrix[0])):
        for elem in range(len(matrix)):
            new_matrix[column][elem] = matrix[elem][column]
    return new_matrix


def get_characteristic(row):
    characteristic = [0]
    for elem in range(1, len(row), 2):
        if row[elem] < 0:
            characteristic.append(abs(row[elem]))
    return sum(characteristic)
    # return row[0]


# def sort_matrix(matrix):
#     for iter in range(len(matrix) - 1):
#         for row in range(len(matrix) - 1 - iter):
#             if get_characteristic(matrix[row]) > get_characteristic(matrix[row + 1]):
#                 matrix[row], matrix[row + 1] = matrix[row + 1], matrix[row]


def sort_matrix(matrix):
    new_matrix = reverse_matrix(matrix)
    return reverse_matrix(sorted(new_matrix, key=get_characteristic))


def print_characteristics(matrix):
    # print("")
    for row in matrix:
        print(get_characteristic(row), end=" ")


matrix = create_matrix(6, 7)
print_matrix(matrix)
print_characteristics(reverse_matrix(matrix))
print("\n")
newmatrix = sort_matrix(matrix)
print_matrix(newmatrix)
print_characteristics(reverse_matrix(newmatrix))
print("\n")

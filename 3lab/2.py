def get_even(num):
    if num % 2 == 1:
        return num - 1
    return num


def permutation(arr):
    new_arr = arr
    for i in range(0, get_even(len(arr)) - 1, 2):
        new_arr[i], new_arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(permutation([1, 2, 3, 4, 5, 6, 7]))

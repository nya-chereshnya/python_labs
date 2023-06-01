import random


class Array:
    def __init__(self, size):
        self.size = size
        self.values = [random.randint(-50, 50) for _ in range(self.size)]

    def count_multiples_of_three(self):
        return sum(1 for value in self.values if value % 3 == 0)

    def sum_positive_numbers(self):
        return sum(value for value in self.values if value > 0)

    def max_positive_number_index(self):
        positive_numbers = [value for value in self.values if value > 0]
        if not positive_numbers:
            return None
        return self.values.index(max(positive_numbers))

    def has_zeros(self):
        return any(value == 0 for value in self.values)

    def print_even_indices(self):
        for i in range(0, self.size, 2):
            print(f'a[{i}] = {self.values[i]}')


# Пример использования
my_array = Array(15)
print(my_array.values)

print("Количество чисел, кратных трём: ", my_array.count_multiples_of_three())
print("Сумма положительных чисел: ", my_array.sum_positive_numbers())
print("Номер максимального положительного числа: ",
      my_array.max_positive_number_index())
print("Наличие нулевых значений: ", my_array.has_zeros())
print("Ячейки массива с чётными индексами:")
my_array.print_even_indices()

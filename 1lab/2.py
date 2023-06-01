def has_duplicate_digits(n):
    # Проверяем, есть ли в числе n две одинаковые цифры
    digits = []
    for digit in str(n):
        if digit in digits:
            return True
        digits.append(digit)
    return False

def main():
    # Выводим все числа, удовлетворяющие условию
    for n in range(1000, 9999):
        if not has_duplicate_digits(n):
            print(n)


main()
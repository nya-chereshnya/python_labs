def sum_two_digits(n, sum = 0):
    if n < 10 or n > 99:
        return sum
    else:
        return n + sum_two_digits(n-1, sum)
        sum += n
        

print(sum_two_digits(99))
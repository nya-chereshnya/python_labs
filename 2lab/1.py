import timeit

def NumberOfOdds(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 10
    return count

n = 123456789
repetitions = 1000000

start_time = timeit.default_timer()
for i in range(repetitions):
    result = NumberOfOdds(n)
end_time = timeit.default_timer()

print("Результат: ", result)
print("Время работы функции для %d повторов: %f секунд" % (repetitions, end_time - start_time))
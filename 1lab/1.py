import math
t, d, b, s = 0, 0, 0, 0
# Функция для определения области определения функции


def find_domain(func):
    domain = None
    try:
        eval(func)
        # Вызываем функцию со значением, выходящим за ее область определения
    except ArithmeticError:
        domain = "Oшибка ООФ"
    return domain

# Функция для оценки сложности функции в условных единицах


def estimate_complexity(func):
    complexity = 0
    complexity += func.count("=")
    complexity += func.count("+") * 3
    complexity += func.count("-") * 3
    complexity += func.count("*") * 5
    complexity += func.count("/") * 7
    complexity += func.count("math.") * 13
    complexity += func.count("<<") * 2
    complexity += func.count(">>") * 2
    return complexity


def var_inputs():
    global t, d, b, s
    t = float(input("t: "))
    d = float(input("d: "))
    b = float(input("b: "))
    s = float(input("s: "))


func1 = "(2 / ((1 / math.tan(math.exp(math.pow(s, t)))) - math.tan(math.exp(math.pow(s, t))))) * ((math.tan(math.pow(d, 3)) + math.tan(math.log10(b))) / ((1 / math.tan(math.pow(d, 3))) + ((1 / math.tan(math.log10(b))))))"
func2 = "(math.tan(2 * math.exp(math.pow(s, t)))) * (math.tan(math.pow(d, 3)) * math.tan(math.log10(b)))"
var_inputs()
domain1 = find_domain(func1)
complexity1 = estimate_complexity(func1)
domain2 = find_domain(func2)
complexity2 = estimate_complexity(func2)
print("Область определения исходного выражения:", domain1)
print("Область определения результирющего выражения:", domain2)
print("Сложность исходного выражения:", complexity1, "условных единиц")
print("Сложность результирющего выражения:", complexity2, "условных единиц")
print("Выйгрыш: ", complexity1 - complexity2)
print(eval(func1))
print(eval(func2))
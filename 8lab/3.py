from abc import ABC, abstractmethod
from math import sqrt


class ICalculatable(ABC):
    @abstractmethod
    def calculate_recursived(self, n):
        pass

    @abstractmethod
    def get_numbers_order(self, n):
        pass


class FibonacciCalculator(ICalculatable):
    def __init__(self) -> None:
        super().__init__()
        self.fib = lambda x: x if x <= 1 else self.fib(x - 1) + self.fib(x - 2)

    def calculate_recursived(self, n):
        return self.fib(n)

    def get_numbers_order(self, n):
        return [self.fib(i) for i in range(1, n + 1)]
    
    def calculate_optimised(self, n):
        order = [0, 1]
        if n == 1:
            return order[1]
        for i in range(2, n + 1):
            order.append(int(str(sum(order))[-1]))
            order.pop(0)
            # print(order)
        return order[-1]


fibonacci_calculator = FibonacciCalculator()
print(fibonacci_calculator.calculate_recursived(3))
print(fibonacci_calculator.get_numbers_order(3))
n = int(input())
print(fibonacci_calculator.calculate_optimised(n))
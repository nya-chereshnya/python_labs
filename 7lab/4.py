from abc import ABC, abstractmethod


class IComparable(ABC):

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass


class IEnumerable(ABC):

    @abstractmethod
    def __iter__(self):
        pass


class iPad(IComparable, IEnumerable):
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __iter__(self):
        yield self.model
        yield self.year
        yield self.price


ipad1 = iPad("iPad Air", 2020, 599)
ipad2 = iPad("iPad Pro", 2021, 799)
ipad3 = iPad("iPad mini", 2022, 499)

print(ipad1 > ipad2)
print(ipad3 == ipad1)
print(ipad3 < ipad2)

for item in ipad1:
    print(item)

for item in ipad2:
    print(item)

for item in ipad3:
    print(item)

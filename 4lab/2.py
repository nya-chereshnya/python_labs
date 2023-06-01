from enum import Enum
from math import floor


class Student:
    class spec(Enum):
        spec1 = "РПИС"
        spec2 = "ПО"
        spec3 = "УИТС"

    def __init__(self, studentsArr):
        self.__studentsArr = studentsArr
        self.__groups = self.__getGroups()

    # def jjj(self):
    #     return self.__groups

    def __getGroups(self):
        groups = [["{} ".format(self.__studentsArr[i * 3 + j]) + eval("self.spec.spec{}.value".format(j + 1), {"self": self}) for j in range(3)] for i in range(
            0, floor(len(self.__studentsArr) / 3) - 0)]
        groups.extend([["{} ".format(self.__studentsArr[-(1 + i)]) + eval(
            "self.spec.spec{}.value".format(i + 1), {"self": self}) for i in range(len(self.__studentsArr) % 3)]])
        groups = [group for group in groups if group]
        return groups

    def printGroups(self):
        for group in range(0, len(self.__groups)):
            print("Группа {}:".format(group + 1), end=" ")
            for student in range(len(self.__groups[group]) - 1):
                print(self.__groups[group][student], end=", ")
            print(self.__groups[group][student + 1], end=";\n")


lol = Student(["Иванов", "Петров", "Сидоров",
              "Смирнов", "Кузнецов", "111", "222s", "12132"])
# print(lol.jjj())
lol.printGroups()



class Student:
    def __init__(self, name, mathGrade, physicsGrade, informaticsGrade):
        self.name = name
        self.mathGrade = mathGrade
        self.physicsGrade = physicsGrade
        self.informaticsGrade = informaticsGrade


with open("in.txt", "r") as fileIn:
    len = int(fileIn.readline())
    students = []
    for string in fileIn:
        line = string.split()
        students.append(Student("{} {}".format(
            line[0], line[1]), int(line[2]), int(line[3]), int(line[4])))
fileIn.close()


for student in students:
    avg = (student.mathGrade + student.physicsGrade +
           student.informaticsGrade) / 3
    print("%.3f" % avg)

with open("out.txt", "w") as fileOut:
    for student in students:
        if student.mathGrade > 3 and student.physicsGrade > 3 and student.informaticsGrade > 3:
            fileOut.write(student.name + "\n")

fileOut.close()

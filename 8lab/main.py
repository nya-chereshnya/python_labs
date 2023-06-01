from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from design import Ui_MainWindow
from classes import Student, Students, Teacher, StudentsContainer
import sys


class StudentThread(QThread):
    move_to_progress_list = pyqtSignal(Student)
    move_from_progress_to_queue = pyqtSignal(Student)
    move_from_queue_to_teacher_1 = pyqtSignal(Student)
    move_from_queue_to_teacher_2 = pyqtSignal(Student)
    move_from_teacher_1_to_retaking = pyqtSignal(Student)
    move_from_teacher_2_to_retaking = pyqtSignal(Student)
    move_from_teacher_1_to_passed = pyqtSignal(Student)
    move_from_teacher_2_to_passed = pyqtSignal(Student)
    move_from_retake_to_queue = pyqtSignal(Student)

    def __init__(self, student, mutex_1, mutex_2, teacher_1, teacher_2):
        super().__init__()
        self.student = student
        self.mutex_1 = mutex_1
        self.mutex_2 = mutex_2
        self.teacher_1 = teacher_1
        self.teacher_2 = teacher_2

    def run(self):
        self.move_to_progress_list.emit(self.student)
        self.student.take_test()
        self.move_from_progress_to_queue.emit(self.student)
        self._join_test_queue(self.student)

    def _join_test_queue(self, student):
        while True:
            if self.mutex_1.tryLock():
                self.move_from_queue_to_teacher_1.emit(student)
                self._submit_for_review(student, self.teacher_1)
                self.mutex_1.unlock()
                self._check_student_status(student, self.teacher_1)
                break
            elif self.mutex_2.tryLock():
                self.move_from_queue_to_teacher_2.emit(student)
                self._submit_for_review(student, self.teacher_2)
                self.mutex_2.unlock()
                self._check_student_status(student, self.teacher_2)
                break

    def _submit_for_review(self, student, teacher):
        teacher.start_checking_test(student)

    def _check_student_status(self, student, teacher):
        pass_status = student.get_result()
        if not pass_status:
            if teacher == self.teacher_1:
                self.move_from_teacher_1_to_retaking.emit(student)
                self._resit_exam(student)
            else:
                self.move_from_teacher_2_to_retaking.emit(student)
                self._resit_exam(student)
            return
        if teacher == self.teacher_1:
            self.move_from_teacher_1_to_passed.emit(student)
        else:
            self.move_from_teacher_2_to_passed.emit(student)

    def _resit_exam(self, student):
        student.take_test()
        self.move_from_retake_to_queue.emit(student)
        self._join_test_queue(student)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mutex_1 = QMutex()
        self.mutex_2 = QMutex()

        self.teacher_1 = Teacher("teacher_1")
        self.teacher_2 = Teacher("teacher_2")

        self.container = StudentsContainer()
        self.passed_table = self.ui.tableWidget_passed
        self.retake_table = self.ui.tableWidget_retaking
        self.queue_table = self.ui.tableWidget_queue
        self.in_progress_table = self.ui.tableWidget_in_progress
        self.teacher_1_table = self.ui.tableWidget_teacher_1
        self.teacher_2_table = self.ui.tableWidget_teacher_2

        students = Students().create_group(20)
        self.threads = []

        for student in students:
            t = StudentThread(student, self.mutex_1,
                              self.mutex_2, self.teacher_1, self.teacher_2)
            t.move_to_progress_list.connect(self.move_to_progress_list)
            t.move_from_progress_to_queue.connect(
                self.move_from_progress_to_queue)
            t.move_from_queue_to_teacher_1.connect(
                self.move_from_queue_to_teacher_1)
            t.move_from_queue_to_teacher_2.connect(
                self.move_from_queue_to_teacher_2)
            t.move_from_teacher_1_to_retaking.connect(
                self.move_from_teacher_1_to_retaking)
            t.move_from_teacher_2_to_retaking.connect(
                self.move_from_teacher_2_to_retaking)
            t.move_from_teacher_1_to_passed.connect(
                self.move_from_teacher_1_to_passed)
            t.move_from_teacher_2_to_passed.connect(
                self.move_from_teacher_2_to_passed)
            t.move_from_retake_to_queue.connect(
                self.move_from_retake_to_queue)
            self.threads.append(t)

    def move_to_progress_list(self, student):
        self.container.add_to_progress_list(student)
        self.update_table(self.in_progress_table,
                          self.container.get_progress_list())

    def move_from_progress_to_queue(self, student):
        self.container.add_to_queue_list(student)
        self.container.remove_from_progress_list(student)
        self.update_table(self.queue_table, self.container.get_queue_list())
        self.update_table(self.in_progress_table,
                          self.container.get_progress_list())

    def move_from_queue_to_teacher_1(self, student):
        self.container.remove_from_queue_list(student)
        self.container.add_to_waiting_list_1(student)
        self.update_table(self.queue_table, self.container.get_queue_list())
        self.update_table(self.teacher_1_table,
                          self.container.get_waiting_list_1())

    def move_from_queue_to_teacher_2(self, student):
        self.container.remove_from_queue_list(student)
        self.container.add_to_waiting_list_2(student)
        self.update_table(self.queue_table, self.container.get_queue_list())
        self.update_table(self.teacher_2_table,
                          self.container.get_waiting_list_2())

    def move_from_teacher_1_to_retaking(self, student):
        self.container.remove_from_waiting_list_1(student)
        self.container.add_to_retake_list(student)
        self.update_table(self.teacher_1_table,
                          self.container.get_waiting_list_1())
        self.update_table(self.retake_table, self.container.get_retake_list())

    def move_from_teacher_2_to_retaking(self, student):
        self.container.remove_from_waiting_list_2(student)
        self.container.add_to_retake_list(student)
        self.update_table(self.teacher_2_table,
                          self.container.get_waiting_list_2())
        self.update_table(self.retake_table, self.container.get_retake_list())

    def move_from_teacher_1_to_passed(self, student):
        self.container.remove_from_waiting_list_1(student)
        self.container.add_to_passed_list(student)
        self.update_table(self.teacher_1_table,
                          self.container.get_waiting_list_1())
        self.update_table(self.passed_table, self.container.get_passed_list())

    def move_from_teacher_2_to_passed(self, student):
        self.container.remove_from_waiting_list_2(student)
        self.container.add_to_passed_list(student)
        self.update_table(self.teacher_2_table,
                          self.container.get_waiting_list_2())
        self.update_table(self.passed_table, self.container.get_passed_list())

    def move_from_retake_to_queue(self, student):
        self.container.remove_from_retake_list(student)
        self.container.add_to_queue_list(student)
        self.update_table(self.retake_table, self.container.get_retake_list())
        self.update_table(self.queue_table, self.container.get_queue_list())

    def update_table(self, table, data):
        data_len = len(data)
        table.setRowCount(data_len)
        for row in range(data_len):
            student_id = data[row]
            table.setItem(row, 0, QTableWidgetItem(str(student_id)))

    def start_threads(self):
        self.ui.start_pushButton.setEnabled(False)
        for t in self.threads:
            t.start()

    def start(self):
        self.ui.start_pushButton.clicked.connect(self.start_threads)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start()
    sys.exit(app.exec_())

import time
import random


class Student:
    def __init__(self, id) -> None:
        self.MIN_TEST_EXECUTION_TIME = 1
        self.MAX_TEST_EXECUTION_TIME = 3
        self._student_id = id
        self.test_execution_time = random.randint(
            self.MIN_TEST_EXECUTION_TIME, self.MAX_TEST_EXECUTION_TIME)
        self._test_result = False

    def get_id(self):
        return self._student_id

    def set_result(self, result: bool):
        if result == False:
            print(f"{self.get_id()} went to RETAKE")
            self.test_execution_time = random.randint(
                self.MIN_TEST_EXECUTION_TIME, self.MAX_TEST_EXECUTION_TIME)
            return
        self._test_result = result

    def take_test(self):
        print(f"student {self.get_id()} started doing the test")
        time.sleep(self.test_execution_time)
        print(f"student {self.get_id()} finished the test")
        return

    def get_result(self):
        return self._test_result


class Students:
    def __init__(self):
        self._students = []

    def _append_student(self, student_id):
        self._students.append(Student(student_id))

    def create_group(self, students_amount):
        for _ in range(students_amount):
            self._append_student(f'#{_}')
        return self._students

    def get_group(self):
        return self._students


class Teacher:
    def __init__(self, name) -> None:
        self._name = name
        self._MIN_TEST_CHECKING_TIME = 1
        self._MAX_TEST_CHECKING_TIME = 3
        self.test_check_time = random.randint(
            self._MIN_TEST_CHECKING_TIME, self._MAX_TEST_CHECKING_TIME)

    def start_checking_test(self, student: Student):
        print(
            f"{self._name} CHECKING {student.get_id()}")
        time.sleep(self.test_check_time)
        result = random.choice([True, False])
        print(f"{self._name} CHECKED {student.get_id()}")
        student.set_result(result)

    def get_name(self):
        return self._name


class StudentsContainer:
    def __init__(self) -> None:
        self._students_awaiting_result_1 = []
        self._students_awaiting_result_2 = []
        self._students_in_progress = []
        self._students_in_queue = []
        self._students_retaking = []
        self._students_passed = []

    def add_to_waiting_list_1(self, student):
        self._students_awaiting_result_1.append(student.get_id())

    def add_to_waiting_list_2(self, student):
        self._students_awaiting_result_2.append(student.get_id())

    def remove_from_waiting_list_1(self, student):
        self._students_awaiting_result_1.remove(student.get_id())

    def remove_from_waiting_list_2(self, student):
        self._students_awaiting_result_2.remove(student.get_id())

    def add_to_progress_list(self, student):
        self._students_in_progress.append(student.get_id())

    def remove_from_progress_list(self, student):
        self._students_in_progress.remove(student.get_id())

    def add_to_queue_list(self, student):
        self._students_in_queue.append(student.get_id())

    def remove_from_queue_list(self, student):
        self._students_in_queue.remove(student.get_id())

    def add_to_retake_list(self, student):
        self._students_retaking.append(student.get_id())

    def remove_from_retake_list(self, student):
        self._students_retaking.remove(student.get_id())

    def get_waiting_list_1(self):
        return self._students_awaiting_result_1

    def get_waiting_list_2(self):
        return self._students_awaiting_result_2

    def get_progress_list(self):
        return self._students_in_progress

    def get_queue_list(self):
        return self._students_in_queue

    def get_retake_list(self):
        return self._students_retaking

    def add_to_passed_list(self, student):
        self._students_passed.append(student.get_id())

    def get_passed_list(self):
        return self._students_passed

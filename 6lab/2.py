import datetime
import re


class Note:
    def __init__(self, full_name: str, phone_number: str, email: str, birth_day: str) -> None:
        self.__email = self.__validate_email(email)
        self.__birth_day = self.__validate_birth_day(birth_day)
        self.__full_name = self.__validate_full_name(full_name)
        self.__phone_number = self.__validate_phone_number(phone_number)

    def __validate_email(self, email: str) -> str:
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_pattern, email):
            return email
        return "none"

    def __validate_birth_day(self, birth_day: str) -> str:
        try:
            datetime.datetime.strptime(birth_day, '%d.%m.%Y')
            return birth_day
        except ValueError:
            return "none"

    def __validate_full_name(self, full_name: str) -> str:
        name_pattern = r"^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$"
        if re.match(name_pattern, full_name):
            return full_name
        return "none"

    def __validate_phone_number(self, phone_number: str) -> str:
        phone_number = re.sub(r"\s+|-", "", phone_number)
        phone_number = phone_number.replace("+7", "8")
        if not phone_number.startswith("8"):
            phone_number = "8" + phone_number
        if len(phone_number) < 11:
            phone_number = "8" + phone_number[1:] + "0" * \
                (11 - len(phone_number))
        elif len(phone_number) > 11:
            phone_number = phone_number[11:]
        return phone_number

    @property
    def full_name(self): return self.__full_name

    @property
    def phone_number(self): return self.__phone_number

    @property
    def email(self): return self.__email

    @property
    def birth_day(self): return self.__birth_day

    def print_all_data(self):
        print("full name:", self.__full_name)
        print("phone number:", self.__phone_number)
        print("email:", self.__email)
        print("birth day:", self.__birth_day)


class Notebook:
    def __init__(self, notes: list[Note]) -> None:
        self.__notes = notes

    def __get_error(self): return "no such note"

    def search_by_phone(self, phone_number):
        found = False
        for note in self.__notes:
            if note.phone_number == phone_number:
                note.print_all_data()
                found = True
        if found == False:
            print(self.__get_error())
        return 0

    def search_by_birth_date(self, birth_day=datetime.date.today()):
        found = False
        for note in self.__notes:
            if note.birth_day == birth_day:
                note.print_all_data()
                found = True
        if found == False:
            print(self.__get_error())

    def search_by_birth_month(self, month=str(datetime.date.today().month)):
        found = False
        for note in self.__notes:
            if str(note.birth_day)[3:5] == ('0' + month):
                note.print_all_data()
                found = True
        if found == False:
            print(self.__get_error())

    def search_by_phone(self, phone_number):
        found = False
        if phone_number[0] == '8':
            for note in self.__notes:
                if note.phone_number[0:len(phone_number)] == phone_number:
                    note.print_all_data()
                    found = True
        else:
            for note in self.__notes:
                if note.phone_number[1:len(phone_number) + 1] == phone_number:
                    note.print_all_data()
                    found = True
        if found == False:
            print(self.__get_error())


note1 = Note("Иванов Александр Сергеевич", "89991234567",
             "ivanov.alexandr@mail.com", "23.06.1987")
note2 = Note("Кузнецова Екатерина Дмитриевна", "89182345678",
             "kuznetsova.ekaterina@gmail.com", "11.11.1995")
note3 = Note("Петров Даниил Андреевич", "89997894567",
             "petrov.daniil@yahoo.com", "05.04.1983")
note4 = Note("Лебедева Анастасия Максимовна", "89873451234",
             "lebedeva.nastya@outlook.com", "18.09.1990")
note5 = Note("Смирнов Владимир Игоревич", "89026547890",
             "smirnov.vladimir@mail.ru", "29.12.1978")


notes = Notebook([note1, note2, note3, note4, note5])
notes.search_by_phone('999')

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

class Author(Person):
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_genre(self):
        return self.genre

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

class Reader(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books_read = []

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_book(self, book):
        self.books_read.append(book)

    def get_books_read(self):
        return self.books_read

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def get_books(self):
        return self.books

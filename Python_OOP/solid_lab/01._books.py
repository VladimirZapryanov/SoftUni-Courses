<<<<<<< HEAD
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
=======
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        return [b for b in self.books if b.title == title][0]
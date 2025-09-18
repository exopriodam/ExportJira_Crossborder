from Biblioteque_project.models.Book import Book


class Member:
    def __init__(self, name:str):
        self._name = name
        self._list_of_books = []
    def __str__(self):
        return f"{self._name}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    # @property
    # def list_of_books(self):
    #     for __book in self._list_of_books:
    #         yield __book.title
    @property
    def list_of_books(self):
        return [__book.title for __book in self._list_of_books]
    def borrow_book(self, book:Book):
        self._list_of_books.append(book)
        book.state="Borrowed"
    def return_book(self, book:Book):
        self._list_of_books.remove(book)
        book.state="Available"
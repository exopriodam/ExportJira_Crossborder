from Biblioteque_project.models.Book import Book
from Biblioteque_project.models.Member import Member

class Library:
    def __init__(self,name:str):
        self.name=name
        self.books=[]
        self.members=[]
    @property
    def all_books(self):
        return [[item.title,item.state] for item in self.books]
    def add_book(self,book:Book):
        self.books.append(book)
    def add_member(self,member:Member):
        self.members.append(member)
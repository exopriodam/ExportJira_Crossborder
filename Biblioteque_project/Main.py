from models.Book import Book
from models.Member import Member
from models.Library import Library

def run():
    livre1 = Book("Le livre de la jungle", "Nisrine *","Available")
    livre2 =  Book("1984", "Goerge Orwel","Available")
    user1 = Member("AdamLeFou")
    biblio = Library("Koekelberk")
    biblio.add_member(user1)
    biblio.add_book(livre1)
    biblio.add_book(livre2)
    user1.borrow_book(livre1)
    print(biblio.all_books)
    user1.return_book(livre1)
    print(biblio.all_books)
    # for title in user1.list_of_books:
    #     print(title)

if __name__ == "__main__":
    run()
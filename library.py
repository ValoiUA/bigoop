from person import LibraryEmployer, Employyer

class Book:
    def __init__(self, title: str, author: str, genre: str, price: int, isbn: str) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.isbn = isbn

class Library:
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.users = []
        self.employyers = []
        self.books = []
        self.borrowed_books = []
        self.ranks = ["Library Trainee", "Library Manager", "Library Director"]

    #Employyers
    def add_librarystaff(self, person) -> None:
        if person.__class__ == LibraryEmployer:
            self.employyers.append(person)
        elif person.__class__ != Employyer:
            print(f"{person.name} cant word he must be Employyer")
        else:
            try:    
                self.employyers.append(person)
                person.__class__ = LibraryEmployer
                person.status = "Free"
                person.rank = self.ranks[0]
            except ValueError:
                print(f"{person.name} is already employyer")
    
    def remove_librarystaff(self, person: LibraryEmployer) -> None:
        self.employyers.remove(person)
        person.status = "Free"
        person.rank = "Employyer"
        person.__class__ = Employyer

    def promote_libraryst(self, libraryyst: LibraryEmployer) -> None:
        if libraryyst in self.employyers:
            libraryyst.rank = self.ranks[libraryyst.rank + 1]
            print(f"{libraryyst.name} have been promoted to {libraryyst.rank}")
        else:
            print(f"Person {libraryyst.name} is not in the library")
        
    #Books
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def borrow_book(self, book: Book, people) -> None:
        if people not in self.users:
            print(f"{people.name} is not in the library")
            return None
        
        self.borrow_book.append({people: book})
        self.books.remove(book)
    
    def return_book(self, people, book: Book):
        if {people: book} not in self.borrow_book:
            print(f"{people.name} has not borrowed {book.title}")
            return None
        self.borrow_book.remove({people: book})
        self.books.append(book)


    #Users
    def add_user(self, person) -> None:
        if person not in self.users:
            self.users.append(person)
        else:
            print(f"{person.name} is already in the library")

    def remove_user(self, person) -> None:
        if person not in self.users:
            print(f"{person.name} is not in the library")
        else:
            self.users.remove(person)
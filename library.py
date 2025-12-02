from person import Employer, Person
class Library:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.librarians = []
        self.books = []

    # ===== Librarians =====
    def add_librarian(self, person):
        if isinstance(person, Employer) or isinstance(person, Person):
            person.position = "Librarian"
            librarian = person
        else:
            print("Invalid object")
            return

        self.librarians.append(librarian)
        print(f"Librarian '{librarian.name}' added.")

    def remove_librarian(self, librarian, reason):
        if librarian in self.librarians:
            self.librarians.remove(librarian)
            librarian.__class__ = Employer
            librarian.position = ""
            librarian.status = ""
            print(f"Librarian '{librarian.name}' removed. Reason: {reason}")

    # ===== Books =====
    def add_book(self, book_name: str):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to library.")

    def remove_book(self, book_name: str):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' removed from library.")

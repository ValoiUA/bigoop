from book import Book
from person import Member, Employer

class Library:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.books = []
        self.loaned_books = []
        self.employers = []
        self.members = []
        self.transactions = []
        self.ranks = ["Trainee", "Librarian", "Head Librarian"]

    # ===== Books =====
    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from library.")
        else:
            print("Book not found in library.")

    def give_book(self, book: Book, member: Member):
        if book not in self.books:
            print("Book not found in library.")
            return
        if len(member.borrowed_books) >= member.max_books:
            print(f"Member {member.name} has reached the maximum number of books.")
            return
        self.books.remove(book)
        member.borrowed_books.append(book)
        self.loaned_books.append(book)
        self.transactions.append((book, member, "give"))
        print(f"Book '{book.title}' given to member '{member.name}'.")

    def return_book(self, book: Book, member: Member):
        if book not in member.borrowed_books:
            print(f"Member '{member.name}' does not have this book.")
            return
        member.borrowed_books.remove(book)
        self.loaned_books.remove(book)
        self.books.append(book)
        self.transactions.append((book, member, "return"))
        print(f"Book '{book.title}' returned by member '{member.name}'.")

    # ===== Members =====
    def add_member(self, member: Member):
        if member in self.members:
            print(f"Member '{member.name}' is already in library.")
            return
        if member.check_who() != "Unknown":
            print(f"Member '{member.name}' already has a position.")
            return
        self.members.append(member)
        member.position = "Library Member"
        print(f"Member '{member.name}' added to library.")

    def remove_member(self, member: Member, reason: str):
        if member not in self.members:
            print(f"Member '{member.name}' not found in library.")
            return
        self.members.remove(member)
        member.position = ""
        print(f"Member '{member.name}' removed from library. Reason: {reason}")

    # ===== Employers =====
    def add_employer(self, employer: Employer):
        if employer in self.employers:
            print(f"Employer '{employer.name}' is already in library.")
            return
        if employer.age < 18:
            print(f"Employer '{employer.name}' must be at least 18 years old.")
            return
        if employer.check_who() != "Unknown":
            print(f"Employer '{employer.name}' already has a position.")
            return
        self.employers.append(employer)
        employer.position = "Library Employer"
        employer.rank = "Trainee"
        print(f"Employer '{employer.name}' added to library.")

    def remove_employer(self, employer: Employer, reason: str):
        if employer not in self.employers:
            print(f"Employer '{employer.name}' not found in library.")
            return
        self.employers.remove(employer)
        employer.position = ""
        employer.rank = ""
        print(f"Employer '{employer.name}' removed from library. Reason: {reason}")

    def promote_employer(self, employer: Employer):
        if employer not in self.employers:
            print(f"Employer '{employer.name}' not found in library.")
            return
        if employer.rank == "Head Librarian":
            print(f"Employer '{employer.name}' is already a Head Librarian.")
            return
        if employer.rank == "Librarian":
            employer.rank = "Head Librarian"
            print(f"Employer '{employer.name}' promoted to Head Librarian.")
        else:
            employer.rank = "Librarian"
            print(f"Employer '{employer.name}' promoted to Librarian.")

    # ===== Logs =====
    def print_logs(self):
        print("Library Transactions:")
        for book, member, action in self.transactions:
            print(f"{action.upper()}: Book '{book.title}' with {member.name}")

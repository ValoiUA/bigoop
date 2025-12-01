class Book:
    def __init__(self, title, author, price, isbn, available=True):
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.available = available

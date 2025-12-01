class Person:
    def __init__(self, name: str, age: int, criminal_record: bool = False):
        self.name = name
        self.age = age
        self.position = ""
        self.criminal_record = criminal_record

    def check_who(self) -> str:
        if self.position == "Library Member":
            return "Library Member"
        elif self.position == "Library Employer":
            return "Library Employer"
        elif self.position == "Prisoner":
            return "Prisoner"
        else:
            return "Unknown"

class Member(Person):
    def __init__(self, name: str, age: int, max_books: int = 3):
        super().__init__(name, age)
        self.max_books = max_books
        self.borrowed_books = []

class Employer(Person):
    def __init__(self, name: str, age: int, criminal_record: bool):
        super().__init__(name, age, criminal_record)
        self.rank = ""


class Prisoner(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.prison_time = 0
        self.article = ""
        self.criminal_record = True
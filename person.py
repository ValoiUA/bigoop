import asyncio

class Person:
    def __init__(self, name: str, surname: str, age: int, x: int, y: int, criminal_record: bool = False) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.x = x
        self.y = y
        self.criminal_record = criminal_record

    def __str__(self) -> str:
        return f"Person: {self.name} {self.surname} has {self.age} y.o and crim is {self.criminal_record}"
    
    def ifcrim(self) -> bool:
        if self.criminal_record:
            return True
        else:
            return False
    
class Employyer(Person):
    def __init__(self, name, surname, age, x, y, criminal_record, rank: str, status: str):
        super().__init__(name, surname, age, x, y, scriminal_record)
        self.rank = rank
        self.status = status

    def __str__(self) -> str:
        return f"Employyer {self.name} {self.surname} {self.age} y.o status: {self.status}, rank: {self.rank}"

class PoliceOfficer(Employyer):
    def __init__(self, name, surname, age, x, y, criminal_record, status, rank, trained: bool):
        super().__init__(name, surname, age, x, y, criminal_record, status, rank)
        self.trained = trained
    def __str__(self) -> str:
        return f"Officer {self.name} {self.surname} {self.age} y.o status: {self.status}, rank: {self.rank}"
class Doctor(Employyer):
    def __init__(self, name, surname, age, x, y, criminal_record, status, rank):
        super().__init__(name, surname, age, x, y, criminal_record, status, rank)
    
class Prisoner(Person):
    def __init__(self, name: str, surname: str, age: int, x: int, y: int, criminal_record: bool, duration: int, rank: str, status: str) -> None:
        super().__init__(name, surname, age, x, y, criminal_record)
        self.criminal_record = True
        self.duration = duration

class Mayor(Employyer):
    def __init__(self, name, surname, age, x, y, criminal_record, status, rank):
        super().__init__(name, surname, age, x, y, criminal_record)
        self.status = status
        self.rank = rank

class Doctor(Employyer):
    def __init__(self, name, surname, age, x, y, criminal_record, status, rank):
        super().__init__(name, surname, age, x, y, criminal_record, status, rank)


class Patient(Person):
    def __init__(self, name: str, surname: str, age: int, x: int, y: int) -> None:
        super().__init__(name, surname, age, x, y)

class LibraryEmployer(Employyer):
    def __init__(self, name, surname, age, x, y, criminal_record, status, rank):
        super().__init__(name, surname, age, x, y, criminal_record, status, rank)

class LibraryUser(Person):
    def __init__(self, name, surname, age, x, y):
        super().__init__(name, surname, age, x, y)
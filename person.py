class Person:
    def __init__(self, name: str, age: int, criminal_record: bool = False):
        self.name = name
        self.age = age
        self.criminal_record = criminal_record

class Employer(Person):
    def __init__(self, name: str, age: int, criminal_record: bool = False):
        super().__init__(name, age, criminal_record)
        self.position = ""
        self.rank = ""
        self.status = "Free"
        self.location = None
        self.x = 0
        self.y = 0

class PoliceOfficer(Employer):
    def __init__(self, name: str, age: int, criminal_record: bool = False):
        super().__init__(name, age, criminal_record)
        self.rank = "Trainee Police"
        self.position = "Police Officer"
        self.training = False

class Doctor(Employer):
    def __init__(self, name: str, age: int, criminal_record: bool):
        super().__init__(name, age, criminal_record)
        self.rank = "Trainee Medic"
        self.position = "Medic"
        self.experience = 0

class Firefighter(Employer):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.rank = "Trainee Firefighter"
        self.position = "Firefighter"
        self.training = False

class Patient(Person):
    def __init__(self, name: str, age: int, position: str, degree: int, diagnosis, surgeon_need: bool) -> None:
        super().__init__(name, age, position)
        self.degree = degree
        self.diagnosis = diagnosis
        self.surgeon_need = surgeon_need
        self.x = 0
        self.y = 0


class Prisoner(Person):
    def __init__(self, name: str, age: int, x: int, y: int):
        super().__init__(name, age, criminal_record=True)
        self.prison_time = 0
        self.article = ""
        self.x = x
        self.y = y
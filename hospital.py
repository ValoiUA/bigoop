from person import Doctor, Employyer, Patient, Person
from pydoc import doc
import asyncio

from city import Street


class Hospital:
    def __init__(self, title: str, x: int, y: int) -> None:
        self.title = title
        self.x = x
        self.y = y
        self.doctors = []
        self.ranks = ["Doctor Trainee", "Surgeon", "Nurse", "Depart manager", "Main Doctor"]
        self.patients = []
        self.terms = {"Heart": 5, "Headache": 10, "stomachache": 15}
        self.calling = {"Heart": 5, "Headache": 10, "stomachache": 15}
    def __str__(self) -> str:
        return f"Hospital: {self.title} {self.x} {self.y}"
    

    def add_doctor(self, person) -> None:
        if person.age < 18:
            print(f"{person.name} must be at least 18 years old")
        if isinstance(person, Person):
            person.__class__ = Doctor
            person.status = "Free"
            person.rank = "Doctor Trainee"
            self.doctors.append(person)
        if person in self.doctors:
            print(f"{person.name} is already Doctor")
        if isinstance(person, Employyer):
            person.__class__ = Doctor
            person.status = "Free"
            person.rank = "Doctor Trainee"
        else:
            print(f"{person.name} is already working")
    
    def remove_doctor(self, doctor: Doctor) -> None:
        try:
            if doctor in self.doctors:
                doctor.status = "Free"
                doctor.rank = "Employyer"
                doctor.__class__ = Employyer
                self.doctors.remove(doctor)
            else:
                print(f"Person {doctor.name} is not in the hospital")
        except ValueError:
            print(f"Person {doctor.name} is not in the hospital")
    

    def promote_doctor(self, doctor: Doctor) -> None:
        try:
            if doctor in self.doctors:
                doctor.rank = self.ranks[doctor.rank + 1]
            else:
                print(f"Person {doctor.name} not doctor")
        except ValueError:
            print(ValueError)


    #======Patient======
    def add_patient(self, person, article: str):
        if person in self.patients:
            print(f"{person.name} already in hospital")        
        try:
            person.__class__ = Patient
            person.status = "At Hospital"
            time = self.terms = [article]
            self.person.append({person: time})
            print(f"{person.name} at prison now")
        except ValueError:
            print("no article")
        
    def free_patient(self, patient: Patient):
        if patient not in self.patients:
            print(f"{patient.name} not in hostital")
            patient.__class__ = Employyer
            patient.status = "Free"
            patient.rank = "Employyer"
            return
    

    #======Calling======
    def check_if_wall(self, doctor: Doctor, street: Street):
        pass
    
    async def doctor_go(self, doctor: Doctor, time_to_go: int, time_staying: int):
        print(f"doctor {doctor.name} go to street")
        asyncio.sleep(time_to_go)
        print(f"doctor {doctor.name} is on the street")
        asyncio.sleep(time_staying)
        print(f"doctor {doctor.name} leave the street")
        doctor.status = "Free"
    
    async def call_doctor(self, street: Street, article: str):
        time = self.calling[article]
        for doctor in self.doctors:
            if doctor.status == "Free":
                doctor.status = "On calling"
                timetogo = math.sqrt((street.x - doctor.x) ** 2 + (street.y - doctor.y) ** 2)
                self.calling_make(doctor, timetogo, time)
            
        
    async def calling_make(self, doctor: Doctor, timetogo: int, timestaying: int):
        asyncio.create_task(self.doctor_go(doctor, timetogo, timestaying))

    
    #======Patrooling======
    def goto_patrol(self, doctor: Doctor):
        pass
    
    def check_if_wall(self, doctor: Doctor):
        pass
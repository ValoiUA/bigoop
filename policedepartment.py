from person import Employyer, Person, PoliceOfficer, Prisoner
import asyncio
from city import Street
import math

class Police:
    def __init__(self, title: str, x:int, y: int) -> None:
        self.title = title
        self.x = x
        self.y = y
        self.officers = []
        self.ranks = ["Police Trainee", "Police Officer", "Police Leader"]
        self.training = [5, 10, 15]
        self.terms = {"Robbery" : 5, "Assault" : 10, "Killing": 15}
        self.prisoners = []
        self.calling = {"Robbery" : 5, "Assault" : 10, "Killing" : 15}

        
        asyncio.create_task(self.prison_time)

    #======Officer======

    def add_officer(self, person) -> None:
        if person.criminal_record:
            print(f"Person {person.name} has crim")
            return
        if person in self.officers:
            print(f"Person {person.name} is already an officer")
            return
        if isinstance(person, Person):
            person.__class__ = PoliceOfficer
            person.status = "Free"
            person.rank = "Police Trainee"
            person.trained = False
            self.officers.append(person)
            print(f"{person.name} is officer now")
        elif isinstance(person, Employyer):
            person.__class__ = PoliceOfficer
            person.status = "Free"
            person.rank = "Police Trainee"
            person.trained = False
            self.officers.append(person)
            print(f"{person.name} is officer now")
        else:
            print(f"{person.name} is already working")
    def remove_officer(self, officer: PoliceOfficer) -> None:
        try:
            if officer in self.officers:
                officer.status = "Free"
                officer.rank = "Employyer"
                officer.trained = False
                officer.__class__ = Employyer
                self.officers.remove(officer)
            else:
                print(f"Person {officer.name} is not in the police")
        except ValueError:
            print(f"Person {officer.name} is not in the police")
    
    def promote_officer(self, officer: PoliceOfficer) -> None:
        try:
            if officer in self.officers:
                if officer.trained:
                    officer.rank = self.ranks[officer.rank + 1]
                else:
                    print(f"Officer {officer.name} not trained")
            else:
                print("Person not officer")
        except ValueError:
            print(ValueError)

    async def run_training(self, officer: PoliceOfficer):
        print(f"{officer.name} start training")
        await self.training_officer(officer)

    async def training_officer(self, officer: PoliceOfficer):
        try:
            if officer in self.officers:
                if not officer.trained:
                    rank_index = self.ranks.index(officer.rank)
                    time_duration = self.training[rank_index]
                    officer.status = "Training"
                    await asyncio.sleep(time_duration)
                    print(f"Officer {officer.name} have trained")
                    officer.status = "Free"
                    officer.trained = True
                else:
                    print(f"Officer {officer.name} already trainde")
            else:
                print("Person not officer")
        except ValueError:
            print(ValueError)

    #======Prisoner=======
    async def prison_time(self):
        for i in self.prisoners:
            if self.prison_time[i] > 0:
                self.prison_time[i] -= 1
            else:
                self.free_prisoner(i)
            asyncio.sleep(1)
            

    def add_prisoner(self, person, article: str):
        if person in self.prisoners:
            print(f"{person.name} already in prison")
        try:
            person.__class__ = Prisoner
            person.status = "At Prison"
            time = self.terms[article]
            self.prisoners.append({person: time})
            print(f"{person.name} at prison now")
        except ValueError:
            print("no article")

    def free_prisoner(self, prisoner: Prisoner):
        if prisoner not in self.prisoners:
            print(f"{prisoner.name} not in prison")
            prisoner.duration = 0
            prisoner.__class__ = Employyer
            prisoner.status = "Free"
            prisoner.rank = "Employyer"
            return
        prisoner.duration = 0
        prisoner.criminal_record = True
        if prisoner.rank == "Employyer":
            prisoner.__class__ = Employyer
        elif prisoner.rank in self.ranks:
            prisoner.__class__ = PoliceOfficer
            
        
    #======Callings=======
    def check_if_wall(self, officer: PoliceOfficer, street: Street):
        pass
    async def officer_go(self, officer: PoliceOfficer, timetogo: int, time_staying: int):
        print(f"officer {officer.name} go to street")
        asyncio.sleep(timetogo)
        print(f"officer {officer.name} is in the street")
        asyncio.sleep(time_staying)
        print(f"officer {officer.name} leave the street")
        officer.status = "Free"
    
    async def call_police(self, street: Street, article: str):
        time = self.calling[article]
        for officer in self.officers:
            if officer.status == "Free":
                officer.status = "On calling"
                timetogo = math.sqrt((street.x - officer.x) ** 2 + (street.y - officer.y) ** 2)
                self.calling_make(officer, timetogo, time)    

    async def calling_make(self, officer: PoliceOfficer, timetogo: int, timestaying: int):
        asyncio.create_task(self.officer_go(officer, timetogo, timestaying))

    
    #======Patrooling=======
    def goto_patrol(self, officer: PoliceOfficer):
        pass

    def check_if_wall(self, officer: PoliceOfficer):
        pass

        



from person import Employer
import time
class Police:
    def __init__ (self, name: str, adress: str):
        self.name = name
        self.adress = adress
        self.employers = []
        self.prisoners = []
        self.ranks = ["Trainee Police", "Police Officer", "Police Captain"]
        self.articles = [{"Kill" : 10}, {"Rob" : 5}, {"Assault" : 3}]
        self.wit_crim = ["Trainee Police", "Police Officer", "Police Captain"]
    
    # ===== Employers =====
    def add_employer(self, employer: Employer):
        if employer.age < 21:
            print("Employer must be at least 21 years old.")
            return
        if employer.position != "Unknown":
            print("Employer already has a position.")
            return
        if employer.criminal_record == True:
            print("Employer has a criminal record.")
            return
        self.employers.append(employer)
        employer.rank = "Trainee Police" 
        employer.position = "Police Employer"
        print(f"Employer '{employer.name}' added to police.")

    def remove_employer(self, employer: Employer, reason: str):
        if employer not in self.employers:
            print(f"Employer '{employer.name}' not found in police.")
            return
        self.employers.remove(employer)
        employer.position = ""
        employer.rank = ""
        print(f"Employer '{employer.name}' removed from police. Reason: {reason}")
    
    def promote_employer(self, employer: Employer):
        if employer not in self.employers:
            print(f"Employer '{employer.name}' not found in police.")
            return
        if employer.rank == "Police Captain":
            print(f"Employer '{employer.name}' is already a Police Captain.")
            return
        if employer.rank == "Police Officer":
            employer.rank = "Police Captain"
            print(f"Employer '{employer.name}' promoted to Police Captain.")
        else:
            employer.rank = "Police Officer"
            print(f"Employer '{employer.name}' promoted to Police Officer.")


    # ===== Prisoners =====
    def add_prisoner(self, prisoner: Prisoner, article: str):
        if prisoner.age < 18:
            print("Prisoner must be at least 18 years old.")
            return
        for i in range(len(self.articles)):
            if article in self.articles[i]:
                time = self.articles[i][article]
        self.prisoners.append(prisoner)
        prisoner.prison_time = time
        asyncio.create_task(self._prison_timer())
        if prisoner.rank in self.wit_crim:
            prisoner.rank = ""
            prisoner.position = ""
        print(f"Prisoner '{prisoner.name}' added to police.")

    async def _prison_timer(self):
        while True:
            await asyncio.sleep(1)  
            for prisoner in self.prisoners[:]:
                prisoner.prison_time -= 1

                if prisoner.prison_time <= 0:
                    await self.free_prisoner(prisoner)
    
    async def free_prisoner(self, prisoner: Prisoner):
        if prisoner not in self.prisoners:
            print(f"Prisoner '{prisoner.name}' not found in police.")
            return
        self.prisoners.remove(prisoner)
        print(f"Prisoner '{prisoner.name}' removed from police.")

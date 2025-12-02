from person import Employer, Person, PoliceOfficer, Prisoner
from city import Location, Street
import asyncio
import math
class Police:
    def __init__ (self, name: str, x: int, y: int, city):
        self.city = city
        self.name = name
        self.x = x
        self.y = y
        self.employers = []
        self.prisoners = []
        self.ranks = ["Trainee Police", "Police Officer", "Police Captain", "SWAT officer", "SWAT Leader"]
        self.trainings = [5, 10, 15, 25, 100]
        self.articles = [{"Kill" : 10}, {"Rob" : 5}, {"Assault" : 3}]
        self.level = {"Robbing":5, "Assault":10, "Kill":15}
        self.wit_crim = [*self.ranks]
    async def start(self):
        asyncio.create_task(self._prison_timer())
    
    # ===== Officers =====
    async def _train_officers(self, officer: PoliceOfficer):
        if officer not in self.employers:
            print(f"Officer '{officer.name}' not found in police.")
            return
        if officer.training:
            print(f"Officer '{officer.name}' is already training.")
            return
        ranc = officer.rank
        time = self.trainings[self.ranks.index(ranc)]
        officer.status = "Training"
        await asyncio.sleep(time)
        officer.training = True
        officer.status = "Free"
        print(f"Officer '{officer.name}' finished training.")

    def add_police(self, person):
        if isinstance(person, PoliceOfficer):
            officer = person
        elif isinstance(person, Employer):
            officer = PoliceOfficer(name=person.name, age=person.age, criminal_record=person.criminal_record)
        elif isinstance(person, Person):
            officer = PoliceOfficer(name=person.name, age=person.age, criminal_record=person.criminal_record)
        else:
            print("Invalid object")
            return

        if officer.age < 21:
            print(f"Officer '{officer.name}' must be at least 21 years old.")
            return
        if officer.criminal_record:
            print(f"Officer '{officer.name}' has a criminal record.")
            return
        if officer in self.employers:
            print(f"{officer.name} is already in the police.")
            return
        self.employers.append(officer)
        officer.x = self.x
        officer.y = self.y
        print(f"Officer '{officer.name}' added to police.")

    def remove_officer(self, officer: PoliceOfficer, reason: str):
        if officer not in self.employers:
            print(f"Officer '{officer.name}' not found in police.")
            return
        self.employers.remove(officer)
        
        officer.__class__ = Employer
        officer.status = ""
        officer.rank = ""
        officer.position = ""
        officer.x = 0
        officer.y = 0
    
        print(f"Officer '{officer.name}' removed from police and is now a regular Employer. Reason: {reason}")

    def promote_officer(self, officer: PoliceOfficer):
        if officer not in self.employers:
            print(f"Officer '{officer.name}' not found in police.")
            return
        if officer.rank == "Trainee Police" and officer.training:
            officer.rank = "Police Officer"
        elif officer.rank == "Police Officer" and officer.training:
            officer.rank = "Police Captain"
        elif officer.rank == "Police Captain" and officer.training:
            officer.rank = "SWAT officer"
        elif officer.rank == "SWAT officer" and officer.training:
            officer.rank = "SWAT Leader"
        else:
            print(f"Officer '{officer.name}' is not trained.")
            return
        print(f"Officer '{officer.name}' promoted to {officer.rank}.")

    # ===== Prisoners =====
    def add_prisoner(self, person, article: str):
        if isinstance(person, Prisoner):
            prisoner = person
        elif isinstance(person, Person) or isinstance(person, Employer):
            prisoner = Prisoner(name=person.name, age=person.age)
        else:
            print("Invalid object")
            return

        if prisoner.age < 18:
            print("Prisoner must be at least 18 years old.")
            return

        prison_time = None
        for item in self.articles:
            if article in item:
                prison_time = item[article]

        if prison_time is None:
            print("Wrong article")
            return

        prisoner.prison_time = prison_time
        self.prisoners.append(prisoner)

        if prisoner.position in self.wit_crim:
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

    async def free_prisoner(self, prisoner):
        if prisoner in self.prisoners:
            self.prisoners.remove(prisoner)
            prisoner.__class__ = Employer
            prisoner.status = ""
            prisoner.rank = ""
            prisoner.position = ""
            prisoner.x = 0
            prisoner.y = 0
            print(f"Prisoner '{prisoner.name}' removed from police.")

    def remove_prisoner(self, prisoner: Prisoner, reason: str):
        if prisoner not in self.prisoners:
            print(f"Prisoner '{prisoner.name}' not found in police.")
            return
        self.prisoners.remove(prisoner)
        prisoner.__class__ = Employer
        prisoner.status = ""
        prisoner.rank = ""
        prisoner.position = ""
        prisoner.x = 0
        prisoner.y = 0
        print(f"Prisoner '{prisoner.name}' removed from police. Reason: {reason}")

    # ===== Calls =====

    def find_path(self, city, start, goal):
        from heapq import heappush, heappop

        (sx, sy) = start
        (gx, gy) = goal

        width = city.width
        height = city.height

        def neighbors(x, y):
            for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= nx < width and 0 <= ny < height:
                    if city.area[ny][nx] == " ":
                        yield (nx, ny)

        def heuristic(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        open_set = []
        heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}

        while open_set:
            _, current = heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for nxt in neighbors(*current):
                tentative_g = g_score[current] + 1
                if nxt not in g_score or tentative_g < g_score[nxt]:
                    g_score[nxt] = tentative_g
                    priority = tentative_g + heuristic(nxt, goal)
                    heappush(open_set, (priority, nxt))
                    came_from[nxt] = current

        return None


    async def officer_return(self, officer: PoliceOfficer, reason: str):
        officer.status = "Free"
        officer.location = None
        print(f"Officer '{officer.name}' returned to base. Reason: {reason}")


    async def _move_officer(self, officer: PoliceOfficer, target: Location, speed: float = 1.0):
        while True:
            dx = target.x - officer.x
            dy = target.y - officer.y
            distance = math.sqrt(dx*dx + dy*dy)
            if distance < 0.1:
                officer.x = target.x
                officer.y = target.y
                break
            step = min(speed * 0.1, distance)  
            officer.x += dx / distance * step
            officer.y += dy / distance * step
            await asyncio.sleep(0.1)

    def call_police(self, reason: str, location: Location, level: str):
        asyncio.create_task(self._call_police(reason, location, level))
    
    async def _call_police(self, reason: str, location: Location, level_key: str):
        level_time = self.level.get(level_key)
        if level_time is None:
            print(f"There is no level defined for '{level_key}'. Call aborted.")
            return
        nearest_officer = None
        min_distance = float('inf')

        for officer in self.employers:
            if officer.status == "Free":
                dist = math.sqrt((officer.x - location.x)**2 + (officer.y - location.y)**2)
                if dist < min_distance:
                    min_distance = dist
                    nearest_officer = officer

        if nearest_officer is None:
            print("No officers are free now")
            return

        officer = nearest_officer
        officer.status = "On call"
        officer.location = location

        print(f"{officer.name} is the nearest officer (distance {min_distance:.1f}).")
        print(f"{officer.name} (Level {level_key}) is going to {location.name}...")
        print(f"[{officer.name}] Reason: {reason}")

        speed = 1 

        while (round(officer.x), round(officer.y)) != (location.x, location.y):

            path = self.find_path(
                self.city,
                (round(officer.x), round(officer.y)),
                (location.x, location.y)
            )

            if not path:
                print(f"{officer.name} cannot reach {location.name}, path blocked!")
                officer.status = "Free"
                return

            for (nx, ny) in path:
                officer.x = nx
                officer.y = ny
                print(f"[MOVE →] {officer.name} at ({nx}, {ny})")
                await asyncio.sleep(0.2)


        print(f"{officer.name} arrived at {location.name}! Processing incident...")

        await asyncio.sleep(level_time)

        print(f"{officer.name} finished: {reason}. Returning to base...")
        base_x, base_y = self.x, self.y

        while officer.x != base_x or officer.y != base_y:

            if officer.x < base_x: officer.x += min(speed, base_x - officer.x)
            elif officer.x > base_x: officer.x -= min(speed, officer.x - base_x)

            if officer.y < base_y: officer.y += min(speed, base_y - officer.y)
            elif officer.y > base_y: officer.y -= min(speed, officer.y - base_y)

            print(f"[MOVE ←] {officer.name} at ({officer.x}, {officer.y})")
            await asyncio.sleep(0.3)
        officer.status = "Free"
        officer.location = None
        print(f"{officer.name} returned to base. Ready for next call.")


    



    



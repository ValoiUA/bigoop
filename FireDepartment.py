from person import Employer, Person

class FireDepartment:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.firefighters = []
        self.fires = []
        self.levels = {"Small":5, "Medium":10, "Large":15}

    # ===== Firefighters =====
    def add_firefighter(self, person):
        if isinstance(person, Employer) or isinstance(person, Person):
            person.position = "Firefighter"
            firefighter = person
        else:
            print("Invalid object")
            return

        self.firefighters.append(firefighter)
        firefighter.x = self.x
        firefighter.y = self.y
        print(f"Firefighter '{firefighter.name}' added.")

    def remove_firefighter(self, firefighter, reason):
        if firefighter in self.firefighters:
            self.firefighters.remove(firefighter)
            firefighter.__class__ = Employer
            firefighter.position = ""
            firefighter.status = ""
            firefighter.x = 0
            firefighter.y = 0
            print(f"Firefighter '{firefighter.name}' removed. Reason: {reason}")

    # ===== Fires =====
    def report_fire(self, location_name: str, level: str):
        fire_time = self.levels.get(level)
        if fire_time is None:
            print("Invalid fire level")
            return
        self.fires.append({"location": location_name, "time": fire_time})
        print(f"Fire reported at {location_name}, level {level}")

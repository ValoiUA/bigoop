from person import Person


class City:
    def __init__(self, name: str, areax: int, areay: int, population: int) -> None:
        self.name = name
        self.areax = areax
        self.areay = areay
        self.population = population
    def __str__(self) -> str:
        return f"City: {self.name} {self.areax} {self.areay} {self.population}"
    
class Street:
    def __init__(self, name: str, x: int, y:int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.buildings = []
    def __str__(self) -> str:
        return f"Street: {self.name} {self.x} {self.y}"
    
    def put_buiding(self, building) -> None:
        if isinstance(building, Police):
            self.buildings.append(building)
        
    def break_building(self, building) -> None:
        if isinstance(building, Police):
            self.buildings.remove(building)
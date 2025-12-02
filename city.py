class City:
    def __init__(self, name, population, width, height):
        self.name = name
        self.population = population
        self.width = width
        self.height = height
        self.area = [[" " for _ in range(width)] for _ in range(height)]

    def put_building(self, x, y, building="B"):
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.area[y][x] == " ":
                self.area[y][x] = building
            else:
                print(f"Щось вже є на {x},{y}")
        else:
            print("Координати поза межами міста")

    def add_street(self, street):
        for x, y in street.coordinates:
            if 0 <= x < self.width and 0 <= y < self.height:
                if self.area[y][x] == "B":
                    self.area[y][x] = "X"
                else:
                    self.area[y][x] = "S"

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.area)


class Location:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y


class Street:
    def __init__(self, name: str, coordinates: list[tuple[int,int]]):
        self.name = name
        self.coordinates = coordinates

    def random_location(self) -> Location:
        import random
        x, y = random.choice(self.coordinates)
        return Location(f"On {self.name}", x, y)
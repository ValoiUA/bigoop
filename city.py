class City:
    def __init__(self, name, population, width, height):
        self.name = name
        self.population = population
        self.width = width
        self.height = height
        self.area = [["1" for i in range(width)] for j in range(height)]
    def put_building(self, x, y, building):
        if self.area[y][x] != "1":
            self.area[y][x] = building
        else:
            print("Building already exists.")
    def remove_building(self, x, y):
        if self.area[y][x] != "1":
            self.area[y][x] = "1"
        else:
            print("Building already doesn't exist.")
    def __str__(self):
        return "\n".join(" ".join(row) for row in self.area)

city = City("New York", 8000000, 10, 10)
print(city)
import tkinter as tk
import asyncio
import random
import threading
from city import City, Location, Street
from policeot import Police
from person import Employer, PoliceOfficer, Doctor, Firefighter, Patient
from library import Library
from hospital import Hospital
from FireDepartment import FireDepartment

# ===== Створюємо місто =====
city_width, city_height = 20, 15
city = City("Metropolis", 1000, city_width, city_height)

# Додаємо деякі будівлі
city.put_building(2, 2, "H")  # Hospital
city.put_building(5, 5, "P")  # Police
city.put_building(8, 8, "L")  # Library
city.put_building(12, 3, "F") # Fire Department

# ===== Створюємо служби =====
police_dept = Police("Police HQ", 5, 5, city)
hospital = Hospital("City Hospital", 2, 2)
fire_dept = FireDepartment("Fire Station", 12, 3)
library = Library("Central Library", 8, 8)

# ===== Додаємо людей =====
police_dept.add_police(PoliceOfficer("John", 30))
police_dept.add_police(PoliceOfficer("Alice", 25))
police_dept.add_police(PoliceOfficer("Bob", 40))

hospital.add_doctor(Doctor("Eve", 32, False))
hospital.add_doctor(Doctor("Charlie", 29, False))

fire_dept.add_firefighter(Firefighter("Mike", 28))
fire_dept.add_firefighter(Firefighter("Anna", 35))

library.add_librarian(Employer("Lucy", 27))
library.add_librarian(Employer("Tom", 33))

# ===== GUI =====
root = tk.Tk()
root.title("City Simulation")
cell_size = 30
canvas = tk.Canvas(root, width=city_width*cell_size, height=city_height*cell_size, bg="white")
canvas.pack()

# ===== Відображення =====
def draw_entities():
    canvas.delete("all")
    # Малюємо будівлі
    for y in range(city_height):
        for x in range(city_width):
            cell = city.area[y][x]
            color = "lightgray" if cell != " " else "white"
            canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill=color, outline="black")
            if cell == "H": canvas.create_text(x*cell_size+15, y*cell_size+15, text="H")
            if cell == "P": canvas.create_text(x*cell_size+15, y*cell_size+15, text="P")
            if cell == "L": canvas.create_text(x*cell_size+15, y*cell_size+15, text="L")
            if cell == "F": canvas.create_text(x*cell_size+15, y*cell_size+15, text="F")

    # Малюємо людей
    for e in police_dept.employers:
        canvas.create_rectangle(e.x*cell_size, e.y*cell_size, (e.x+1)*cell_size, (e.y+1)*cell_size, fill="blue")
        canvas.create_text(e.x*cell_size+15, e.y*cell_size+15, text=e.name[0])

    for e in hospital.doctors + hospital.patients:
        canvas.create_rectangle(e.x*cell_size, e.y*cell_size, (e.x+1)*cell_size, (e.y+1)*cell_size, fill="red")
        canvas.create_text(e.x*cell_size+15, e.y*cell_size+15, text=e.name[0])

    for e in fire_dept.firefighters:
        canvas.create_rectangle(e.x*cell_size, e.y*cell_size, (e.x+1)*cell_size, (e.y+1)*cell_size, fill="orange")
        canvas.create_text(e.x*cell_size+15, e.y*cell_size+15, text=e.name[0])

    for e in library.librarians:
        canvas.create_rectangle(e.x*cell_size, e.y*cell_size, (e.x+1)*cell_size, (e.y+1)*cell_size, fill="green")
        canvas.create_text(e.x*cell_size+15, e.y*cell_size+15, text=e.name[0])

async def update_loop():
    while True:
        draw_entities()
        await asyncio.sleep(0.2)

# ===== Симуляції подій =====
async def simulate_events():
    while True:
        # Виклики поліції
        loc = Location("Random Street", random.randint(0, city_width-1), random.randint(0, city_height-1))
        police_dept.call_police("Robbery", loc, "Robbing")

        # Пацієнти
        hospital.add_patient(Employer(f"Patient{random.randint(1,100)}", random.randint(10,80)), random.choice(["Minor","Moderate","Severe"]))

        # Пожежі
        fire_dept.report_fire(f"Building {random.randint(1,city_width)}", random.choice(["Small","Medium","Large"]))

        await asyncio.sleep(5)

# ===== Запуск =====
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(update_loop(), simulate_events()))

loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(loop,), daemon=True)
t.start()

root.mainloop()

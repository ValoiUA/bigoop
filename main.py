from person import Person, PoliceOfficer, Employyer
from policedepartment import Police
import asyncio

p = Person("John", "Gays", 19, 1, 1)
p1 = Person("Martin", "Lega", 24, 1, 2)
police = Police("Title", 1, 2)
police.add_prisoner(p, "Robbery")


# async def main_simulation():
#     # 1. Синхронне додавання офіцерів (не використовуємо await)
#     # Якщо метод add_officer не має await, він має бути синхронним!
#     police.add_officer(p) 
#     police.add_officer(p1) 
    
#     # ПРИМІТКА: Об'єкти p та p1 ТЕПЕР є PoliceOfficer завдяки логіці конвертації.

#     # 2. Створення незалежних задач для паралельного виконання
#     task_john = asyncio.create_task(police.run_training(p))
#     task_martin = asyncio.create_task(police.run_training(p1))
    
#     print("Тренування розпочато паралельно...")
    
#     # 3. Очікування завершення обох задач одночасно
#     # Якщо Джон тренується 5с, а Мартін 10с, ми чекаємо лише 10с.
#     await task_john
#     await task_martin 

#     print("Тренування завершено.")
#     print(f"Закінчили. Статус тренування Джона: {p.trained}")
#     print(f"Закінчили. Статус тренування Мартіна: {p1.trained}")

# if __name__ == "__main__":
#     asyncio.run(main_simulation())


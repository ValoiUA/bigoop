import asyncio
import math

from person import Employer, Person, Patient, Doctor

class Hospital:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.doctors = []
        self.patients = []
        self.levels = {"Minor":5, "Moderate":10, "Severe":15}
    async def start(self):
        asyncio.create_task(self._patient_timer())

    # ===== Doctors =====
    def add_doctor(self, person):
        if isinstance(person, Doctor):
            doctor = person
        elif isinstance(person, Employer) or isinstance(person, Person):
            doctor = Doctor(name=person.name, age=person.age, criminal_record=getattr(person, 'criminal_record', False))
        else:
            print("Invalid object")
            return
        
        if doctor.age < 21:
            print(f"Doctor '{doctor.name}' must be at least 21 years old.")
            return
        
        if doctor in self.doctors:
            print(f"{doctor.name} is already working in the hospital.")
            return
        
        self.doctors.append(doctor)
        doctor.x = self.x
        doctor.y = self.y
        print(f"Doctor '{doctor.name}' added to hospital.")

    def remove_doctor(self, doctor, reason):
        if doctor not in self.doctors:
            print(f"Doctor '{doctor.name}' not found in hospital.")
            return
        self.doctors.remove(doctor)
        doctor.__class__ = Employer
        doctor.status = ""
        doctor.rank = ""
        doctor.position = ""
        doctor.x = 0
        doctor.y = 0
        print(f"Doctor '{doctor.name}' removed from hospital. Reason: {reason}")

    # ===== Patients =====
    def add_patient(self, person, level: str):
        if isinstance(person, Patient):
            patient = person
        elif isinstance(person, Person) or isinstance(person, Employer):
            patient = Patient(name=person.name, age=person.age, position="Patient", degree=0, diagnosis="", surgeon_need=False)
        else:
            print("Invalid object")
            return

        treat_time = self.levels.get(level)
        if treat_time is None:
            print("Wrong level")
            return

        patient.degree = treat_time
        self.patients.append(patient)
        print(f"Patient '{patient.name}' admitted to hospital.")

    async def _patient_timer(self):
        while True:
            await asyncio.sleep(1)
            for patient in self.patients[:]:
                patient.degree -= 1
                if patient.degree <= 0:
                    self.discharge_patient(patient)

    def discharge_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"Patient '{patient.name}' discharged from hospital.")

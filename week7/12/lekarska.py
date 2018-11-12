# lekarz, pacjent, w ciagu dnia lekarz moze przyjac 4 pacjentów
# jak bedzie sie chcialo zapisac wiecej pacjetow niz 4 to powinno wywolac wyjatek

# obiekty Clinic, Doctor, Pacient, Day

# Clinic - zapisuje pacjenta, wyswietla  per_day lub per_doctor
# Day - przechowuje liste lekarzy i liste pacjentow dla danego pacjenta, max 4 pacjentow
# nie moze byc tak, ze w miejsce lekarza wpiszemy pacjenta (sprawdzamy czy dany obiekt jest z klady Doctor)
# Pacient - ma imie , nazwisko

import random
class Human:
    def __init__(self, first_name, secname):
        self.first_name = first_name
        self.secname = secname
    def full_name(self):
        return f"{self.first_name} {self.secname}"

class Patient(Human):
    pac_num = 0
    def __init__(self, name, secname):
        Human.__init__(self, name, secname)
        Patient.pac_num +=1

class Doctor(Human):
    def __init__(self, name, secname):
        Human.__init__(self, name, secname)

class Day:
    def __init__(self, name):
        self.name = name
        self.list={}
    def append(self, doctor, patient):
        if not doctor.full_name in self.schedule:
            cls.schedule[day,name].append[doctor,patient]
        self.list[doctor.full_name].append(patient)

class Clinic:
    calendar = {}
    @classmethod
    def schedule(cls, day, doctor, patient):
        #zapsiuje pacjenta do lekarza
        if not  day.name in cls.calendar:
            cls.calendar[day.name] = day
        cls.calendar[day.name].append[doctor, patient]

    @classmethod
    def print_per_doc(cls, doctor, patient):
        pass

    @classmethod
    def print_per_day(cls, name):
        pass


doc1 = Doctor("doctor1" , "doctor1")
pat1 = Patient("Pat1", "Pat1")
pat2 = Patient("Pat2", "Pat2")
pat3 = Patient("Pat3", "Pat3")
pat4 = Patient("Pat4", "Pat4")
pat5 = Patient("Pat5", "Pat5")
pat6 = Patient("Pat6", "Pat6")
print(Patient.pac_num)
Clinic.schedule()
Clinic.print_per_day()
print(pat1.name)

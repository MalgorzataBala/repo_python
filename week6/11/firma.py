#firma z pracownikami, roznie wyliczane miesieczne wynagrodzenie
#stawka tygodniowa, satwka miesieczna
# kazdy pracownik posiada imie i nazwisko

class Employee: #klasa bazowa
    def __init__(self, first_name, second_name, stawka):
        self.first_name = first_name
        self.second_name = second_name
        self.stawka = stawka

    def __str__(self):
        return f'{self.first_name}  {self.second_name}'

class EmployeeHourly(Employee):
   # def __init__(self, first_name, second_name, stawka):
    #    super().__init__(first_name,second_name)

    def hsalary(self, czas_pracy):
        self.czas_pracy = czas_pracy
        #stawkaa = 40
        return self.stawka * czas_pracy

class EmployeeSalary(Employee):
    def salary(self, godziny):
        return (godziny/168)*self.stawka

jan_kowalski = EmployeeHourly('Jan','Kowalski', 100)
marek_nowak = EmployeeSalary('Marek', 'Nowak', 2000)

print(jan_kowalski.hsalary(20))
print(marek_nowak)
print(jan_kowalski.first_name)
print(marek_nowak.salary(50))

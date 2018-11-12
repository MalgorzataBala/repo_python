from engines import Silniki
from cars import Cars
silnik1 = Silniki("2.0", "Diesel", "200")
silnik2 = Silniki("2.0", "Diesel", "220")
print(silnik1.pojemnosc)
print(silnik1.rodzaj_silnika)
print(silnik1.ile_koni)

car1= Cars("Volvo","V60", "Black metalic", silnik1)
car2= Cars("Volvo","V40", "Black metalic", silnik2)
print(car1.mark, car1.model, car1.colour)

def ktory_szybszy(s1,s2):
 if s1.ile_koni > s2.ile_koni :
   return s1
 else:
   return s2

zwyciezca = ktory_szybszy(silnik1,silnik2)
print("szybszy jest: ", zwyciezca)
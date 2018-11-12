
#POLA KLASY
class Osoba:
    ilosc_osob = 0
    def __init__(self, imie, nazwisko):
        Osoba.ilosc_osob+=1
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        print(self. imie, self.nazwisko)
    @classmethod   #metoda klasy
    def zeruj_licznik(cls):
        print(Osoba.ilosc_osob)
        cls.ilosc_osob =0

jan = Osoba('Jan', 'Kowalski')
#print(jan.imie )
jan.przedstaw_sie() #odnosimy sie do obiektu
Osoba.zeruj_licznik()#odnosimy sie do klasy i dokopujemy sie pola klasy

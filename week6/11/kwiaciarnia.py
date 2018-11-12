
#   kwiat       bukiet     kwiaciarnia
#   -cena       -kwiaty     -zrob_bukiet
#   -nazwa                  - wystaw_rachunek

class Kwiat:
    def __init__(self, lista_kwiatow):
        self.lista_kwiatow = lista_kwiatow

class Bukiet(Kwiat):
    def __init__(self, kwiat, cena):
        self.kwiat = kwiat
        self.cena = cena
    def __add__(self, other):
        r = self.cena + other.cena
        return r

class Kwiaciarka(Bukiet):
    def zrobiony_bukiet(self):

        pass

kwiaty = Kwiat({
"Róża" :Bukiet("Róża", 10),
"Tulipan": Bukiet("Tulipan", 12)
})

print(kwiaty.lista_kwiatow)
"""
Program który wyszukuje Liczby doskonałe https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a do podanego zakresu:
  - korzystamu z wcześniej napisanej funkcji sumator do sumowania liczb w zakresie. Uwaga zostawiamy ją w innym pliku i ćwiczymy importy
  - potrzebujemy listę pomocniczą do przechowywania dzielników
  - potrzebujemy funkcją testującą czy liczba jest dzielnikiem
"""
def sumator(lista_suma):
    suma = 0
    for i in lista_suma:
        suma = suma + i
    return suma

def duplikaty(listaa):
    druga_lista =[]
    for i in listaa:
        if i not in druga_lista:
            druga_lista.append(i)
    return druga_lista

def dzielnik(lista_dziel):
    dzielniki = []
    x=len(lista_dziel)
    #print(x)
    liczba = lista_dziel.index(x)
    #print(liczba)
    index = 1
    while index <= x/2:
        #print(index,"<=",x,"/2")
        if x %index == 0:
            dzielniki.append(index)
           # print(dzielniki)
        index = index + 1
    return dzielniki


def l_perfekcyjna(liczba):
    zakres = range(1,liczba+1)
    dzielniki_list = dzielnik(zakres)
    suma_dziel = sumator(dzielniki_list)
    if suma_dziel == liczba:
        return True
    else:
        return False




liczbaa= 28
#zakres = range(1,liczbaa+1)
#z= dzielnik(zakres)
#z = dzielnik(range(1,liczbaa))
z=l_perfekcyjna(liczbaa)
print(z)

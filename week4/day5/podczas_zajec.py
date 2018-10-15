"""def give_square(x,y,z):
    return y+"xxx", x**2, z+z


wywolanie = give_square(2,"zz", [1,2,3,4,5])
print(wywolanie)

def foo(imie, nazwisko):
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    return f"{imie} \t {nazwisko}"

napis=foo("celina","eugenia")
print(napis)

#temat na rozmowie kwalifikacyjnej - bez cleara do listy ciagle beda dodawane argumenty

def dodaj_imie(imie, imiona = None):
    if imiona == None:
        imiona = []
    imiona.append(imie)
    return imiona

i=[]
dodaj_imie("Adam",i)
dodaj_imie("Monia",i)
dodaj_imie("Jurek",i)

print(i)



imie = "Ania"
def i():
    imie = "Jola"
    print("w srodku   ",imie)

i()
print(" NA ZEWNATRZ",imie)


imie = "Ania"
def i():
    #global imie
    imie = "Jola"
    print("w srodku   ",imie)

i()
print(" NA ZEWNATRZ",imie)


imiona=[]
def i():
    imiona.append("Ania")
i()
print(" NA ZEWNATRZ",imiona)

"""

def sumator(lista_suma):
    suma = 0
    for i in lista_suma:
        suma = suma + i
    return suma

ista_suma = [1, 2, 3, 4, 5, 6]
x = sumator(ista_suma)
print(x)


#funkcja sprawdzajace czy podany napis jest palindromem

def palindrom(slowo):
    slowo = slowo.lower()
    len_slowo = len(slowo)-1
    j = len_slowo
    k = 0
    while k in range(len_slowo):
        if k != j:
            if slowo[k] == slowo[j]:
                j-=1
                k +=1
            else:
                slowo= slowo+" nie"
        k = len_slowo
    return slowo +" jest palindromem"

z = palindrom("kamil ślimak")
print(z)


def trywial_palindrom(slowoo):
    #samym returnem
    #return slowoo==slowoo[::-1]
    if slowoo == slowoo[::-1]:
        return slowoo+" jest palidromem"
    else:
        return slowoo+" nie jest palindromem"

m= trywial_palindrom("kajafgdgk")
print(m)

#szukanei liczb perfekcyjnych tzn. liczba której suma wszystkie dzielniki naruralne lub suma wszystkich dzielników plu sta l
#np 6, 1+2+3 =6
#   1. test czy jest dzielnikiem
#   2. lista na dzielniki
#   3. sumator z zadania 1 (*import)
#   4. porównanie wyników

#owrotna notacja polska

#trojka pascala - pseudo kod


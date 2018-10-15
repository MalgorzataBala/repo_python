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
                j=len_slowo-1
                k = k + 1
            else:
                slowo= slowo+" nie"
        k = len_slowo
    return slowo +" jest palindromem"

z = palindrom("kamil ślimak")
print(z)


def trywial_palindrom(slowoo):
    if slowoo == slowoo[::-1]:
        return slowoo+" jest palidromem"
    else:
        return slowoo+" nie jest palindromem"

m= trywial_palindrom("kajafgdgk")
print(m)
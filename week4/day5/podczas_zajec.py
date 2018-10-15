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
"""

imiona=[]
def i():
    imiona.append("Ania")
i()
print(" NA ZEWNATRZ",imiona)
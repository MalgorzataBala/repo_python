# Funkcję zliczającą wielkie i małe litery w zadanym stringu.
# Pamiętamy tabele ASCII i jak są ułożone wielkie i małe litery?
# https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html dodatkowo przypominamy funkcję `ord` która dla
#  zadanej litery zwraca jej numer z tabeli ascii.

def licz_male_duze_litery(x):
    ilosc_znakow = int(len(zadany_string))
    duze_litery = 0
    male_litery =0
    for i in range(ilosc_znakow):
        numer_ascii = ord(zadany_string[i])

        if numer_ascii>=65 and numer_ascii<=90:
            duze_litery = duze_litery+1
        elif numer_ascii>=97 and numer_ascii<=122:
            male_litery += 1
        else:
            return
    return "Duze litery: ", duze_litery,"Małe litery: ", male_litery




zadany_string = input("Podaj jakis string, któy posiada male i wielkie litery: \n")
wywolaj_funkcje = licz_male_duze_litery(zadany_string)
print(wywolaj_funkcje)
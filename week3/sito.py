#sito erystotelesa - wyszukiwanie liczb pierwszych


# szukam wielokrotnsci liczb
def sito_eras (nn):
    tablica_nowa = []
    # tworze tablice
    for z in range(2, nn):
        tablica_nowa.append(z)
    for z in tablica_nowa:
        for j in range(2, nn):
            if (z * j) in tablica_nowa:
                tablica_nowa.remove(z * j)
    return tablica_nowa

z = sito_eras(14)
print("Liczby pierwsze z zakresu : ",z)

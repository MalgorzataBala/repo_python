#sito erystotelesa - wyszukiwanie liczb pierwszych

nn = 10

tablica_nowa = []
#tworze tablice
for z in range(2, nn):
    tablica_nowa.append(z)

print(tablica_nowa)

# szukam wielokrotnsci liczb

for z in tablica_nowa:
    for j in range(2, nn):
        if (z * j) in tablica_nowa:
            tablica_nowa.remove(z * j)

print("Liczby pierwsze z zakresu : ",tablica_nowa)
#Multiplikator czyli na wzór sumatora chcemy przemnożyć wszystkie liczby z zadanej listy.
# Nie kopiujemy próbujemy napisać sami

def multiplikator(zakres):
    silnia = 1
    for i in zakres:
        silnia *= i
    return silnia

x = int(input("Podaj jakąć liczbę, a ja obliczę jej silnie: "))
zakres_usera  = range(1, x+1)
z = multiplikator(zakres_usera)
print(z)
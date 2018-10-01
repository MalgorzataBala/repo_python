


input_liczba = input("Podaj liczbę do sprawdzenia podzielności ")
s = str(input_liczba)
print(s)
list_of_string = list(s)
print(list_of_string)
konwert_to_int = [int(i) for i in list_of_string]
print(konwert_to_int)
summ = sum(konwert_to_int)
print(summ)
if summ in(3,6,9):
    print(input_liczba, "- jest podzielna przez 3")
if summ>9:
    ret = (sum(map(int, str(summ)))
    print(ret)


"""
number = 3424
print(sum(map(int, str(number))))
"""
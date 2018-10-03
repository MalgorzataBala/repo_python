
#.isdigir() sprawdza czy napis jest liczba
input_liczba = input("Podaj liczbę do sprawdzenia podzielności ")
if input_liczba.isdigit()==True:

    length = len(input_liczba)

    i =1
    suma=0
    for i in input_liczba[length]:
        #suma = input_liczba[i]+ suma
        #x = input_liczba[i]
        print(i)
    input_liczba = int(input_liczba)
    if suma % 3 == 0:
        print(input_liczba, "Jest podzielna przez 3!")


else:
    print("Podaj liczbe!")
    '''

a=15
if a%3==0:
    print(a, "jest podzielna przez 3")

if a%5==0:
    print(a, "jest podzielna przez 5")

if a%7==0:
    print(a, "jest podzielna przez 7")
    
if not checked:
    print("Liczna nie jest podzielna przez 3, ani przez 5, ani przez 7!")
    '''
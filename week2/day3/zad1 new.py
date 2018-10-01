"""
Napisz skrypt który oblicza obwód i pole powierzchni podstawowych figur geometrycznych jak trójkąt.
(wersja podstawowa wystarczą zdefiniowane zmienne przechowujące podstawowe wartosci jak długości boków czy wysokość,
wersja zaawansowana może zakładać podstawowe menu dla użytkownika które odpytuje o poszczególne dane
"Podaj jaką figurę chcesz obiczyc 1. trojkąt 2. kwadrat i w zależności od wprowadzonych wartości prosi o odpowiednie dane)
"""

input_usera = int(input("Podaj jaką figurę chcesz obiczyc : 1. trojkąt 2. kwadrat:  "))
#input_usera = int(input_usera)
#print(input_usera)
a=1
b=2

if input_usera == a:
    input_usera_h = input("Podaj długość boku trójkata : ")
    input_usera_h = int(input_usera_h)
    input_usera_a = input("Podaj długość wysokości opuszczonej na wcześniej podany bok : ")
    input_usera_a = int(input_usera_a)
    input_usera_b = input("Podaj długość drugiego boku trójkąta: ")
    input_usera_b = int(input_usera_b)
    input_usera_c = input("Podaj długość trzeciego boku trójkąta: ")
    input_usera_c = int(input_usera_c)
    if input_usera_a+input_usera_b>input_usera_c & input_usera_b+input_usera_c>input_usera_a & input_usera_a+input_usera_c>input_usera_b:
        Pole = (input_usera_a*input_usera_h)/2
        Obwod = input_usera_a+ input_usera_b+input_usera_c
        print ("Pole trojkąta wynosi: ", Pole)
        print("Obwód trójkąta wynosi:  ", Obwod)

    else:
        print("Z podanych długości boków nie można zbudować trójkąta!")




elif input_usera == b:
    input_usera_a =[a,b]
    input_usera_a = input("Podaj długość boków kwadratu : ")
    input_usera_a = int(input_usera_a)

    Pole = input_usera_a*input_usera_a
    Obwod = 4*input_usera_a

    print("Pole kwdratu wynosi: ", Pole)
    print("Obwód kwadratu wynosi:  ", Obwod)


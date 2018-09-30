"""
Napisz skrypt który oblicza obwód i pole powierzchni podstawowych figur geometrycznych jak trójkąt.
(wersja podstawowa wystarczą zdefiniowane zmienne przechowujące podstawowe wartosci jak długości boków czy wysokość,
wersja zaawansowana może zakładać podstawowe menu dla użytkownika które odpytuje o poszczególne dane
"Podaj jaką figurę chcesz obiczyc 1. trojkąt 2. kwadrat i w zależności od wprowadzonych wartości prosi o odpowiednie dane)
"""

input_usera = input("Podaj jaką figurę chcesz obiczyc : 1. trojkąt 2. kwadrat")

if input_usera = "1"
    input_usera_h = input("Podaj długość boku trójkata : ")
    input_usera_h = int(input_usera_h)
    input_usera_a = input("Podaj długość wyskości opuszczonej na wcześniej podany bok : ")
    input_usera_a = int(input_usera_a)
    input_usera_b = input("Podaj długość drugiego boku trójkąta: ")
    input_usera_b = int(input_usera_b)
    input_usera_c = input("Podaj długość trzeciego boku trójkąta: ")
    input_usera_c = int(input_usera_c)

    Pole = (input_usera_a*input_usera_h)/2
    Obwod = input_usera_a+ input_usera_b+input_usera_c
    print ("Pole trojkąta wynosi: ", Pole)
    print("Obwód trójkąta wynosi:  ", Obwod)

if input_usera = "2"
    input_usera_a = input("Podaj długość boku kwadratu : ")
    input_usera_a = int(input_usera_a)

    Pole = input_usera_a*input_usera_a
    Obwod = 4*input_usera_a

    print("Pole kwdratu wynosi: ", Pole)
    print("Obwód kwadratu wynosi:  ", Obwod)

    
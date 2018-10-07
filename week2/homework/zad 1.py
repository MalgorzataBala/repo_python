"""
Popularna gra słowna FizzBuzz
- wypisz liczby od 1 do 100 (wlacznie)
- jesli podzielna przez 3 to napisz Fizz
- jesli podzilena przez 5 to napisz Buzz
- jesli podzielna przez 3 i przez 5 to napisz FizzBuzz

"""
number = 1
for number in range(100):
    number = number + 1
    napis = ""

    if number % 3 == 0:
        napis = "Fizz"
        if number % 5 == 0:
            napis = napis  + "Buzz"
    elif number % 5 == 0:
        napis = "Buzz"
    print(number, " ", napis)




input_imie = input("Podaj imie: ")

if input_imie.endswith("a") == True:
    if len(input_imie.split()) ==2:
        print(input_imie, "Podane imię jest męskie")
    else:
        print(input_imie, "Podane imię jest żeńskie.")
else:
    print(input_imie, "Podane imię jest męskie")


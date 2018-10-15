"""

KSIĄŻKA ADRESOWA
1. dane ["Jan","kowalski", "777777777"]
2. menu
3.komendy :
	-wyszukiwanie
	-dodawanie użytkowników
	-usuwanie
	-edytowanie
"""

input_user=int(input("Wybiersze co chcesz zrobić: \n 1 - Wyszukiwanie \n 2 - Dodawanie Użytkowników \n 3 - Usuwanie \n 4 - Edytowanie danych \n"))

if input_user == 1:
    input_szukaj = int(input("Wyszukiwanie po : \n 1 - Imieniu \n 2 - Nazwisko \n 3 - nr telefonu \n"))
    if input_szukaj == 1:
        print("wyszukwanie po imieniu")
    elif input_szukaj == 2:
        print("Wyszukiwanie po nazwisku")
    elif input_szukaj == 3:
        print("Wyszukiwanie po n telefonu")
elif input_user == 2:
    print("Podaj imię, nazwisko, nr telefonu")
elif input_user == 3:
    print("Które dane chcesz usunąć ")
elif input_user == 4:
    print("Które dane chcesz edytowac?")
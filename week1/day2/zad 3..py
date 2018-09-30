"""używając metody `.replace` https://docs.python.org/3.6/library/stdtypes.html#str.replace (oswajamy się z dokumentacją)
dla typów string zamienić wszystkie wszystkie występowania litery `s` na $ w dowolnym słowie (które posiada chociaż jedno s :))
dla bardziej ambitnych można pobierać słowo, literę do zamiany i znak do zamiany od usera (edited)"""

input_slowo = input("Podaj słowo : ")
input_litera = input("Podaj litere do zamiany: ")
input_znak = input("Podaj znak do zamiany: ")

print(input_slowo.replace(input_litera,input_znak))
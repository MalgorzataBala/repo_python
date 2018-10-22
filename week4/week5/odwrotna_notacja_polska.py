"""
Dla wszystkich symboli z wyrażenia ONP wykonuj:
jeśli i-ty symbol jest liczbą, to odłóż go na stos,
jeśli i-ty symbol jest operatorem to:
zdejmij ze stosu jeden element (ozn. a),
zdejmij ze stosu kolejny element (ozn. b),
odłóż na stos wartość b operator a.
jeśli i-ty symbol jest funkcją to:
zdejmij ze stosu oczekiwaną liczbę parametrów funkcji(ozn. a1...an)
odłóż na stos wynik funkcji dla parametrów a1...an
Zdejmij ze stosu wynik.

"""

wyrazenie = "2 3 + 5 *"
dl_wyraz = len(wyrazenie)
stos =[]
for i in wyrazenie:
    #37=47 operator
    #48-57 liczba
    if ord(i)>=37 and   ord(i)<=47:
        stos.append(i)
    if ord(i)>=48 and ord(i)<=57:
        pass

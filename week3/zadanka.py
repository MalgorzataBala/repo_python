#zad. 1 tworzymy liste i pozbywamy sie z niej duplikatów
input_usera=[1,2,3,1,4,1]
#input_usera=input("Podaj jakąś liste")
druga_lista=[]
for el_listy in input_usera:
    print(el_listy)
    if el_listy not in druga_lista:
        druga_lista.append(el_listy)



print(druga_lista)


#zad.2 sumator elementów listy
print("*********************")
print("*********************")

lista_suma = [1,2,3,4,5,6]
suma= 0
for i in lista_suma:
    suma = suma+i
    print(i)
print(suma)

print(sum(lista_suma))

#zad.3 max/min
print("*********************")
print("*********************")


lista_ext = [7,2,3,4,5,6]
min = lista_ext[0]
print(min)
#xx=len(lista_ext)
max = lista_ext[0]
for el_ext in lista_ext:
    print(el_ext)
    if min > el_ext:
        min = el_ext
    if max<el_ext:
        max = el_ext

print("min = " , min)
print("max = ", max)

"""
#importy
import math
import sys
from python_file import test
# from test.python_file import *  nie dziala

print(test.PI)      #importuje zmienna PI z pliku test z folderu python_file
print(sys.path)

print(test.PI2)
a=2
b=8
c=math.sqrt(b)
d=math.sqrt(a)

print(c)
"""
print("*********************")
print("*********************")


#sito erystotelesa - wyszukiwanie liczb pierwszych

nn = 10

tablica_nowa = []
#tworze tablice
for z in range(2, nn):
    tablica_nowa.append(z)

print(tablica_nowa)

# szukam wielokrotnsci liczb

for z in tablica_nowa:
    for j in range(2, nn):
        if (z * j) in tablica_nowa:
            tablica_nowa.remove(z * j)

print("Liczby pierwsze z zakresu : ",tablica_nowa)
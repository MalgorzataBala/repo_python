"""
 Rysujemy piramidę z gwiazdek za pomocą pętli.
 Jako input przyjmujemy wysokość pętli np. dla liczby 3 powinniśmy dostać coś takiego:
   *
  **
 ***

 ---*
 --**
 -***
"""
wysokosc = int(input("Podaj wysokosć piramidy: "))


liczba_spacji = wysokosc
liczba_gwiazdek  =1
for number in range(wysokosc):
    obraz_spacji = ""
    obraz_gwiazdek = ""
    for number in range(liczba_spacji):
        obraz_spacji = obraz_spacji+" "
    for number in range(liczba_gwiazdek):
        obraz_gwiazdek = obraz_gwiazdek + "*"
    print(obraz_spacji,obraz_gwiazdek)
    liczba_spacji = liczba_spacji - 1
    liczba_gwiazdek = liczba_gwiazdek+1

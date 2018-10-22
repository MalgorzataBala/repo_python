#trojkat pascala

import math
row =6
list_row=range(2,row+1)
lista_startowa =[1,1]
lista_do_zapamietania =[]
print("[1]")
print("[1, 1]")
for i in list_row:
    #print("lista startowa", lista_startowa)
    lista_do_zapamietania.append(1)
    d = len(lista_startowa)
    b = int(math.floor(d/2)+1)
    for j in range(b):
        k= int(lista_startowa[j])
        #print("k = ", k)
        if j>=b-1:
            break
        else:
            z=j+1
            l = lista_startowa[z]
            #print("l = ", l)
            m = k + l
            #print("m = ", m)
            lista_do_zapamietania.append(m)

    if d%2 != 0:
        lista_end = lista_do_zapamietania[::-1]
        lista_do_zapamietania = lista_do_zapamietania+lista_end
        print(lista_do_zapamietania)
    else:
        h = int(b)-1
        lista_koncowka = lista_do_zapamietania[0:h]
        lista_end_nieparz = lista_koncowka[::-1]
        lista_do_zapamietania = lista_do_zapamietania + lista_end_nieparz
        print(lista_do_zapamietania)
    lista_end=[]
    lista_end_nieparz=[]
    lista_koncowka=[]
    lista_startowa = lista_do_zapamietania
    lista_do_zapamietania = []




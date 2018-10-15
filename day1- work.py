
l = ["a"]
ll=["b"]
l.append(2)  #pozwala modyfikowac zawartosc listy, dorzuca na koniec listy
print(l)
l.extend(ll) #sumowanie dwóch list
print(l)
l.insert(2,"m") #indeks przed ktorym chcemy wlozyc inny argument
print(l)
l.remove("a") #usuwa pierwsze wystapeinie podanego elementu
print(l)
l.pop()  #usuwa ostatni element listy
print(l)
l.index("m")#podaje indeks podanego elementu, pierwszego
print(l)
l.reverse()
print(l)


lista = [[1,2,3],[4,5,6],[7,8,9]]
# print(lista([1][2]))   #nie dziala

print("******************************")
print("**********kopiowanie**********")
print("******************************")

a=[1]
a.append(2)
b=a.copy()
a=[[],[],[]]
b=a[:]
print(a)
print(b)
a.append(2)
print("b", b)
print("a", a)
a[0].append(1)
a[1].append(1)
a[2].append(1)
print("b", b)
print("a", a)
a.append("A")
print("b", b)
print("a", a)
a.append([4,5,6])
print("b", b)
print("a", a)
print(id(a))
print(id(b))
print(id(a[0]) ," = ", id(b[0]))
#b ma trzy elementy i jak dodajemy cokolwiek do a to sie doda, ale jak zmeiniamy elementy a to w b tez beda one zmienione, bo kopiujesz referencje,
#dlatego id(a[0])=id(b[0]) sa takie same
print("*****************************")
import copy
a=[[]]
b=copy.deepcopy(a)
print(id(a))
print(id(b))
a.append(1)
print("a",(a))
print("b",(b))
a[0].append([5,5,5])
print("a",(a))
print("b",(b))

#deepcopy kopiuje liste a pozniej jej nie zmienia, kopiujesz aktualna zawartosc, nie referencje
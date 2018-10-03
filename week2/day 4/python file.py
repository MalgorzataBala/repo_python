#***************************************
'''
number = 1
while number == 10:
    if number % 2 == 0:
        print(number)
        number = number + 1

print("koniec")

#Wyswietlanie liczb parzystych
for number in range(10):
    if number % 2 != 0 :
        continue
        print(number)
    else:
        print(number)
#***************************************
#***************************************

#sprawdzanie czy podane hasło jest poprawne, haslo musi byc dluzsze niz 6 znakow:


#import getpass
#haslo_szyfr= getpass.getpass("podaj haslo")


haslo = "haslo123"
input_user = input("Podaj hasło: ")
while len(input_user)<=6:

       print("Twoje hasło musi mieć więcej niż 6 znaków!")
    input_user = input("Podaj hasło: ")
    continue


print("the end")

#***************************************
#***************************************
'''

#zliczanie parzystych, nie parzystych liczb (0,100)

parz = 0
nieparz = 0
for number in range(100):
    if number%2==0:
        parz += 1
    else:
        nieparz +=1
a= "Parzyste {}, Nieparzyste {}".format(parz, nieparz)
b= f"Parzyste {parz}, Nieparzyste {nieparz}"
print(a)
print(b)


print("*************************")
#ciag Fibbonaciego dla 100
fib_one =0
fib_two =1

print(fib_one)
print(fib_two)
for number_fib in range(100):
    fib_three = fib_one + fib_two
    if fib_three < 100:
        fib_one=fib_two
        fib_two=fib_three
        print(fib_three)

    else:
        print ("koniec!")
        break



#silnia

print("*************************")
x = " "
silnia=1
number_silnia = 1

for number_silnia in range(4):

    silnia = silnia *(number_silnia+1)
    number_silnia += 1
    x= str(x) +"*"+ str(number_silnia)

print(x, "=",silnia)



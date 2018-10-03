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
        parz=parz+1
    else:
        nieparz=nieparz+1

print("parzystych: ",parz, "nieparzystych: ", nieparz)


print("*************************")
#ciag Fibbonaciego dla 100
fib_one =1
fib_two =1
for number_fib in range(10):
    fib_three =fib_one + fib_two
    fib_one=fib_two
    fib_two=fib_three
    print(fib_three)


#silnia

print("*************************")
silnia=1
number_silnia = 1
print(number_silnia)
for number_silnia in range(4):

    silnia = silnia *(number_silnia+1)
    number_silnia = number_silnia+1
    print("*", number_silnia)

print("=",silnia)
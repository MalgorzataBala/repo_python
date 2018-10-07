"""
Oblicz wiek psa z ludzkich lat w psich latach
- przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
- kolejne lata, psi rok to 4 ludzkie lata np. 15 ludzkich lat to 73 psie lata

"""

input_uesra = int(input("Ile lat ma Twój pies: "))
y_old= 0
for number in range(input_uesra):
    number=number+1
    if number ==1 or number==2:
        y_old = y_old + 10.5
    else:
        y_old = y_old + 4
y_old= round(y_old)
print("twój pies ma ", y_old, "psich lat")
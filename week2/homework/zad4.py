"""
 Program obliczajacy liczbe liter i cyfr w stringu. np. dla Tomek36 zwróci 2 liczby i 5 liter
"""
input_usera=input("Wpisz ciag znakow zawierajacy litery i cyfry: ")

len_str = int(len(input_usera))
count_str = 0
count_int = 0
other =0
for number in range(len_str):
    if input_usera[number].isalpha() == True :
        count_str = count_str + 1
    elif input_usera[number].isdigit() == True :
        count_int = count_int +1
    else:
        print("Miales wpisac ciag znakow zawierajacy litery i cyfry!")
        other = other+1
        continue
if other ==0:
    print("Liczb ", count_int, "\nCyfr", count_str)
else:
    print("Liczby: ", count_int, "\nCyfry: ", count_str, "\nInne znaki: ", other)
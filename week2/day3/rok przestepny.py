
#((rok mod 4 = 0) and (rok mod 100 <> 0)) or (rok mod 400 = 0)
input_year = int(input("Podaj rok do sprawdzenia: "))

if input_year%4==0  and  input_year %100 !=0 or input_year %400==0:

    print(input_year, "jest rokiem przestępnym.")
else:
    print(input_year, "nie jest rokiem przestepnym")
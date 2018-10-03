"""
Przelicznik C => F i C <= F a. C = (F - 32) * 5/9 b. F = C * (9/5) + 32
"""

input_data= input("Podaj temperature do przeliczenia :" )
input_data_value= input_data[0:len(input_data)-1]
if input_data_value.isdigit() == True :

    if input_data.endswith("C"):

        c_to_f = int(input_data_value)*(9/5) +32
        print(input_data,"=",round(c_to_f,2) ,"F")

    elif input_data.endswith("F"):
        f_to_c = (int(input_data_value) -32)*5/9
        print(input_data, "=", round(f_to_c,2), "C")


    else:
        print("Podaj temperaturę w stopniach Celcjusza lub Fahrenheita!")

else:
    print("Podaj poprawnie dane!")
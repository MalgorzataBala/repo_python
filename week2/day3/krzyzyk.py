#dodatkowo: dodac pusty znak, symulacja wpisywania stringa, parzysty ruch - kolko, nieparzysty - krzyzyk
gra = "xoooxxxoo"
ruch = 0

while ruch == 8:
    xxx = input("wpisz pierwszy znak")
    gra= xxx


    #0,4,8
    if gra[0]==gra[4]==gra[8]:
        print("wygral: " , gra[0])
    #012

    elif gra[0]==gra[1]==gra[2]:
        print("wygral: " , gra[0])

    elif gra[3] == gra[4]==gra[5]:
        print("wygral: " , gra[3])

    elif gra[6]==gra[7]==gra[8]:
        print("wygral: " , gra[6])

    elif  gra[2]==gra[4]==gra[6]:
        print("wygral: " , gra[2])

    elif  gra[0]==gra[3]==gra[6]:
        print("wygral: " , gra[0])

    elif  gra[1]==gra[4]==gra[7]:
        print("wygral: " , gra[1])

    elif gra[2] == gra[5] == gra[8]:
        print("wygral: " , gra[2])

    else:
        print("Rozgrywka przegrana!")

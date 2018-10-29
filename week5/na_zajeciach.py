"""import csv
#import pdb
#contekst manager
with open("dane.csv","r") as f:
    reader_object = csv.reader(f, delimiter=";")
    #pdb.set_trace()
    print("Naglowek")
    print(next(reader_object))
    print("Dane")
    for row in reader_object:
        print(row)

with open("dane.csv","a",newline="\n") as f:
    writer_object = csv.writer(f, delimiter=";")
    writer_object.writerow(["Marian", "Nowak", "Krakow", "Zielony Most 8"])
    for row in reader_object:
        print(row)
"""
#*********************************
#WYJĄTKI
#*********************************
import sys
l =[1,2,3]
try:
    print("Przed wyjatkiem")
    print(l[3])
    raise ValueError()
except (IndexError,) as error:
    print("ERROR: ",error)
    sys.exit(1)
except ValueError:
    print('value')
except:
    print('ogolne except')
finally:
    print("Po wyjatku")

print("Piszemy dalej")



#raise ValueError('Zla wartosc')
"""
 Program, który wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4.
"""

for number in  range(21):
    if number%4!=0:
        print(number)

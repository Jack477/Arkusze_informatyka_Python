
dane = ""

with open("liczby.txt", 'r') as plik:
    dane = plik.readlines()


suma = 0
for x in dane:
    if x.count("0") > x.count("1"):
        suma+=1
print(suma)



dane = ""
with open("pierwsze.txt", "r") as plik:
    dane = plik.read()
dane = dane.split()
liczby2 = []
liczby = []
def suma_cyferki(x):
    suma = 0
    for y in x:
        suma +=int(y)
    if len(str(suma))>1:
        tablicax = str(suma)
        suma_cyferki(str(tablicax))
    elif suma==1:
        return liczby.append(suma)


for x in dane:
    suma_cyferki(x)

print(sum(liczby))

for x in liczby2:
    print(x)


dane = ""
with open("galerie.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
dane2 = []
for x in dane[:-1]:
    a = x.split(" ")
    kraj = a[0]
    miasto = a[1]
    cyfry = []
    for y in a[2::]:
        cyfry.append(y)
    dane2.append((kraj, miasto, cyfry))
kraje = []
for x in dane2:
    if x[0] not in kraje:
        kraje.append(x[0])
for x in kraje:
    licznik = 0
    for y in dane2:
        if x == y[0]:
            licznik+=1
    print(x + " "+str(licznik))
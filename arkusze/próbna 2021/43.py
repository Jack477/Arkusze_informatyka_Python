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
        cyfry.append(int(y))
    buff = cyfry[0]
    lokale = []
    for y in range(1, len(cyfry), 2):
        if cyfry[y] != 0:
            lokale.append(cyfry[y]*cyfry[y-1])
            print(str(cyfry[y]) + " " + str(cyfry[y-1]))
        else:
            break
    dane2.append((kraj, miasto, lokale))

wynik = []
for x in dane2:
    powierzchnie = []
    for y in x[2]:
        if y not in powierzchnie:
            powierzchnie.append(y)
    wynik.append((x[1], len(powierzchnie)))
najmniejsza = wynik[0][1]
najwieksza = 0
for x in wynik:
    a = int(x[1])
    if a < najmniejsza:
        najmniejsza=a
    if a > najwieksza:
        najwieksza=a
for x in wynik:
    if x[1]==najwieksza:
        print(x[0]+" "+str(najwieksza))
    if x[1]==najmniejsza:
        print(x[0]+" "+str(najmniejsza))

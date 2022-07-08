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
najwieksza = 0
najmniejsza = 100000
wynik2 = [0, 0, 0, 0]
for x in dane2:
    powierzchnia = 0
    liczba_lokali = len(x[2])
    for y in x[2]:
        powierzchnia+=y
    if powierzchnia>najwieksza:
        najwieksza=powierzchnia
        wynik2[0]=najwieksza
        wynik2[1]=x[1]
    if powierzchnia<najmniejsza:
        najmniejsza=powierzchnia
        wynik2[2]=najmniejsza
        wynik2[3]=x[1]
    print(x[1]+" "+str(powierzchnia)+" "+str(liczba_lokali))
for x in wynik2:
    print(x)


dane = ""
with open("dane.txt", "r") as plik:
    dane = plik.readlines()

kontrastujace = 0
buffw = -1
buffk = -1
for x in range(340):
    for y in range(200):
        wiersz = dane[y].split()
        wiersz = [int(x) for x in wiersz]
        buffw=wiersz
        buffk=wiersz[x]
        if buffw==wiersz[x]:
            kontrastujace+=1




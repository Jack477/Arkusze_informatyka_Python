dane = ""
with open("dane.txt", "r") as plik:
    dane = plik.readlines()
dlugosc = 0
a = 0
for x in dane:
    wiersz = x.split()
    wiersz = (int(x) for x in wiersz)
    wiersz= list(wiersz)
    dlugoscx = []
    wyraz = -1
    for y in range(1, 320, 1):
        print(str(a)+" "+str(y))
        if wiersz[a] == wiersz[y]:
            dlugoscx.append(wiersz[y])
        a += 1
    a=0
    if len(dlugoscx)>dlugosc:
        dlugosc=len(dlugoscx)
print(dlugosc)
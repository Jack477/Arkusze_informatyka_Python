dane = ""
with open("pary.txt", "r") as plik:
    dane = plik.readlines()

slowa = []
for x in dane:
    a = x.split()
    slowa.append(a[1])

piwo = []
for x in slowa:
    buff = ""
    literki = ""
    wynik = ""
    for i in range(len(x)):
        y = x[i]
        literki+=y
        indeks = 0
        for z in x[i::]:
            if not z == y:
                buff=literki[0:-1]
                literki=""
                break
            if indeks==len(x[i::])-1:
                buff = literki
                literki = ""
                break
            literki+=z
            indeks+=1
        if len(buff)>len(wynik):
            wynik=buff
    piwo.append((wynik, len(wynik)))
for x in piwo:
    print(x)

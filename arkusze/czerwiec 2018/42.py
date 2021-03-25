dane = ""
with open("dane1.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
danea = []
for x in dane[:-1]:
    a = x.split()
    a=[int(x) for x in a]
    danea.append(a)

dane2 = ""
with open("dane2.txt", "r") as plik:
    dane2=plik.read()
dane2=dane2.split("\n")
daneb = []
for x in dane2[:-1]:
    a = x.split()
    a=[int(x) for x in a]
    daneb.append(a)
wynik = 0
for x in range(len(danea)):
    parz1 = 0
    nparz1 = 0
    parz2=0
    nparz2=0
    for y in danea[x]:
        if y%2==0:
            parz1+=1
        else:
            nparz1+=1
    for y in daneb[x]:
        if y % 2 == 0:
            parz2 += 1
        else:
            nparz2 += 1
    if parz1==5 and nparz1==5 and parz2 == 5 and nparz2==5:
        wynik+=1
print(wynik)

dane = ""
with open("dane1.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
danea=[]
for x in dane[:-1]:
    a = x.split()
    a = [int(x) for x in a]
    danea.append(a)
dane2= ""
with open("dane2.txt", "r") as plik:
    dane2=plik.read()
dane2=dane2.split("\n")
daneb=[]
for x in dane2[:-1]:
    a = x.split()
    a = [int(x) for x in a]
    daneb.append(a)
wynik = 0
for x in range(len(danea)):

    if danea[x][-1] == daneb[x][-1]:
        wynik+=1
print(wynik)
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
pary = 0
wyniki=[]
for x in range(len(danea)):
    tab1 = []
    tab2 = []
    for y in danea[x]:
        if y not in tab1:
            tab1.append(y)
    for y in daneb[x]:
        if y not in tab2:
            tab2.append(y)
    tab1=sorted(tab1)
    tab2=sorted(tab2)
    if tab1==tab2:
        pary+=1
        wyniki.append(x+1)
print(pary)
for x in wyniki:
    print(x)
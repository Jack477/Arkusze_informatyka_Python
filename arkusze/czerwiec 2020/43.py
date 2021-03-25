dane = ""
with open("pary.txt", "r") as plik:
    dane=plik.readlines()

pary = []
for x in dane:
    a = x.split()
    pary.append((a[0], a[1]))
pary2 = []
for x in pary:
    if len(x[1])==int(x[0]):
        pary2.append((int(x[0]), x[1]))
#pary2 = [int(x[0]) for x in pary2]
pary3 = []
for x in pary2:
    mniejsza = False
    for y in pary2:
        if x[0]<y[0]:
            mniejsza=True
        elif x[0] == y[0]:
            if str(sorted(x[1]))<str(sorted(y[1])):
                mniejsza=True

    if not list(x[1]) == sorted(x[1]):
        if mniejsza:
            pary3.append(x)
            #print(x)

najmniejsza = pary3[0]
for x in pary3:
    for y in pary3:
        if x[0] < y[0]:
             pass
        elif x[0] == y[0]:
            if str(sorted(x[1])) < str(sorted(y[1])):
                pass
        if najmniejsza[1]>y[1]:
            najmniejsza=x

print(najmniejsza)
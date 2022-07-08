dane = ""
with open("sygnaly.txt", "r") as plik:
    dane= plik.read()
dane = dane.split()
slowa = []
for x in dane:
    mmax = 0
    mmin = ord(x[0])
    for y in x:
        if ord(y)<mmin:
            mmin = ord(y)
        if ord(y)>mmax:
            mmax = ord(y)
    if mmax-mmin<=10:
        slowa.append(x)
for x in slowa:
    print(x)
dane = ""
with open("pary.txt", "r") as plik:
    dane = plik.readlines()
liczby = []
wyniki=[]
for x in dane:
    a = x.split()
    liczby.append(a[0])
liczby=[int(x) for x in liczby]

pierwsze = []
def genpierwsze():
    for x in range(2, 100):
        pierw = True
        for y in range(2, x):
            if x%y==0:
                pierw=False
                break
        if pierw:
            pierwsze.append(x)
genpierwsze()


for x in liczby:
    wyk = True
    if x>4 and x%2==0:
        for p1 in pierwsze:
            for p2 in pierwsze:
                if p1+p2==x:
                    if p1<p2:
                        wyniki.append((x, p1, p2))
                        wyk = False
                        break
                    else:
                        wyniki.append((x, p2, p1))
                        wyk = False
                        break
            if wyk==False:
                break

print(wyniki)
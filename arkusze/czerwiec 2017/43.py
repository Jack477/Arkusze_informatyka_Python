import math
def odlegosc(x1, x2, y1, y2):
    wynik = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
    return wynik
dane=""
with open("punkty.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
dane2=[]
for x in dane[:-1]:
    a = x.split(" ")
    dane2.append((int(a[0]), int(a[1])))
punkt1 = None
punkt2 = None
najodl = 0
for x in dane2:
    for y in dane2:
        odl=odlegosc(x[0], y[0], x[1], y[1])
        if odl>najodl:
            najodl=odl
            punkt1=x
            punkt2=y
print(punkt1)
print(punkt2)
print(int(najodl))



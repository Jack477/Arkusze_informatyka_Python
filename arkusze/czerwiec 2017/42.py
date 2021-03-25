dane = ""
with open("punkty.txt", "r") as plik:
    dane = plik.read()
dane = dane.split("\n")
dane2 = []
for x in dane[:-1]:
    a = x.split(" ")
    dane2.append((a[0], a[1]))

def cyfropodobne(x, y):
    znaki = ""
    for z in x:
        if z not in znaki:
            znaki += z
    znaki2 = ""
    for z in y:
        if z not in znaki2:
            znaki2+=z
    znaki = sorted(znaki)
    znaki2 = sorted(znaki2)
    if znaki == znaki2:
        return True
    else:
        return False

wynik = 0
for x in dane2:
    if cyfropodobne(x[0], x[1]) == True:
        wynik += 1
print(wynik)

def pierwsze(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()

dane = dane.split()
dane = [int(x) for x in dane]
dupa = []
for x in dane:
    if pierwsze(x) and x>=100 and x<=5000:
        dupa.append(x)

for x in dupa:
    print(x)
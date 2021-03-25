dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
    dane = dane.split()

systemy = []
for x in dane:
    systemy.append(x[-1])

ilosc= 0
for x in systemy:
    if int(x) == 8:
        ilosc+=1
print(ilosc)


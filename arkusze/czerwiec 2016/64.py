dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
    dane = dane.split()

suma=0
for x in dane:
    if x[-1]=="8":
        suma+=int(x[0:-1],8)
print(suma)
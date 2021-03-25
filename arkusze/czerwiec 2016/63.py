dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
    dane = dane.split()

ilosc = 0
for x in dane:
    if x[-1] == "2":
        xy = x[0:-1]
        if int(xy,2)%2==0:
            ilosc+=1
print(ilosc)
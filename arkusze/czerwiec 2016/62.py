dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
    dane = dane.split()

ilosc = 0
for x in dane:
    if x[-1] == "4":
        if "0" not in x:
            ilosc+=1
print(ilosc)

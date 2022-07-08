dane = ""
with open("sygnaly.txt", "r") as plik:
    dane=plik.readlines()
literki=""
for x in range(39, len(dane), 40):
    bufor=dane[x]
    literki+=bufor[9]
print(literki)
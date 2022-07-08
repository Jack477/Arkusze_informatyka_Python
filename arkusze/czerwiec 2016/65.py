dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
    dane = dane.split()
najwkod = None
najwwartosc=0
najmkod= None
buff = dane[0]
najmwartosc = int(buff[0:-1], int(buff[-1]))
for x in dane:
    system = x[-1]
    liczba = int(x[0:-1],int(system))
    if liczba>najwwartosc:
        najwwartosc=liczba
        najwkod=x
    if liczba<najmwartosc:
        najmwartosc=liczba
        najmkod=x
print(najwwartosc)
print(najwkod)
print(najmwartosc)
print(najmkod)
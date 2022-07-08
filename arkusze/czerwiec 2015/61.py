dane = ""
with open("kody.txt", "r") as plik:
    dane=plik.read()
dane = dane.split()
wynik = []
for x in dane:
    a = x[::-1]
    sumap = 0
    sumanp = 0
    for i in range(len(a)):
        if i%2==0:
            sumap+=int(a[i])
        else:
            sumanp+=int(a[i])
    sumap=sumap*3
    wynik.append((sumap, sumanp))
tekst = ""
for x in wynik:
    tekst+=str(x[0])+" "+str(x[1])+"\n"
with open("kody1.txt", "w") as plik:
    plik.write(tekst)


dane = ""
with open("kody.txt", "r") as plik:
    dane=plik.read()
dane = dane.split()
kodowanie = ""
with open("cyfra_kodkreskowy.txt", "r") as plik:
    kodowanie=plik.read()
kodowanie=kodowanie.split("\n")
kody = []
for x in range(1, len(kodowanie)-1):
    linia = str(kodowanie[x])
    a=linia
    a=a.split()
    kody.append((a[0], a[1]))

wyniki = ""
for x in dane:
    kodcyferki = "11011010"
    for y in x:
        for z in kody:
            if y==z[0]:
                kodcyferki+=z[1]
    a = x[::-1]
    sumakontrolna = 0
    sumap = 0
    sumanp = 0
    for i in range(len(a)):
        if i%2==0:
            sumap+=int(a[i])
        else:
            sumanp+=int(a[i])
    sumap=sumap*3
    sumakontrolna=sumap+sumanp
    sumakontrolna=sumakontrolna%10
    sumakontrolna=10-sumakontrolna
    kod=sumakontrolna%10
    cyfra_kontrolna = ""
    for y in kody:
        if int(y[0])==kod:
            cyfra_kontrolna=y[1]
    kodcyferki+=cyfra_kontrolna+"11010110"
    wyniki+=kodcyferki+"\n"
with open("kody3.txt", "w") as plik:
    plik.write(wyniki)
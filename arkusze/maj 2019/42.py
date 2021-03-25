dane = ""
with open("liczby.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
for x in dane[:-1]:
    silnia = 0
    for y in x:
        liczby = []
        y=int(y)
        if y == 0:
            silnia+=1
            continue
        for j in range(1, y+1):
            liczby.append(j)
        buff = liczby[0]
        for j in liczby[1:]:
            buff*=j
        silnia+=buff
    if  silnia == int(x):
        print(silnia)




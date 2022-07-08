dane = ""
with open("punkty.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
dane2= []
def pierwsze(liczba):
    if liczba == 1:
        return False
    else:
        for i in range(2, liczba-1):
            if liczba%i==0:
                return False
    return True
for x in dane[:-1]:
    a=x.split(" ")
    dane2.append((a[0], a[1]))
wynik=0
for x in dane2:
    a = pierwsze(int(x[0]))
    b = pierwsze(int(x[1]))
    if a == True and b == True:
        wynik+=1
        print(x)
print(wynik)
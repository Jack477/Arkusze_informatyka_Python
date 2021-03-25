def pierwsze(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True


dane =""
with open("pierwsze.txt", "r") as plik:
    dane = plik.read()
dane=dane.split()
liczby=[]
for x in dane:
    x = x[::-1]
    if pierwsze(int(x)):
        liczby.append(str(x[::-1]))
for x in liczby:
    print(x)
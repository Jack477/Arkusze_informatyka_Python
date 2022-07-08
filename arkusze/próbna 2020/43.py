dane = ""
with open("dane4.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
luki = []
element = int(dane[0])
for x in range(1, len(dane)-1):
    buff = int(dane[x])
    luka = abs(element-buff)
    element=buff
    luki.append(luka)
powtorzenia = []

for x in luki:
    wartosc = str(x)+" "+str(luki.count(x))
    if wartosc not in powtorzenia:
        powtorzenia.append(wartosc)
naj = 0
wynik = ""
najczestsze_luki = []
for x in powtorzenia:
    print(x)
    y = x.split(" ")
    if int(y[1])>1:
        najczestsze_luki.append(y)
    if naj<int(y[1]):
        naj=int(y[1])
        wynik=y
print("najczesciej wystepujacy element to: "+str(wynik))
print(najczestsze_luki)
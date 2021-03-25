dane=""
with open("dane_6_3.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
dane2=[]
for x in dane[:-1]:
    a=x.split(" ")
    dane2.append((a[0], a[1]))

def szyfr_cezara(klucz, slowo):
    buff = ""
    y = klucz % 26
    y=-y
    for x in slowo:
        if ord(x)+y<65:
            a = ord(x)-65
            buff+=chr(91+a+y)
        else:
            buff+=chr(ord(x)+y)
    return buff

for x in dane2:
    klucz=0
    a = x[0][0]
    for y in range(26):
        if a==x[1][0]:
            klucz=y
            break
        else:
            a=chr(ord(a)+1)
        if ord(a)>90:
            a=chr(65)
    odszyfr = szyfr_cezara(klucz,x[1])
    if x[0]!=odszyfr:
        print(x)

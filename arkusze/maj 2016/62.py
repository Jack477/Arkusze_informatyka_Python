dane = ""
with open("dane_6_2.txt", "r") as plik:
    dane=plik.readlines()
dane2=[]
for x in dane:
    a=x.split(" ")
    dane2.append((a[0], a[1][:-1]))


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
    slowo = x[0]
    klucz = x[1]
    if klucz=='':
        klucz='0'
    print(szyfr_cezara(int(klucz), slowo))
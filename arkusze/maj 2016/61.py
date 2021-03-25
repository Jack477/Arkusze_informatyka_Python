dane=""
with open("dane_6_1.txt", "r") as plik:
    dane=plik.read()

dane=dane.split()

def szyfr_cezara(klucz, slowo):
    buff = ""
    y = klucz % 26
    for x in slowo:
        if ord(x)+klucz>90:
            a = 90-ord(x)
            buff+=chr(90-a)
        else:
            buff+=chr(ord(x)+klucz)
    return buff

print(szyfr_cezara(107,"DUPA"))



wynik=""
for x in dane:
    print(szyfr_cezara(107, x))
    wynik+=szyfr_cezara(107, x)+"\n"
with open("wyniki_6_1.txt", "w") as plik:
    plik.write(wynik)

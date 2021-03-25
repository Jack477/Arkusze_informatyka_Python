dane = ""
with open("przyklad.txt", "r") as plik:
    dane = plik.read()
dane=dane.split("\n")

def nwd(a, b):
    while(a!=b):
        if a>b:
            a-=b
        else:
            b-=a
    return a

dlugosc = 0
dlugosci = []
wynik = []
p_para = nwd(int(dane[0]), int(dane[1]))
element = int(dane[1])
for x in dane[2:-1]:
    if p_para == nwd(element, int(x)):
        dlugosc+=1
    else:
        dlugosci.append(dlugosc)
        dlugosc=0
    element=int(x)
print(dlugosci)



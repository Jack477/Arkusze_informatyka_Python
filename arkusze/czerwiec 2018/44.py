dane = ""
with open("przyklad1.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
danea = []
for x in dane[:-1]:
    a = x.split()
    a=[int(x) for x in a]
    danea.append(a)

dane2 = ""
with open("przyklad2.txt", "r") as plik:
    dane2=plik.read()
dane2=dane2.split("\n")
daneb = []
for x in dane2[:-1]:
    a = x.split()
    a=[int(x) for x in a]
    daneb.append(a)

def glupio(ciag1, ciag2):
    x = ciag1+ciag2
    x = sorted(x)
    print(x)


for x in range(len(danea)):
    a = danea[x]
    b = daneb[x]
    glupio(a, b)

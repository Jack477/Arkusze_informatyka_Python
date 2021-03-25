dane = ""
with open("dane.txt","r") as plik:
    dane = plik.readlines()
maxx= []
minn = []

for x in dane:
    dane2 = x.split()
    dane2 = [int(x) for x in dane2]
    a = max(dane2)
    b = min(dane2)
    maxx.append(int(a))
    minn.append(int(b))
print(min(minn))
print(max(maxx))

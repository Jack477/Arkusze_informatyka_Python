dane = ""
with open("dane.txt", "r") as plik:
    dane = plik.readlines()
buff = 0
z = 0
for x in dane:
    dane2 = x.split()
    dane2 = [int(x) for x in dane2]
    for y in range(0, 160, 1):
        if dane2[y]!=dane2[320-y-1]:
            buff+=1
            break

print(buff)
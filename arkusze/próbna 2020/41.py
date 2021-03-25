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
print(min(luki))
print(max(luki))
#for x in luki:
#    print(x)
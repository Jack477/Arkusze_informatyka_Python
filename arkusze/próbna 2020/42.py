dane = ""
with open("dane4.txt", "r") as plik:
    dane = plik.read()
dane=dane.split("\n")

roznica = 0
element = int(dane[0])
ciagi = []
ciagi.append('0')
buff_ciag = []
for x in range(1, len(dane)-1):
    buff = int(dane[x])
    if abs(element-buff)!=roznica:
        roznica=abs(element-buff)
        if len(ciagi[0])<len(buff_ciag):
            ciagi.append(buff_ciag)
            print("ciag jest dluzszy")
            buff_ciag = []
            buff_ciag.append(element)
            buff_ciag.append(buff)
    else:
        buff_ciag.append(buff)
    element=buff
dlugosc = 0
najdluzszy_ciag = []
for x in ciagi:
    if len(x)>dlugosc:
        dlugosc=len(x)
        najdluzszy_ciag=x
print(dlugosc)
print(najdluzszy_ciag)
print(najdluzszy_ciag[0])
print(najdluzszy_ciag[-1])


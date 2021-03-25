dane = ""
with open("sygnaly.txt", "r") as plik:
    dane = plik.readlines()

slowa = []
najliter = 0
for x in dane:
    bufor = []
    for y in x:
        if(y not in bufor):
            bufor.append(y)
    if najliter < len(bufor):
        najliter=len(bufor)
        slowa.insert(0,x)
        print(bufor)
print(najliter-1)
print(slowa[0])
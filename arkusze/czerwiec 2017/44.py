import math
dane=""
with open("punkty.txt", "r") as plik:
    dane=plik.read()
dane=dane.split("\n")
dane2=[]
for x in dane[:-1]:
    a = x.split(" ")
    dane2.append((int(a[0]), int(a[1])))
wew=0
bok=0
zew=0
for x in dane2:
    if x[0]<5000 and x[1]<5000:
        wew+=1
    elif x[0]==5000 and x[1]<=5000 or x[0]<=5000 and x[1]==5000:
        bok+=1
    elif x[0]>5000 or x[1]>5000:
        zew+=1
print(wew)
print(bok)
print(zew)

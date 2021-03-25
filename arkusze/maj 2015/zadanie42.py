dane = ""
with open("liczby.txt", "r") as plik:
    dane = plik.readlines()

liczby = []
for x in dane:
    liczby.append(int(x, 2))

przez2 = 0
przez8 = 0
for x in liczby:
    if x % 2 == 0:
        przez2+=1
    if x % 8 == 0:
        przez8+=1
print(przez2)
print(przez8)
dane = ""
with open("liczby.txt", 'r') as plik:
    dane = plik.readlines()

tab = [int(x,2) for x in dane]
maks = max(tab)
minimum = min(tab)
print(tab.index(maks)+1)
print(tab.index(minimum)+1)


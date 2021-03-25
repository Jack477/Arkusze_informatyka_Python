dane = ""
with open("DANE_PR2\liczby.txt") as f:
	dane = f.readlines()

powers = [3**i for i in range(0, 11)]
am = 0
for line in dane:
	line = line.strip()
	if int(line) in powers:
		am += 1

print("4.1.", am)
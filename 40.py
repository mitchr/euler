champ = ""
for i in range(1000000):
	champ += str(i)

print(int(champ[1]) * int(champ[10]) * int(champ[100]) * int(champ[1000]) * int(champ[10000]) * int(champ[100000]) * int(champ[1000000]))
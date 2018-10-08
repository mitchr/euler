def isPandigital(n):
	s = [int(i) for i in str(n)]
	return sorted(s) == [0,1,2,3,4,5,6,7,8,9]

sum = 0
for d in range(1023456789, 9876543210):
	if isPandigital(d) == False:
		continue

	print(d)

	s = str(d)
	if int(s[1:4]) % 2 == 0:
		if int(s[2:5]) % 3 == 0:
			if int(s[3:6]) % 5 == 0:
				if int(s[4:7]) % 7 == 0:
					if int(s[5:8]) % 11 == 0:
						if int(s[6:9]) % 13 == 0:
							if int(s[7:10]) % 17 == 0:
								print(d)
								sum += d

print(sum)

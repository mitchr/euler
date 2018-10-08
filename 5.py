def doesDivideByAll(n, divisors):
	for d in divisors:
		if i % d != 0:
			return False
	return True

# if n is divisible by 9, n is divisble by 3
divisors = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

i = 1
while True:
	if doesDivideByAll(i, divisors) == False:
		i += 1
	else:
		print(i)
		break

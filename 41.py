# this is another one that just runs forever
# how to prove?

import math

def isPandigital(n):
	template = []
	for i in range(len(str(n))):
		template.append(i+1)

	s = [int(i) for i in str(n)]
	return sorted(s) == template

def isPrime(p):
	if p > 1:
		for i in range(2, int(math.sqrt(p))+1):
			if p % i == 0:
				return False
		return True


max = 0
while True:
	if isPandigital(i) and isPrime(i):
		if i > max:
			max = i
		print(i)
	i += 1

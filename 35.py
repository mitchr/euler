import math

def rotateRight(s):
	return s[-1] + s[:-1]

def isPrime(p):
	if p > 1:
		for i in range(2, int(math.sqrt(p))+1):
			if p % i == 0:
				return False
		return True

def isCircularPrime(p):
	s = str(p)
	for i in range(len(s)):
		s = rotateRight(s)
		if isPrime(int(s)) == False:
			return False
	return True

count = [] 
for i in range(1, 1000000):
	if isPrime(i) == False:
		continue
	if isCircularPrime(i):
		count.append(i)

print(count)

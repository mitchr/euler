import math

def factorize(n):
	primes = []

	while n % 2 == 0:
		primes.append(2)
		n = n / 2

	for i in range(3, int(math.sqrt(n))+1, 2):
		while n % i== 0:
			primes.append(int(i))
			n = n / i

	if n > 2:
		primes.append(int(n))

	return primes


def uniqueElementCount(a):
	count = 0
	for i in range(0, len(a)):
		foundAlready = False
		for j in range(0, i):
			if a[i] == a[j]:
				foundAlready = True
				break
		if foundAlready == False:
			count += 1
	return count

i = 2
while True:
	c1 = uniqueElementCount(factorize(i))
	if c1 != 4:
		i += 1
		continue
	c2 = uniqueElementCount(factorize(i+1))
	c3 = uniqueElementCount(factorize(i+2))
	c4 = uniqueElementCount(factorize(i+3))
	if c1==c2==c3==c4==4:
		print(i)
		break
	i += 1

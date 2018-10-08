# github.com/mitchr/fraction

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

def countElementInArray(n, arr):
	count = 0
	for x in arr:
		if x == n:
			count += 1
	return count

def repetend(denominator):
	factors = factorize(denominator)

	c = 1
	for f in factors:
		if f is not 2 and f is not 5:
			c *= f

	if c == 1:
		return max([countElementInArray(2, factors), countElementInArray(5, factors)])


	n = 1
	while True:
		if ((10**n)-1) % c == 0:
			return n
		n += 1


d = 2
longestCycle = 1
longestD = 1

while d < 1000:
	r = repetend(d)
	if r > longestCycle:
		longestCycle = r
		longestD = d
	d += 1

print(longestD)
print(longestCycle)

import math

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

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

def divisors(n):
	divisors = []

	for i in range(1, n+1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def isPrime(p):
	if p > 1:
		for i in range(2, int(math.sqrt(p))+1):
			if p % i == 0:
				return False
		return True

def totient(n):
	sum = 0
	for i in range(1, n+1):
		if gcd(n,i)==1:
			sum+=1
	return sum

def g2(n):
	sum = 0
	for d in divisors(n):
		sum += totient(d)/d
	return sum*n

def g(n):
	if isPrime(n):
		return (2*n)-1

	# product = 1
	# primes = factorize(n)
	# for p in primes:
	# 	product *= g(p)
	# return product
	sum = 0
	for i in range(1, n+1):
		sum += gcd(i, n)
	return sum

def G(n):
	sum = 0
	for j in range(1, n+1):
		sum += g2(j)
	return sum

# print(g2(30))
# print(g(30))
# print(g(3)*g(5)*g(2))
# print(g(1)+g(2)+g(3)+g(4)+g(5)+g(6)+g(7)+g(8)+g(9)+g(10))
# print(G(10))
print(G(10**11) % 998244353)
import math

def divisors(n):
	d = []
	for i in range(1, int(math.sqrt(n))):
		if n % i == 0:
			if n / i == i:
				d.append(i)
			else:
				d.append(i)
				d.append(int(n/i))
	return d

def d(n):
	return sum(divisors(n))-n

amicables = []
for a in range(220, 10000):
	b = d(a)
	if a == d(b) and (a != b):
		if a in amicables or b in amicables:
			continue
		amicables.append(a)
		amicables.append(b)

print(sum(amicables))

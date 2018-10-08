import math

def triangle(n):
	return (n*(n+1))//2

# https://www.quora.com/What-is-an-efficient-algorithm-to-find-divisors-of-any-number
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

i = 1
while True:
	t = triangle(i)
	if len(divisors(t)) > 500:
		print(t)
		break
	i += 1

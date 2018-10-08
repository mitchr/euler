def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)

n = factorial(100)
k = str(n)

sum = 0
for d in k:
	sum += int(d)

print(sum)

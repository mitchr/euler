def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	return fib(n-1) + fib(n-2)

sum = 0
i = 1
while True:
	n = fib(i)
	if n >= 4000000:
		break
	if n % 2 == 0:
		sum += n
	i += 1

print(sum)

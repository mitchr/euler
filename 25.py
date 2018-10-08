def fib(n):
	f1 = 1
	f2 = 1
	tmp = 0
	for i in range(1, n):
		tmp = f1 + f2
		f1 = f2
		f2 = tmp
	return f1

i = 1
while True:
	if len(str(fib(i))) >= 1000:
		print(i)
		break
	i += 1
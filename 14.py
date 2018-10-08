def collatz(n):
	if n%2 == 0:
		return n/2
	return 3*n+1

def chainLength(n):
	s = 0
	length = 1
	while n != 1:
		n = collatz(n)
		length += 1
	return length

startingNumber = 0
max = 0
for i in range(13, 999999):
	k = chainLength(i)
	if k > max:
		startingNumber = i
		max = k

print(startingNumber, max)

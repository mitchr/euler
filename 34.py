# runs forver, but does find the correct 2 numbers
# how to prove that there are only 2 such numbers?

def fac(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return n*fac(n-1)

i = 3
while True:
	sum = 0
	for j in str(i):
		sum += fac(int(j))
	if sum == i:
		print(i)
	i += 1

import math

def T(n):
	return n*(n+1)/2

def isPentagonal(x):
	if x <= 0:
		return False
	return (math.sqrt(24*x+1) + 1) % 6 == 0

def isHexagonal(x):
	return (math.sqrt(8*x+1)+1) % 4 == 0

i = 286
while True:
	t = T(i)
	if isPentagonal(t) and isHexagonal(t):
		print(t)
		break
	i += 1

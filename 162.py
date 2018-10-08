def fac(n):
	if n == 0:
		return 1
	return n*fac(n-1)

def choose(n, k):
	return fac(n)/(fac(k)*fac(n-k))

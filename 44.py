import math

def P(n):
	return n*(3*n-1)/2

# courtesy of wikipedia
def isPentagonal(x):
	if x <= 0:
		return False
	return (math.sqrt(24*x+1) + 1) % 6 == 0

D = None
for j in range(1, 10000):
	for k in range(1, 10000):
		Pk = P(k)
		Pj = P(j)
		if isPentagonal(Pj+Pk) and isPentagonal(Pj-Pk):
			result = Pk-Pj
			if D == None:
				D = result
			if result < D:
				D = result

print(D)

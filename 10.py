import math

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
def sieve(n):
	if n <= 1:
		return None

	A = [True]*n
	A[0] = False
	A[1] = False

	for i in range(2, int(math.sqrt(n))+1):
		if A[i] == True:
			for j in range(i*i, n, i):
				A[j] = False
	return A

p = sieve(2000000)
sum = 0
for i in range(0, len(p)):
	if p[i]:
		sum += i
print(sum)

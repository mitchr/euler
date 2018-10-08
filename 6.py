def sumOfSquares(n):
	sum = 0
	for i in range(1, n+1):
		sum += i*i
	return sum

def squareOfSums(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum*sum

print(squareOfSums(100) - sumOfSquares(100))

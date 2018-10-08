def isPalindrome(x):
	return x == x[::-1]

max = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		n = i*j
		if isPalindrome(str(n)):
			if n > max:
				max = n
print(max)

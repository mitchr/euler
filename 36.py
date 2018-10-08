def isPalindrome(x):
	return x == x[::-1]

sum = 0
for i in range(1, 1000000):
	if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
		sum += i

print(sum)

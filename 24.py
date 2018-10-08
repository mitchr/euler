x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
def permute(a):
	k = None
	for i in range(0, len(a)):
		# check for going outside list bounds
		if i+1 >= len(a):
			break
		if a[i] < a[i+1]:
			k = i
	if k == None:
		return a

	l = None
	for i in range(k, len(a)):
		if a[k] < a[i]:
			l = i

	temp = a[k]
	a[k] = a[l]
	a[l] = temp

	nextP = []
	for i in range(k+1):
		nextP.append(a[i])

	for i in list(reversed(a[k+1:len(a)])):
		nextP.append(i)
	return nextP

i = 1
while i <= 1000000-1:
	x = permute(x)
	i += 1

print(x)

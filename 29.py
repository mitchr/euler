def uniqueElementCount(a):
	count = 0
	for i in range(0, len(a)):
		foundAlready = False
		for j in range(0, i):
			if a[i] == a[j]:
				foundAlready = True
				break
		if foundAlready == False:
			count += 1
	return count

terms = []
for a in range(2, 101):
	for b in range(2, 101):
		terms.append(a**b)

print(uniqueElementCount(terms))

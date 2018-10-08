alphaMap = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

f = open("p022_names.txt", "r")
words = f.read().split(",")
for i in range(0, len(words)):
	words[i] = words[i].strip("\"")

words = sorted(words)

sum = 0
for i in range(0, len(words)):
	wordSum = 0
	for k in words[i]:
		wordSum += alphaMap[k]
	sum += (i+1)*wordSum

print(sum)

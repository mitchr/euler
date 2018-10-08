import math

alphaMap = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

# http://www.wolframalpha.com/input/?i=solve+for+n:+m+%3D+n*(n%2B1)%2F2
def isTriangle(n):
	return (math.sqrt(8*n+1)-1) % 2 == 0

def wordSum(s):
	sum = 0
	for k in s:
		if k == "\"":
			continue
		sum += alphaMap[k]
	return sum

f = open("p042_words.txt", "r")
words = f.read().split(",")

sum = 0
for k in words:
	if isTriangle(wordSum(k)):
		sum += 1

print(sum)

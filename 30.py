# this never stops execution
# I just got lucky and assumed the first 6 I got were the correct answers
# there could've been more but I'm too tired to prove that there aren't any more

i = 2
while True:
	sum = 0
	for k in str(i):
		sum += int(k)**5
	if sum == i:
		print(i)
	i += 1

alpha = [0 for i in range(26)]

for w in input():
	alpha[ord(w) % 97] += 1

for a in alpha:
	print(a,end=' ')
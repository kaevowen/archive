from random import randrange

n=5#int(input())
m1=[randrange(0, 2^n-1) for _ in range(n)]
m2=[randrange(0, 2^n-1) for _ in range(n)]
d = []

print(m1, m2)

for i in range(len(m1)):
	k = "{0:05b}".format(m1[i]|m2[i]).replace('b','') \
	.replace('1','#').replace('0',' ')
	d.append(k)

print(d)
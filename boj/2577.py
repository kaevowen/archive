import sys
l = [0 for i in range(10)]
a = [0, 0, 0]
a[0] = int(input())
a[1] = int(input())
a[2] = int(input())
for i in str(a[0]*a[1]*a[2]):
	l[int(i)]+=1
for i in l:
	print(i)

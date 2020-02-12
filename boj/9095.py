n = int(input())
l = []
int_list = [1,2,4]

for i in range(4, 11):
	int_list.append(sum(int_list[-3:]))

for i in range(n):
	l.append(int(input()))

for i in range(n):
	print(int_list[l[i] - 1])
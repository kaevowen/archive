arr = [i for i in range(1, 10001)]

def s(n):
	total = n
	while 1:
		if n==0:
			break
		total+=n%10
		n=n//10

	return total


for i in range(1,10000):
	idx = s(i)

	if idx < 10000:
		arr[idx] = True

for i in range(1, 10000):
	if arr[i] != True:
		print(i)
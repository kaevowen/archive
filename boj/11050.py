def choose(n, k):
	if n == k or k == 0:
		return 1

	return choose(n-1, k-1) + choose(n-1, k)

n, k = map(int, input().split(' '))
print(choose(n, k))
def fib(n):
	if n in memo:
		return memo[n]

	r = fib(n-1) + fib(n-2)
	memo[n] = r
	return r

memo = {0:1, 1:1}

print(fib(12))

print(memo)

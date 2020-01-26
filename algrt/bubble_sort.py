def bubble_sort(n, k):
    for i in range(k):
        for j in range(k-i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

if __name__ == '__main__':
	from random import sample
	from timeit import Timer
	a = [i for i in range(1,10000)]
	a = sample(a,9999)
	t = Timer(lambda: bubble_sort(a, len(a)-1))
	print(t.timeit(number=1))
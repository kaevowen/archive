import random
import timeit
import sys

def counting_sort(values, k):
    #make list using a length
    b = [-1] * len(values)
    #make list using a's max value
    count = [0] * (k+1)
    #count numbers
    for i in values:
        count[i] += 1

    for i in range(k):
        count[i+1] += count[i]

    for i in reversed(range(len(values))):
        b[count[values[i]] - 1] = values[i]
        count[values[i]] -= 1

    return b
'''
a = [i for i in range(1,10000)]
a = random.sample(a, 9999)

t = timeit.Timer(lambda:counting_sort(a,max(a)))
print(t.timeit(number=1))
'''

n = int(sys.stdin.readline())
k = []
for i in range(n):
    k.append(int(sys.stdin.readline().rstrip()))

for i in counting_sort(k, max(k)):
    print(i)
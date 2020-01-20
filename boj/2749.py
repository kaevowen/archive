import sys

fib = [0, 1]
mod = 1000000
p = int(mod/10*15)

def pisano(n):
    for i in range(2, p):
        fib.append(fib[i-1] + fib[i-2])
        fib[i] %= mod

    return fib[n%p]

n = int(sys.stdin.readline())
print(pisano(n))
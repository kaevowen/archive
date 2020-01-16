import sys

n = int(sys.stdin.readline())
s = 0
for _ in range(n):
	a = sys.stdin.readline()
	s += int(a)
print(s-(n-1))
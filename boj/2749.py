import sys

head = 0
mid = 0
rear = 1

n = int(sys.stdin.readline())

for i in range(n):
    mid = head+rear
    head = rear
    rear = mid

print(head%1000000)
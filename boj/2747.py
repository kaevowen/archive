head = 0
mid = 0
rear = 1

n = int(input())

for i in range(n):
    mid = head+rear
    head = rear
    rear = mid

    fib = head

print(head)
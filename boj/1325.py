import sys
from collections import deque

def BFS(v):
    q = deque()
    visited = [False] * (n+1)
    q.append(v)
    visited[v] = True
    cnt = 1

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not (visited[e]):
                q.append(e)
                visited[e] = True
                cnt += 1
    return cnt

n, M = map(int, sys.stdin.readline().split())
adj = [[] for i in range(n+1)]
max_num = []
m = -1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)

for i in range(1, n+1):
    c = BFS(i)

    if c == m:
        max_num.append(i)
        m = c
    elif c > m:
        max_num = [i]
        m = c

for e in max_num:
    print(e, end = ' ')
print()
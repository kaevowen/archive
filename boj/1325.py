def DFS(v):
    visited[v] = True
    print(v, ' ',end='')
    for w in adj_list[v]:
        if not visited[w]:
            DFS(w)

'''
N, M = map(int, input().split())
graph_list = [set([]) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    graph_list[i].add(j)
    graph_list[j].add(i)

print(graph_list)
for i in range(1, M+1):
    for j in list(DFS(graph_list, i)):
        print(j, end=' ')
    print()
'''

adj_list = [[],[3],[3],[4,5],[],[]]
N = len(adj_list)
visited = [False for _ in range(N)]

for j in range(1, N):
    if not visited[j]:
        DFS(j)


def BFS(graph, root):
	visited = []
	q = [root]

	while q:
		vertex = q.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			q+=sorted(list(graph[vertex] - set(visited)))

	return visited


def DFS(graph, root):
	visited = []
	stack = [root]

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			stack += list(graph[node] - set(visited))
	return visited

adj_set = {
	1:set([5,4]),
	2:set([3,1]),
	3:set([3,2]),
	4:set([4,3]),
	5:set([5,3]),
}

for i in list(DFS(adj_set, 1)):
	print(i)
'''
N, M, V = map(int, input().split())
graph_list = [set([]) for _ in range(N+1)]
for _ in range(M):
	i, j = map(int,input().split())
	graph_list[i].add(j)
	graph_list[j].add(i)


for i in list(DFS(graph_list, V)):
	print(i, end=' ')
print()

for j in list(BFS(graph_list, V)):
	print(j, end=' ')	
'''
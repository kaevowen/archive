def BFS(graph, root):
	visited = []
	q = [root]

	while q:
		vertex = q.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			q+=sorted(list(graph_list[vertex] - set(visited)))

	return visited


def DFS(graph, root):
	visited = []
	stack = [root]

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			stack += sorted(list(graph_list[node] - set(visited))
				, reverse = True)
	return visited

def DFS_recursive(graph, start, end, visited=[]):
	visited = visited + [start]

	if start == end:
		paths.append(visited)

	for node in graph[start]:
		if node not in visited:
			DFS(graph, node, end, visited)
	
	return visited

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
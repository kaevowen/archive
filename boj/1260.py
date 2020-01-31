def BFS(graph, root):
	visited = []
	q = [root]

	while q:
		vertex = q.pop(0)
		if vertex not in visited:
			visited.append(vertex)
<<<<<<< HEAD
			q+=sorted(list(graph_list[vertex] - set(visited)))

	return visited

=======
			q+=sorted(list(graph[vertex] - set(visited)))

	return visited


>>>>>>> 492e57d7f7d40660fd323f3d7521924eb71627c9
def DFS(graph, root):
	visited = []
	stack = [root]

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
<<<<<<< HEAD
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

#N = 정점의 개수
#M = 간선의 개수
#V = 인덱스(시작) 번호
=======
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
>>>>>>> 492e57d7f7d40660fd323f3d7521924eb71627c9
N, M, V = map(int, input().split())
graph_list = [set([]) for _ in range(N+1)]
for _ in range(M):
	i, j = map(int,input().split())
	graph_list[i].add(j)
	graph_list[j].add(i)

<<<<<<< HEAD
print(graph_list)
=======
>>>>>>> 492e57d7f7d40660fd323f3d7521924eb71627c9

for i in list(DFS(graph_list, V)):
	print(i, end=' ')
print()

for j in list(BFS(graph_list, V)):
<<<<<<< HEAD
	print(j, end=' ')	
=======
	print(j, end=' ')	
'''
>>>>>>> 492e57d7f7d40660fd323f3d7521924eb71627c9

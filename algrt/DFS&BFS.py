def BFS(graph, root):
	visited = []
	q = [root]

	while q:
		vertex = q.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			#print(visited)

			for node in graph[vertex]:
				if node not in visited:
					q.append(node)

	return visited

def DFS(graph, start, end, visited=[]):
	visited = visited + [start]

	if start == end:
		paths.append(visited)

	for node in graph[start]:
		if node not in visited:
			DFS(graph, node, end, visited)
	
	return visited


#test case
korea = {'세종': set(['서울', '강릉', '대구', '광주']),
         '서울': set(['평양', '인천', '세종']),
         '강릉': set(['독도', '세종']),
         '광주': set(['세종', '여수']),
         '대구': set(['세종', '울산']),
         '평양': set(['서울', ]),
         '인천': set(['서울', ]),
         '독도': set(['강릉', ]),
         '여수': set(['광주', '부산']),
         '울산': set(['대구', '부산']),
         '부산': set(['여수', '울산']),
         }

print(BFS(korea, '세종'))
paths=[]
DFS(korea, '평양', '부산')
print(paths)

from collections import defaultdict

class Graph():
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, v, w):
		self.graph[v].append(w)
		self.graph[w].append(v)

	def isCyclicUtil(self, v, visited, parent):
		visited[v] = True

		for i in self.graph[v]:
			if visited[i] == False:
				if self.isCyclicUtil(i, visited, v):
					return True

				elif i != parent:
					return True

		return False

	def isTree(self):
		visited = [False] * self.V

		if self.isCyclicUtil(0, visited, -1) == True:
			return False

		for i in range(self.V):
			if visited[i] == False:
				return False
				
		return True

tree = [[6,8],[5,3],[5,2],[6,4],[5,6]]
g1 = Graph(5)

#for x in tree:
#	g1.addEdge(x[0], x[1])

g1.addEdge(1,0)
g1.addEdge(0,2)
g1.addEdge(0,3)
g1.addEdge(3,4)

print(g1.isTree())

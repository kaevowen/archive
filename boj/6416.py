from collections import defaultdict


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.visited = [False] * self.V

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def fn(self, v, parent):
        self.visited[v] = True
        it = iter(self.graph[v])
        for i in it:
            print(i)
            adj = int(i)
            if False == self.visited[adj]:
                ans = self.fn(adj, v)
                if ans == False:
                    return False
            else:
                if True == self.visited[adj]:
                    if adj != parent:
                        return False
        return True

tree = []
case = 1

while 1:
    i = list(map(int, input().split(' ')))
    tree.append(i)
    if tree[-1] == [0, 0]:
        del tree[-1]
        g1 = Graph(len(tree))

        for x in tree:
            g1.addEdge(x[0], x[1])

        print(f"Case {case} is a tree") if g1.fn(0, 0) == True else print(f"Case {case} is not a tree")
        case += 1
        tree = []

    elif tree[-1] == [-1,-1]:
        break
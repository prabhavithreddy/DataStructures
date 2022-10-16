from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.V = v

    def addEdge(self, v, e):
        self.graph[v].append(e)

    def topological_sort_util(self, v, stack, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, stack, visited)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, stack, visited)

        return stack[::-1]


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topological_sort())
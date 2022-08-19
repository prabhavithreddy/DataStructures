from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = {}
        self.queue = deque()

    def add_edge(self, s, d, w):
        se = Edge(s, d, w)
        if s not in self.graph:
            self.graph[s] = []
        self.graph[s].append(se)

        de = Edge(d, s, w)
        if d not in self.graph:
            self.graph[d] = []
        self.graph[d].append(de)

    def bfs(self, v):
        print(v)
        self.visited[v] = True
        self.queue.append(v)
        while self.queue:
            v = self.queue.popleft()
            for edge in self.graph[v]:
                if edge.destination not in self.visited:
                    print(edge.source, edge.destination, edge.weight)
                    self.visited[edge.destination] = True
                    if edge.weight == 0:
                        self.queue.appendleft(edge.destination)
                    else:
                        self.queue.append(edge.destination)


g = Graph()
g.add_edge(0, 1, 0)
g.add_edge(0, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(3, 4, 0)
g.add_edge(4, 5, 1)
g.add_edge(5, 2, 1)

g.bfs(0)

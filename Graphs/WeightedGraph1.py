from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = set()
        self.queue = deque()
        self.distance = {}

    def add_edge(self, s, d, w):
        self.distance[s] = 100
        self.distance[d] = 100
        se = Edge(s, d, w)
        if s not in self.graph:
            self.graph[s] = []
        self.graph[s].append(se)

        de = Edge(d, s, w)
        if d not in self.graph:
            self.graph[d] = []
        self.graph[d].append(de)

    def bfs(self, v):
        # print(v)
        # self.visited[v] = True
        self.queue.append((v, 0))
        while self.queue:
            v, d = self.queue.popleft()
            # self.visited.add(v)
            for edge in self.graph[v]:
                c = edge.weight + d
                # self.visited.add(edge.destination)
                if c < self.distance[edge.destination]:
                    self.distance[edge.destination] = c
                    if edge.weight == 0:
                        self.queue.appendleft((edge.destination, c))
                    else:
                        self.queue.append((edge.destination, c))


g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(0, 7, 1)
g.add_edge(0, 8, 0)
g.add_edge(1, 2, 0)
g.add_edge(1, 3, 1)
g.add_edge(1, 7, 0)
g.add_edge(2, 5, 1)
g.add_edge(2, 6, 0)
g.add_edge(3, 4, 1)
g.add_edge(4, 5, 1)
g.add_edge(5, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 1)

g.bfs(2)
for key in sorted(g.distance.keys()):
    print(f"{2} - {key}: {g.distance[key]}")
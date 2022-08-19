class Edge:
    def __init__(self, source, weight, destination):
        self.source = source
        self.weight = weight
        self.destination = destination


class Graph:
    def __init__(self):
        self.visited = {}
        self.distance = {}
        self.graph = {}
        self.queue = []

    def insert(self, s, w, d):
        # self.visited[s] = False
        # self.visited[d] = False
        sn = Edge(s, w, d)
        dn = Edge(d, w, s)

        if s not in self.graph:
            self.graph[s] = []

        if d not in self.graph:
            self.graph[d] = []

        self.graph[s].append(sn)
        self.graph[d].append(dn)

    def bfs(self, source):
        if source:
            self.queue.append(source)
            self.visited[source] = True
            while self.queue:
                v = self.queue.pop(0)
                print(f"\n{v} -> ", end="")
                for node in self.graph[v]:
                    if node.destination not in self.visited:
                        print(node.destination, end=",")
                        self.queue.append(node.destination)
                        self.visited[node.destination] = True

    def sd(self, source):
        for key in self.graph:
            self.distance[key] = float('inf')

        self.distance[source] = 0
        self.queue.append((source, 0))
        while self.queue:
            v, w = self.queue.pop(0)
            for node in self.graph[v]:
                c = node.weight + w
                if c < self.distance[node.destination]:
                    self.distance[node.destination] = c
                    self.queue.append((node.destination, c))

    def sdg(self, source):
        for key in self.graph:
            self.distance[key] = float('inf')

        self.distance[source] = 0
        self.queue.append((source, 0))
        while self.queue:
            v, w = self.queue.pop(0)
            for node in sorted(self.graph[v], key=lambda p: p.weight):
                c = node.weight + w
                if c < self.distance[node.destination]:
                    print(f"{v} - {node.destination}")
                    self.distance[node.destination] = c
                    self.queue.append((node.destination, c))

    def sdg1(self, source):
        for key in self.graph:
            self.distance[key] = float('inf')

        self.distance[source] = 0
        sptset = set()

        while len(sptset) < len(self.graph):
            for v in sorted(self.distance, key=lambda k: self.distance[k]):
                if v not in sptset:
                    sptset.add(v)
                    for node in self.graph[v]:
                        d = self.distance[v] + node.weight
                        if d < self.distance[node.destination]:
                            self.distance[node.destination] = d


g = Graph()
g.insert('A', 4, 'B')
g.insert('A', 5, 'C')
g.insert('B', 9, 'D')
g.insert('B', 11, 'C')
g.insert('C', 3, 'E')
g.insert('B', 7, 'E')
g.insert('D', 13, 'E')
g.insert('D', 2, 'F')
g.insert('E', 6, 'F')

# g.bfs('A')
g.sdg1('A')
print(g.distance)
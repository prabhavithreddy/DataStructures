class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * vertices
        self.queue = []
        self.visited = {}

    def get_next_node(self, value):
        node = self.graph[value]
        while node and node.next:
            node = node.next

        return node

    def add_edge(self, src, dest):

        source = self.get_next_node(src)
        destination = self.get_next_node(dest)
        src_node = Node(src)
        dest_node = Node(dest)
        if source == None:
            self.graph[src] = dest_node
        else:
            source.next = dest_node

        if destination == None:
            self.graph[dest] = src_node
        else:
            destination.next = src_node

    def display(self):
        for index in range(self.V):
            node = self.graph[index]
            print(f"\n{index} ->", end=" ")
            t = node
            while t:
                print(t.data, end=",")
                t = t.next

    def bfs(self, v):
        if v > -1 and v not in self.visited:
            print(v)
            self.visited[v] = True
            next_node = self.graph[v]
            while next_node:
                data = next_node.data
                if data not in self.visited:
                    self.queue.append(data)
                next_node = next_node.next
            while len(self.queue) > 0:
                v = self.queue.pop(0)
                self.bfs(v)
        else:
            return


g = Graph(7)
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(1, 3);
g.add_edge(1, 4);
g.add_edge(2, 1);
g.add_edge(2, 5);
g.add_edge(3, 6);

g.display()

print("\n--------------------")

g.bfs(1)

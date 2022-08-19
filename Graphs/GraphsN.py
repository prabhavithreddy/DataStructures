class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * vertices

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


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.display()
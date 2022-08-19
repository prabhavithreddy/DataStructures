class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = dict()

    def get_next_node(self, value):
        node = self.graph.get(value)
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
        for index in self.graph.keys():
            node = self.graph[index]
            print(f"\n{index} ->", end=" ")
            t = node
            while t:
                print(t.data, end=",")
                t = t.next


g = Graph(3)
g.add_edge("A", "B")
g.add_edge("B", "C")

g.display()

print()

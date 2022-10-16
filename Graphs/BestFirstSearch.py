from queue import PriorityQueue
from collections import defaultdict

graph = defaultdict(list)

def addedge(src:int, dest:int, cost:int):
    graph[src].append((dest, cost))
    graph[dest].append((src, cost))

def best_first_search(source:int, target:int):
    pq = PriorityQueue()
    pq.put((0, source))
    visited = {source}
    while pq:
        cost, node = pq.get()
        print(node, end='->')
        if node == target:
            break

        for v in graph[node]:
            d, c = v
            if d not in visited:
                pq.put((c, d))
                visited.add(d)

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source = 0
target = 9
best_first_search(source, target)
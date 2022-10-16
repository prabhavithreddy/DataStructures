from collections import defaultdict

graph = defaultdict(list)
visited = [False] * 5


def addEdge(s, d):
    graph[s].append(d)
    graph[d].append(s)


def bfs(src):
    queue = [src]
    while queue:
        node = queue.pop()
        print(node)
        for v in graph[node]:
            if visited[v] == False:
                queue.append(v)
                visited[v] = True


def BFSHelper():
    for index in range(5):
        if visited[index] == False:
            bfs(index)
            visited[index] = True


addEdge(0, 4)
addEdge(1, 2)
addEdge(1, 3)
addEdge(1, 4)
addEdge(2, 3)
addEdge(3, 4)
print(graph)
#BFSHelper()

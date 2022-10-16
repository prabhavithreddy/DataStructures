from collections import defaultdict
shortest_distance = float('inf')
word_list = ["hot","dot","dog","lot","log","cog"]
start = 'hit'
n = len(word_list)
graph = defaultdict(list)


def get_distance(word1, word2):
  d = 0
  for i in range(len(word1)):
    if word1[i]!=word2[i]:
      d+=1

    if d==2:
      return d

  return d

for word in word_list:
  d = get_distance(start, word)
  if d == 1:
    graph[start].append(word)

for i in range(n-1):
  for j in range(i+1, n):
    left = word_list[i]
    right = word_list[j]
    d = get_distance(left, right)
    if d == 1:
      graph[left].append(right)



def dfs(start, end, distance, path):
  global shortest_distance
  if start == end and distance < shortest_distance:
    shortest_distance = distance
    print(path)

  for node in graph[start]:
    dfs(node, end, distance+1, path+'->'+node)

print(graph)
dfs('hit', 'cog', 1, 'hit')
print(shortest_distance)


from MaxHeap import MaxHeap
numbers = [1, 23, 12, 9, 30, 2, 50]

h = MaxHeap()

for i in numbers:
    h.insert(i)

k = 3

result = []

for i in range(k):
    top = h.peek()
    result.append(top)
    h.delete(top)

print(result)
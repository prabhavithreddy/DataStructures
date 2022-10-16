class MaxHeap:
    heap = []

    def heapify(self, n, index):
        largest = index
        l = 2*index + 1
        r = 2* index + 2

        if l<n and self.heap[l] > self.heap[largest]:
            largest = l

        if r<n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(n, largest)

    def insert(self, key):
        n = len(self.heap)
        if n == 0:
            self.heap.append(key)
        else:
            self.heap.append(key)
            n=n+1
            for i in range(((n//2) -1), -1, -1):
                self.heapify(n, i)

    def delete(self, key):
        j = -1
        n = len(self.heap)
        if n==0:
            return -1
        for i in range(n):
            if self.heap[i] == key:
                j = i
                break
        if j == -1:
            return -1
        else:
            self.heap[j], self.heap[-1] = self.heap[-1], self.heap[j]
            self.heap.pop()
            n = n-1
            for i in range(((n//2) -1), -1, -1):
                self.heapify(n, i)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            None
    def display(self):
        print(self.heap)

if __name__ == "__main__":
    h = MaxHeap()
    for i in range(1,11):
        h.insert(i)
    h.display()
    for i in range(10, 5, -1):
        h.delete(i)
    h.display()
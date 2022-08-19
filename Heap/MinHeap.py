class MinHeap:
    heap = []

    def heapify(self, n, index):
        smallest = index
        l = 2*index + 1
        r = 2* index + 2

        if l<n and self.heap[l] < self.heap[smallest]:
            smallest = l

        if r<n and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(n, smallest)
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
    def display(self):
        print(self.heap)

if __name__ == "__main__":
    h = MinHeap()
    for i in range(10,0, -1):
        h.insert(i)
    h.display()
    #for i in range(10, 5, -1):
    #    h.delete(i)
    #h.display()
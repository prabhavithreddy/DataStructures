R = 26

class Node:
    def __init__(self):
        self.val = None
        self.next = [None] * R

class Trie:

    def __init__(self):
        self.root = None

    def get(self, key:str) -> object:
        node = self.get(self.root, key, 0)
        if not node:
            return None
        else:
            return node.val

    def get(self, node:Node, key:str, d:int) -> Node:
        if not node:
            return None
        if d == len(key):
            return node
        char = ord(key[d]) - ord('a')
        return self.get(self.root.next[char], key, d+1)

    def add(self, key:str, value:object):
        self.root = self.put(self.root, key, value, 0)

    def put(self, node:Node, key:str, value:object, d:int):
        if not node:
            node = Node()
        if d == len(key):
            node.val = value
            return node
        char: int = ord(key[d]) - ord('a')
        node.next[char] = self.put(node.next[char], key, value, d+1)
        return node

    def show(self):
        if self.root:
            self.display([(i, self.root.next[i]) for i in range(R) if self.root.next[i]])

    def display(self, queue:list):
        if not queue:
            return
        children = []
        while queue:
            index, node = queue.pop(0)
            print(chr(ord('a') + index), end = ",")
            children.extend([(i, node.next[i]) for i in range(R) if node.next[i]])
        print("\n")
        self.display(children)

if __name__ == "__main__":
    t = Trie()
    words = "she sells sea shells on the sea shore"
    for word in words.split():
        t.add(word, len(word))

    t.show()
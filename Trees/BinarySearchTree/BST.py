class Node:
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = self.add(self.root, None, key)
        else:
            self.add(self.root, None, key)

    def add(self, node, parent, key):
        if not node:
            return Node(parent, key)
        elif key <= node.key:
            node.left = self.add(node.left, node, key)
        else:
            node.right = self.add(node.right, node, key)

        return node

    def display(self, node):
        if node:
            self.display(node.left)
            print(node.key, end=",")
            self.display(node.right)

    def minimum(self, head=None):
        head = head if head else self.root
        while head and head.left:
            head = head.left
        return head.key

    def maximum(self, head=None):
        head = head if head else self.root
        while head and head.right:
            head = head.right
        return head.key

    def find(self, key):
        head = self.root
        while head and head.key != key:
            if key < head.key:
                head = head.left
            else:
                head = head.right
        return head

    def successor(self, key):
        node = self.find(key)
        if not node:
            return None
        if node.right:
            return self.minimum(node.right)
        else:
            y = node.parent
            while y and y.right == node:
                node = y
                y = y.parent

            return y.key

    def predecessor(self, key):
        node = self.find(key)
        if not node:
            return None
        if node.left:
            return self.maximum(node.left)
        else:
            y = node.parent
            while y and y.left == node:
                node = y
                y = y.parent

            return y.key


bst = BST()
items = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
for item in items:
    bst.insert(item)

bst.display(bst.root)
print("")
print(f"Minimum is: {bst.minimum()}")
print(f"Maximum is: {bst.maximum()}")
# Find
print(f"Find {13}: {bst.find(13) != None}")
print(f"Find {40}: {bst.find(40) != None}")
# Successor
key = 7
print(f"Successor {key}: {bst.successor(key)}")
key = 15
print(f"Successor {key}: {bst.successor(key)}")
key = 13
print(f"Successor {key}: {bst.successor(key)}")
# Predecessor
key = 7
print(f"Predecessor {key}: {bst.predecessor(key)}")
key = 15
print(f"Predecessor {key}: {bst.predecessor(key)}")
key = 13
print(f"Predecessor {key}: {bst.predecessor(key)}")
key = 17
print(f"Predecessor {key}: {bst.predecessor(key)}")


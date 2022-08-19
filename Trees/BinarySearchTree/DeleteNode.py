class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root == None:
        return Node(value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)

    return root


def display(root):
    if root:
        display(root.left)
        print(root.value, end=" ")
        display(root.right)


def delete(root, value):
    if root == None:
        return -1
    if root.value == value:
        if root.left == None and root.right == None:
            return None
        elif root.right == None:
            root = root.left
            return root
        elif root.left == None:
            root = root.right
            return root
        else:
            # find the left most child of right subtree
            next_node = root.right
            while next_node.left:
                next_node = next_node.left
            next_node.left = root.left
            return root.right
    elif value < root.value:
        root.left = delete(root.left, value)
        return root
    else:
        root.right = delete(root.right, value)
        return root


root = Node(5)

items = [2, 7, 1, 3, 6, 8]
for item in items:
    insert(root, item)

display(root)
print("\n")
root = delete(root, 1)
display(root)
print("\n")
print(root.value)
from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

root = A
A.left = B
B.left = D
B.right = E
E.left = F
A.right = C


def display(root):
    if root == None:
        return
    print(root.data, end=',')
    display(root.left)
    display(root.right)


display(root)

queue = []
print('\n')


def display_level_order(root):
    while root:
        print(root.data, end=', ')

        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        if len(queue) == 0:
            break
        else:
            root = queue.pop(0)


print_queue = deque()


def display_reverse_level_order(root):
    while root:
        print_queue.appendleft(root.data)

        if root.right:
            queue.append(root.right)

        if root.left:
            queue.append(root.left)
        if len(queue) == 0:
            break
        else:
            root = queue.pop(0)

    print(print_queue)


# print_queue
#  A, C B, E D F

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


display_reverse_level_order(root)

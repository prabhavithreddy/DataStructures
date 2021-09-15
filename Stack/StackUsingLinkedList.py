class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            return -1
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head:
            return self.head.data
        return -1

    def print(self):
        temp = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next

    def is_empty(self):
        return not self.head

    def __repr__(self):
        s = ''
        temp = self.head
        while temp:
            s += temp.data+' '
            temp = temp.next
        return s

if __name__ == '__main__':
    stack = Stack()
    for i in range(1,11):
        stack.push(i)
    for i in range(1,11):
        print(stack.pop(), end=" ")
    print(stack.pop())

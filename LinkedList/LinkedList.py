class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"{self.data}"

class LinkedList(object):
    def __init__(self):
        self.head:Node = None

    def append(self, data):
        temp = self.head
        if not temp:
            self.head = Node(data)
            return
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after(self, data):
        temp = self.head
        previous = None
        while temp and temp.data < data:
            previous = temp
            temp = temp.next
        node = Node(data)
        previous.next = node
        node.next = temp

    def delete(self, data):
        temp = self.head
        previous = None

        if temp and temp.data == data:
            self.head = temp.next
            del temp
            return

        while temp and temp.data != data:
            previous = temp
            temp = temp.next
        if temp:
            previous.next = temp.next
            del temp

    def delete_pos(self, pos):
        temp = self.head
        i=0
        while i < pos:
            temp = temp.next
            i+=1

        self.delete(temp.data)

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def test_push(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.push(i)
        sll.print()

    def test_insert_after(self):
        sll = LinkedList()
        for i in range(1, 11, 2):
            sll.append(i)
        sll.insert_after(10)
        sll.print()

    def test_delete(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.append(i)
        for i in range(1, 11):
            sll.delete(i)
        sll.print()

    def test_delete_pos(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.append(i)
        sll.delete_pos(9)
        sll.print()

if __name__ == '__main__':
    sll = LinkedList()
    sll.test_delete_pos()
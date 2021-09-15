class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class LinkedList(object):
    def __init__(self):
        self.head: Node = None

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
        i = 0
        while i < pos:
            temp = temp.next
            i += 1

        self.delete(temp.data)

    def get_pos(self, pos):
        temp = self.head

        if not temp:
            return -1
        i = 0
        while i < pos:
            temp = temp.next
            i += 1

        return temp.data

    def length(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter

    def length_rec(self, head):
        if not head:
            return 0
        return 1 + self.length_rec(head.next)

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def get_middle(self):
        count = self.length()
        position = 0
        position = count // 2
        return self.get_pos(position)

    def get_middle_fast(self):
        temp = self.head
        if not temp:
            return -1

        fast = temp
        slow = fast
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def create_loop(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)

        one.next = two
        two.next = three
        three.next = four
        four.next = five
        five.next = two
        self.head = one

        pass

    def print(self):
        visited = {}
        temp = self.head
        while temp:
            if temp not in visited:
                visited[temp] = True
            else:
                break
            print(temp.data, end=" ")
            temp = temp.next

    def detect_loop1(self):
        temp = self.head
        while temp:
            if temp.next == temp:
                return True
            current = self.head
            while current != temp:
                if temp.next == current:
                    return True
                current = current.next
            temp = temp.next
        return False

    def detect_loop_floyd_cycle(self):
        slow_p = self.head
        fast_p = self.head

        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            if fast_p == slow_p:
                return True
            slow_p = slow_p.next

        return False

    def detect_loop_by_temp_node(self):
        temp = Node(-1)

        previous = None
        current = self.head

        while current:
            if current.next == temp:
                return True
            previous = current
            current = current.next
            previous.next = temp

        return False

    def reverse(self):
        previous = None
        current = self.head
        next = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def reverse_rec(self, start):
        if not start or not start.next:
            self.head = start
            return start
        rest = self.reverse_rec(start.next)
        rest.next = start
        return start

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

    def test_length(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.append(i)
        print(sll.length_rec(sll.head))

    def test_search(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.append(i)
        print(sll.search(5))
        print(sll.search(12))

    def test_get_middle(self):
        sll = LinkedList()
        for i in range(1, 6):
            sll.append(i)
        print(sll.get_middle())
        sll = LinkedList()
        for i in range(1, 7):
            sll.append(i)
        print(sll.get_middle())

    def test_get_middle_fast(self):
        sll = LinkedList()
        for i in range(5, 6):
            sll.append(i)
        print("5", sll.get_middle_fast())
        sll = LinkedList()
        for i in range(4, 6):
            sll.append(i)
        print("4-5", sll.get_middle_fast())
        sll = LinkedList()
        for i in range(3, 5):
            sll.append(i)
        print("3-4-5", sll.get_middle_fast())
        sll = LinkedList()
        for i in range(2, 6):
            sll.append(i)
        print("2-3-4-5", sll.get_middle_fast())
        sll = LinkedList()
        for i in range(1, 6):
            sll.append(i)
        print("1-2-3-4-5", sll.get_middle_fast())

    def test_detect_loop(self):
        sll = LinkedList()
        # for i in range(1, 6):
        #    sll.append(i)
        sll.create_loop()
        print(sll.detect_loop1())

    def test_detect_loop_floyd(self):
        sll = LinkedList()
        sll.create_loop()
        print(sll.detect_loop_floyd_cycle())

    def test_detect_by_temp_node(self):
        sll = LinkedList()
        sll.create_loop()
        print(sll.detect_loop_by_temp_node())

    def test_reverse(self):
        sll = LinkedList()
        for i in range(1, 3):
            sll.append(i)
        sll.reverse()
        sll.print()

    def test_reverse_rec(self):
        sll = LinkedList()
        for i in range(1, 11):
            sll.append(i)
        sll.reverse_rec(sll.head)
        sll.print()


if __name__ == '__main__':
    sll = LinkedList()
    sll.test_reverse_rec()

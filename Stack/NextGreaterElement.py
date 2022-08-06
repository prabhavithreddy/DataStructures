from StackUsingLinkedList import Stack

def naive(a, start=0):
    l = len(a)
    if start < l - 1:
        x = a[start]
        for i in range(start+1, l):
            if a[i] > x:
                print(a[i])
                return naive(a, start + 1)
            else:
                return -1
    else:
        return -1

def get_next_greater_element_using_stack(a):
    s = Stack()
    i = len(a) - 1
    while i>=0:
        c = a[i]
        if s.is_empty():
            s.push(c)
            print(-1)
        else:
            while not s.is_empty() and c >= s.peek():
                s.pop()
            if s.is_empty():
                print(-1)
            else:
                print(s.peek())
            s.push(c)
        i-=1
if __name__ == '__main__':
    #a = [5,4,3,2,1]
    #a = [4, 5, 2, 25]
    a = [13, 7, 6, 12]
    get_next_greater_element_using_stack(a)
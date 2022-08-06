from StackUsingLinkedList import Stack

def naive(a):
    l = len(a)
    freq_dict = {}
    for i in range(0, l):
        c = a[i]
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1

    frequencies = [freq_dict[x] for x in a]

    s = Stack()
    i = l - 1
    while i >=0:
        c = a[i]
        if s.is_empty():
            print(-1)
            s.push(i)
        else:
            while not s.is_empty() and frequencies[i] >= frequencies[s.peek()]:
                s.pop()
            if s.is_empty():
                print(-1)
            else:
                print(a[s.peek()])
            s.push(i)
        i-=1

if __name__ == '__main__':
    #a = [5,4,3,2,1]
    a = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
    #a = [1, 1, 2, 3, 4, 2, 1]
    naive(a)
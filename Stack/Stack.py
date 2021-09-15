import numpy as np

class Stack:
    def __init__(self, size):
        self.list = np.arange(0,size)
        self.size = size
        self.top = -1

    def push(self, item):
        if self.top < self.size - 1:
            self.top+=1
            self.list[self.top] = item

    def pop(self):
        if self.top >= 0:
            top = self.top
            self.top -= 1
            return self.list[top]
        else:
            return -1

    def current(self):
        if self.top >=0 and self.top <= self.size - 1:
            return self.list[self.top]
        return -1

if __name__ == '__main__':
    stack = Stack(10)
    for i in range(1,11):
        stack.push(i)
    for i in range(1,11):
        print(stack.pop(), end=" ")
    print(stack.pop())
    '''
    0 1 2
    '''
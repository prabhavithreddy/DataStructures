prefix = '*-A/BC-/AKL'
'''
A+B
C-D
'''
y=''
from StackUsingLinkedList import Stack
s = Stack()
operators = set(['*','+','/','-'])
i=len(prefix) - 1
while i >= 0:
    c = prefix[i]
    if c not in operators:
        s.push(c)
    else:
        A = s.pop()
        B = s.pop()
        result = '('+A+c+B+')'
        y = result
        s.push(result)
    i-=1

print(y)
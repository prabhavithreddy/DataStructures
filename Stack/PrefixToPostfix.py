prefix = '*+AB-CD'

y=''
from StackUsingLinkedList import Stack
s = Stack()
operators = set(['/','*','+','-'])
i=len(prefix) - 1
while i >= 0:
    c = prefix[i]
    if c not in operators:
        s.push(c)
    else:
        A = s.pop()
        B = s.pop()
        result = A+B+c
        s.push(result)
    i-=1

while not s.is_empty():
    y+= s.pop()
print(y)
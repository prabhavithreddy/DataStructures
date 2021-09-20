postfix = 'ab*c+'

y=''
from StackUsingLinkedList import Stack
s = Stack()
operators = set(['/','*','+','-'])
i = 0
while i < len(postfix) :
    c = postfix[i]
    if c not in operators:
        s.push(c)
    else:
        B = s.pop()
        A = s.pop()
        result = '('+A+c+B+')'
        s.push(result)
    i+=1

while not s.is_empty():
    y+= s.pop()
print(y)
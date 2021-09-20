infix = 'A * B + C / D'
'''
output: + * A B/ C D
+ *AB /CD

*AB + /CD

ABCD
*+/

*AB/CD
*
A
B
/CD
+


(A - B/C) * (A/K-L)

-ABC
'''




y=''
from StackUsingLinkedList import Stack
s = Stack()
operators = set(['/','*','+','-'])
i = 0
while i < len(infix) :
    c = infix[i]
    if c in operators:
        y+=c
    else:
        prev = s.peek()
        if not s.is_empty() and operators[prev] >= operators[c]:
            y+=s.pop()+c
        s.push(y)
        y=''
    i+=1

while not s.is_empty():
    y+= s.pop()
print(y)
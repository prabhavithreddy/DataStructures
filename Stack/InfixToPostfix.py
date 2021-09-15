from StackUsingLinkedList import Stack

s = Stack()
x = 'a+b*(c^d-e)^(f+g*h)-i)'
y =''
#BODMAS
operators = {'^':5,'/':4, '*':3, '+':2, '-':1}
s.push('(')
i=0
while not s.is_empty() and i < len(x):
    c = x[i]
    if c not in operators:
        if c=='(':
            s.push(c)

        elif c ==')':
            prev = s.peek()
            while prev !='(':
                y += s.pop()
                prev = s.peek()
            s.pop()
        else:
            y += c
    else:
        prev = s.peek()
        while prev in operators and operators[prev] >= operators[c]:
            y+=s.pop()
            prev = s.peek()
        s.push(c)
    i+=1
while not s.is_empty():
    y+=s.pop()
print(y)
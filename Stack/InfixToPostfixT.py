from StackUsingLinkedList import Stack

s = Stack()
x = 'a+b*(c^d-e)^(f+g*h)-i)'
#output: abcd^e-fgh*+^*+i-
y =''
#BODMAS
operators = {'^':5,'/':4, '*':3, '+':2, '-':1}
s.push('(')
i=0

while not s.is_empty() and i < len(x):
    c = x[i]
    if c.isalpha():
        y+=c
    elif c == "(":
        s.push(c)
    elif c == ')':
        peek = s.peek()
        while peek != '(':
            y+= s.pop()
            peek = s.peek()
        s.pop()
    elif c in operators:
        peek = s.peek()
        while not s.is_empty() and peek in operators and operators[c] <= operators[peek]:
            y+=s.pop()
            peek = s.peek()
        s.push(c)
    i+=1
while not s.is_empty():
    y+=s.pop()
print(y)
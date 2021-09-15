from StackUsingLinkedList import Stack

s = Stack()
postfix = '12345*+*+'

operators = set(['+','*'])

for c in postfix:
    if c in operators:
        first = s.pop()
        second = s.pop()
        if c == '+':
            result = first + second
            s.push(result)
        elif c == '*':
            result = first * second
            s.push(result)
    else:
        s.push(int(c))

print(s.pop())
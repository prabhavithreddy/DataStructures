from StackUsingLinkedList import Stack

expression = '[(])'
mapping = {']':'[',')':'(','}':'{'}
s = Stack()

i = 0
while i < len(expression):
    c= expression[i]

    if c not in mapping:
        s.push(c)
    else:
        if not s.is_empty() and mapping[c] != s.pop():
            break
    i+=1

print(s.is_empty())
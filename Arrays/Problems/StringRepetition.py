str = '2[a5[b]]'

stack = []

for i in range(len(str)):
  if str[i].isdigit():
    stack.append(i)

print(stack)

for index in stack[::-1]:
  start = index
  end = index

  while str[end]!="]":
    end = end+1

  expression = str[start:end+1]
  number = int(expression[0])
  residual = expression[2:-1]
  residual = number*residual
  str = str.replace(expression, residual)

str = str.replace("[", "")
str = str.replace("]", "")
print(str)
string = ["a","b","b","f","D","D","h","G","F","B","v","d","F","D","G","B","N","D","a","s","Z","V","D","F","j","k","b"]

upper_chars = []
lower_chars = []

u_count = 0
l_count = 0

for i in range(len(string)):
  char = string[i]
  if string[i].isupper():
    upper_chars.append(char)
    u_count+=1
  else:
    lower_chars.append(char)
    l_count+=1

upper_chars = sorted(upper_chars)
lower_chars = sorted(lower_chars)
#print(upper_chars)
#print(lower_chars)

result = []

i=0
j=0

while i<u_count or j < l_count:
  if i < u_count:
    result.append(upper_chars[i])
  if j < l_count:
    result.append(lower_chars[i])
  i+=1
  j+=1

print(result)
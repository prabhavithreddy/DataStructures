s = "aaaa"
def get_reverse(s):
  n = len(s)
  for i in range(1, len(s)+1):
    i = i % n
    yield s[i:]+s[0:i]
  return -1

counter=1
for a in get_reverse(s):
  print(a)
  if a==s:
    break
  else:
    counter+=1

print(counter)

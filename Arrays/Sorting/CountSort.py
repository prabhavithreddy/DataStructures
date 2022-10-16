a = [2,5,3,0,2,3,0,3]
n = len(a) - 1
b = []
c = []
k=0

for i in a:
  b.append(0)
  if i > k:
    k = i

for i in range(k+1):
  c.append(0)

for i in a:
  c[i] = c[i] + 1

print(c)

for i in range(1,k+1):
  c[i] = c[i] + c[i-1]

print(c)

for i in range(n,-1, -1):
  b[c[a[i]] - 1] = a[i]
  c[a[i]] = c[a[i]] - 1
  #print(b)

print(b)
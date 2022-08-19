a = [1,2,3,4]

n = len(a)
for k in range(n):
  for i in range(n-k):
    print(a[i:i+k+1], end=" ")
    for j in range(i+1,n-k):
      print(a[j], end="")
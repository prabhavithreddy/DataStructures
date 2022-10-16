a = [4,0,3,8,9]

inversions = set()

n = len(a) - 1
k=1
for i in range(n-k, -1, -1):
  for j in range (n-k+1, n+1):
    if i < j and a[i] > a[j]:
      inversions.add(f"{a[i]}, {a[j]}")
  k+=1

print(inversions)
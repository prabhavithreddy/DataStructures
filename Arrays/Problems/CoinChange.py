s = [2, 5, 3, 6]

n = 10
result = []
N = 4
for i in len(s):
    k = i
    s1 = []
    s1.append(i)
    j = n
    while k < N - 1 and j >= 0:
        j = j - s[k]
        if j in s:
            s1.append(j)
        k = k + 1
        print(s1)
    result.append(s1)

print(result)
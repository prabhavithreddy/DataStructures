a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = [[], [], []]
n = len(a)

s = 0

for i in range(n):
    for j in range(n):
        sum = 0
        for k in range(n):
            sum += a[i][k] * b[k][j]

        r[i].append(sum)
        s += 1

print(r)
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

r = []


def mat_mul(a, b, dima, n):
    if len(dima) == 1:
        sum = 0
        for m in range(n):
            sum += a[dima[0]][m] * b[m][dima[0]]
        return sum
    else:
        mid = (dima[0] + dima[-1]) // 2
        al = list(range(dima[0], mid+1))
        ar = list(range(dima[mid+1], dima[-1]))
        left = mat_mul(a, b, al, n)
        right = mat_mul(a, b, ar, n)

        r.append(left)
        r.append(right)


print(mat_mul(a, b, [0,1,2,3], 3))


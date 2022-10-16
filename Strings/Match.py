# p = 'aabaabaaa'
p = 'abcaby'


def prefix_1(p):
    j = 0
    q = 1
    m = len(p)
    a = [0 for i in p]

    while q < m:
        if p[q] == p[j]:
            a[q] = j + 1
            j += 1
            q += 1
        elif j == 0:
            a[q] = 0
            q += 1
        else:
            j = a[j - 1]
    return a


def prefix_2(p):
    m = len(p)
    a = [0 for i in p]
    k = 0
    for q in range(1, m):
        while k > 0 and p[k + 1] != p[q]:
            k = a[k]
        if p[k + 1] == p[q]:
            k = k + 1
        a[q] = k
    return a


print(prefix_1(p))
# print(prefix_2(p))
t = 'abxabcabcaby'


def match(t, p):
    n = len(t)
    m = len(p)
    prefix = prefix_1(p)
    j = 0
    for s in range(n):
        while j > 0 and t[s] != p[j]:
            j = prefix[j - 1]

        if p[j] == t[s]:
            j = j + 1

        if j == m:
            print('Match')
            j = prefix[j - 1]

    return -1


print(match(t, p))
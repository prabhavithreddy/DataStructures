import heapq
import numpy as np


# a = list(np.random.randint(1,1000,20))
# a = [58,93,73,31,34,14,12,77,19,35]
# a = [83,5,30,59,81,88,36,78,10,57]
# a = [627, 871, 812, 346, 759, 512, 614, 660, 969, 697, 573, 531, 620, 124, 136, 372, 711, 119, 748, 695]
def partition(a, l, h):
    pivote = a[h - 1]
    i = l - 1
    for j in range(l, h - 1):
        if a[j] < pivote:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[h - 1] = a[h - 1], a[i + 1]
    return i + 1


def median(a, l, h, i):
    if l < h:
        p = partition(a, l, h)
        if p == i:
            return a[i]
        elif p < i:
            return median(a, p + 1, h, i)
        else:
            return median(a, l, p, i)


def get_median(a):
    n = len(a)
    if n % 2 == 0:
        return (median(a, 0, n, n // 2) + median(a, 0, n, n // 2 - 1)) / 2
    else:
        return median(a, 0, n, n // 2)


for i in range(20):
    a = list(np.random.randint(1, 1000, 50))
    print(get_median(a))
    print(np.median(a))
    print('------------')
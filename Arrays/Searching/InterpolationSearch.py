import numpy as np
'''
y = mx + c
arr[lo] = m*lo + c  (1)
arr[hi] = m*hi + c  (2)

arr[hi] - arr[lo] = m(hi - lo)
m = (arr[hi] - arr[lo])/ (hi - lo)

x = m*pos + c (3)

x - arr[hi] = m*pos - m*hi
x - arr[hi] = m(pos - hi)
(x - arr[hi])/m = pos - hi

pos = hi + (x - arr[hi])*(hi - lo) / (arr[hi] - arr[lo])


'''

def InterpolationSearch(arr, lo, hi, x):
    if lo < hi and x >= arr[lo] and x <= arr[hi]:

        pos = int(hi + (((x - arr[hi])*(hi - lo)) / (arr[hi] - arr[lo])))
        pos_num = arr[pos]
        if pos_num == x:
            return pos

        if pos_num < x:
            return InterpolationSearch(arr, pos+1, hi, x)
        else:
            return InterpolationSearch(arr, lo, pos - 1, x)

    return -1

if __name__ == '__main__':
    numbers = np.linspace(10, 100, 10).astype(int)
    print(numbers)
    print(InterpolationSearch(numbers, 0 , len(numbers) - 1, 45))

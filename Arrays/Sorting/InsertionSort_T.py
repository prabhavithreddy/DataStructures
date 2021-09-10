import numpy as np

def InsertionSort(a):
    n = len(a)
    if n<2:
        return a
    i = 1
    while i < n:
        j = i-1
        k = a[i]
        while j>=0 and k < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = k
        i = i+1
    print(a)


if __name__ == '__main__':
    arr = np.random.randint(1,100,10)
    print(arr)
    InsertionSort(arr)
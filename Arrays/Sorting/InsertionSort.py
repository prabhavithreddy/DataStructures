import math
import numpy as np

def InsertionSort(a):
    i = 1
    n = len(a)
    while i < n:
        j=i-1
        t = a[i]
        while j>=0 and a[j] > t:
            a[j+1] = a[j]
            j-=1
        a[j+1] = t
        i+=1
    print(a)

if __name__ == '__main__':
    arr = np.random.randint(1,1000,50)
    InsertionSort(arr)
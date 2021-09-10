import math
import numpy as np

def SelectionSort(a, i):
    if i < len(a):
        min_index = get_min(a, i+1)
        if min_index > i:
            a[i], a[min_index] = a[min_index], a[i]
            SelectionSort(a, i+1)
    return a

def get_min(a, start):
    if start >= len(a):
        return -1
    min_index = start
    for i in range(start+1, len(a)):
        if a[i] < a[min_index]:
            min_index = i
    return min_index

if __name__ == '__main__':
    arr = np.random.randint(1,100,10)
    print(arr)
    #print(get_min(arr, 0))
    print(SelectionSort(arr,0))
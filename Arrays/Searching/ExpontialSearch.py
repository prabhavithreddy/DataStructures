import numpy as np
from BinarySearch import binary_search

def ExponentialSearch(arr, start, end, key):
    if arr[0] == key:
        return 0

    i = 1
    while i < end and arr[i]<= key:
        i = i * 2
    print(f"i/2: {i//2}, i:{i}")
    return binary_search(arr, i//2, min(i, end), key)


if __name__ == '__main__':
    arr = list(np.linspace(1, 100, 50).astype(int))
    start = 0
    end = len(arr) - 1
    print(arr)
    print(ExponentialSearch(arr, start, end, 100))
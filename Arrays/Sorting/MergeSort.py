import numpy as np
def MergeSort(arr):
    if len(arr) < 2:
        return
    l = 0
    r = len(arr) - 1
    m = (l + r) // 2

    left_arrary = arr[l: m + 1]
    right_array = arr[m + 1: r + 1]

    MergeSort(left_arrary)
    MergeSort(right_array)
    Merge(left_arrary, right_array, arr)
    return arr

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr


if __name__ == '__main__':
    #97  5 63 63 77 55 42 27 17 75
    numbers = np.random.randint(1,10000000,100)
    print(numbers)
    print(MergeSort(list(numbers)))

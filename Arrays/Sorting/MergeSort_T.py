import numpy as np
def MergeSort(a):
    l = 0
    r = len(a) - 1
    if (r - l) < 1:
        return a
    mid = l + (r - l)//2

    left = MergeSort(a[l: mid+1])
    right = MergeSort(a[mid+1: r+1])
    return Merge(left, right, a)

def Merge(left, right, a):

    i=0
    j=0
    k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i+=1
        else:
            a[k] = right[j]
            j+=1
        k+=1

    while i < len(left):
        a[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        a[k] = right[j]
        j+=1
        k+=1

    return a


if __name__ == '__main__':
    #97  5 63 63 77 55 42 27 17 75
    numbers = np.random.randint(1,100,10)
    print(numbers)
    print(MergeSort(list(numbers)))

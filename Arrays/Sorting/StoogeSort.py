import math


def StoogeSort(arr, l, r):
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]
    if (r - l)>2:
        t = math.floor((r - l)/3)
        StoogeSort(arr, l, r - t)
        StoogeSort(arr, l+t, r)
        StoogeSort(arr, l, r - t)
    return arr


if __name__ == '__main__':
    arr = [10,9,8,7,6,5,4,3,2,1]
    l = 0
    r = len(arr) - 1
    print(StoogeSort(arr, l, r))

    '''
    Debug 
        mid_point = (0 + 4) // 2 = 2
        arr[mid_point] = 3 < target
            mid_piont = (2 + 4) // 2 = 3
            arr[mid_point] = 4 == target 
    '''
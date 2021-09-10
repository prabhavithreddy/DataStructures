def ternary_search(arr, l, r, key):
    if len(arr) < 1:
        return - 1

    if l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < arr[mid1]:
            return ternary_search(arr, l, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, r, key)
        else:
            return ternary_search(arr, mid1 + 1, mid2 -1, key)

    else:
        return -1

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    start = 0
    end = len(arr) - 1
    print(ternary_search(arr, start, end, 10))

    '''
    Debug 
        mid_point = (0 + 4) // 2 = 2
        arr[mid_point] = 3 < target
            mid_piont = (2 + 4) // 2 = 3
            arr[mid_point] = 4 == target 
    '''
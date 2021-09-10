def binary_search(arr, start, end, target):
    if len(arr) < 1:
        return - 1

    if start <= end:
        mid_point = (start + end) // 2
        if arr[mid_point] == target:
            return mid_point
        elif arr[mid_point] < target:
            return binary_search(arr, mid_point + 1, end, target)
        else:
            return binary_search(arr, start, mid_point - 1, target)
    else:
        return -1

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    start = 0
    end = len(arr) - 1
    print(binary_search(arr, start, end, 2))

    '''
    Debug 
        mid_point = (0 + 4) // 2 = 2
        arr[mid_point] = 3 < target
            mid_piont = (2 + 4) // 2 = 3
            arr[mid_point] = 4 == target 
    '''
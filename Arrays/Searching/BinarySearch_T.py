def binary_search(arr, start, end, target):
    if start <= end:
        m = start + (end - start) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            return binary_search(arr, start, m-1, target)
        else:
            return binary_search(arr, m+1, end, target)

    return -1



if __name__ == '__main__':
    arr = [1,2,3,4,5]
    start = 0
    end = len(arr) - 1
    for i in range(0, len(arr)+1):
        print(binary_search(arr, start, end, i))

    '''
    Debug 
        mid_point = (0 + 4) // 2 = 2
        arr[mid_point] = 3 < target
            mid_piont = (2 + 4) // 2 = 3
            arr[mid_point] = 4 == target 
    '''
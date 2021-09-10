def SubArrays(arr):
    if len(arr) < 2:
        print(arr)
        return

    n = len(arr)
    last_index = n - 1

    for size in range(1, n+1):
        for i in range(0, n - size+1):
            print(arr[i:i+size])

def SubArraysRec(arr, n, size):
    if size < 1:
        return
    for i in range(0, n-size):
        print(arr[i: i+size])
    SubArraysRec(arr, n, size-1)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    SubArraysRec(arr,5,5)
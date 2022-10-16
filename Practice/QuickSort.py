def partition(a, low, high):
    i = low - 1
    pivote = a[high]
    if low < high:
        for j in range(low, high):
            if a[j] < pivote:
                i=i+1
                a[i], a[j] = a[j], a[i]

        a[i+1], a[high] = pivote, a[i+1]
        return i+1



def sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        sort(array, low, pi-1)
        sort(array, pi+1, high)

    else:
        return

array = [5,4,3,2,1]
print(array)
sort(array, 0, 4)
print(array)
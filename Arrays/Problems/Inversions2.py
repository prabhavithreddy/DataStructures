a = [2, 3, 8, 6, 1]
inversions = set()


def merge(arr1, arr2, p, q):
    i = 0
    j = 0
    k = p
    n1 = len(arr1)
    n2 = len(arr2)
    # print(arr1,arr2)
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            a[k] = arr1[i]
            i += 1
        else:
            l = i
            while l < n1 and arr1[l] > arr2[j]:
                # inversions.add(f"{arr1[l]}, {arr2[j]}")
                print(f"{arr1[l]}, {arr2[j]}")
                l += 1
            a[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = arr1[i]
        k += 1
        i += 1
    while j < n2:
        a[k] = arr2[j]
        k += 1
        j += 2

    return a[p:q]


def merge_sort(a, low, high):
    mid = (low + high) // 2

    if mid == low:
        return [a[mid]]

    left = merge_sort(a, low, mid)
    right = merge_sort(a, mid, high)

    return merge(left, right, low, high)


merge_sort(a, 0, len(a))
print(inversions)
print(a)
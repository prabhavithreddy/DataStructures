a = [7, 0, 9, 4, 8, 3, 2, 1]
n = len(a)


def merge(arr1, arr2):
    result = []
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < l1:
        result.append(arr1[i])
        i+=1
    while j < l2:
        result.append(arr2[j])
        j+=1
    return result


def sort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        l = sort(a, low, mid)
        r = sort(a, mid + 1, high)
        return merge(l, r)

    elif low == high:
        return [a[low]]

    else:
        return []


print(sort(a, 0, n - 1))

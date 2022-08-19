input = ["for", "", "", "", "geeks", "ide", "", "practice", "", "",  "quiz","", ""]


def linear_search(low, high, target):
    for i in range(low, high + 1):
        if input[i] == target:
            return i
    return -1


def binary_search(low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    left = mid - 1
    right = mid + 1

    while True:
        if left < low and right > high:
            return -1
        if left >= low and input[left] != "":
            mid = left
            break
        if right<=high and input[right] != "":
            mid = right
            break
        left-=1
        right+=1

    if input[mid] == target:
        return mid
    elif input[mid] < target:
        return binary_search(mid + 1, high, target)
    else:
        return binary_search(low, mid - 1, target)


print(binary_search(0, len(input) - 1, 'quiz'))
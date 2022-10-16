#import numpy as np

# numbers = np.random.randint(100, size=(10,))
numbers = [22, 6, 79, 90, 95, 70, 51, 50, 80, 76, 94]
n = len(numbers)
print(numbers)


def partition(low, high):
    i = low - 1
    pivote = numbers[high]
    for j in range(low, high):
        if numbers[j] < pivote:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[high] = pivote, numbers[i + 1]
    return i + 1


def sort(low, high):
    if low < high:
        pi = partition(low, high)
        sort(low, pi - 1)
        sort(pi + 1, high)

    else:
        return


sort(0, n - 1)
print(numbers)
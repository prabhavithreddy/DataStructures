import numpy as np


def insertion_sort(nums, n):
    if n == 0:
        return n

    key = nums[n]
    index = insertion_sort(nums, n - 1)
    while index >= 0 and key < nums[index]:
        nums[index + 1] = nums[index]
        index -= 1

    nums[index + 1] = key
    return n


a = np.random.randint(1, 100, 20)
print(a)
insertion_sort(a, len(a) - 1)
print(a)
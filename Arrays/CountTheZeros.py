'''
Count the Zeros
Easy Accuracy: 54.06% Submissions: 30354 Points: 2
Given an array of size N consisting of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

Example 1:

Input:
N = 12
Arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}
Output: 3
Explanation: There are 3 0's in the given array.

Example 2:

Input:
N = 5
Arr[] = {0, 0, 0, 0, 0}
Output: 5
Explanation: There are 5 0's in the array.

Your Task:
You don't need to read input or print anything. Your task is to complete the function countZeroes() which takes the array of integers arr[] and its size n as input parameters and returns the number of zeroes present in the array.


Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 105
0 <= Arr[i] <= 1


Solutions
1. Brute Force
    while you find 0
2. Binary Search
'''


def countZeroes(self, arr, n):
    number_of_zeros = 0
    first_index = 0
    last_index = n - 1

    if n < 1:
        return 0
    if n == 1:
        if arr[first_index] == 0:
            return 1
        else:
            return 0
    else:
        if arr[first_index] == 0:
            return n
        elif arr[last_index] == 1:
            return 0
        else:
            index = 0
            while arr[index] == 1:
                index += 1
            number_of_zeros = n - index
    return number_of_zeros
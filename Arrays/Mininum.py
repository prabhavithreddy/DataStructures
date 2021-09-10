import numpy as np
import datetime
def Minimum(arr):
    if len(arr)<2:
        return arr[0]
    l = 0
    r = len(arr) - 1
    m = (l + r)//2

    left = arr[l: m+1]
    right = arr[m+1: r+1]

    l_m = Minimum(left)
    r_m = Minimum(right)
    return minimize(l_m, r_m)

def minimize(left, right):
   if left < right:
       return left
   else:
       return right

def get_minimum(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum


def DAC_Min(a, index, l):
    min = 0;
    if (index >= l - 2):
        if (a[index] < a[index + 1]):
            return a[index];
        else:
            return a[index + 1];

    # Logic to find the Minimum element
    # in the given array.
    min = DAC_Min(a, index + 1, l);

    if (a[index] < min):
        return a[index];
    else:
        return min;

if __name__ == '__main__':
    numbers = np.random.randint(1, 100000, 1000)
    print(numbers)
    import datetime
    before = datetime.datetime.now()
    print(Minimum(list(numbers)))
    after = datetime.datetime.now()
    print(f"DAC: {(after-before).microseconds}")

    before = datetime.datetime.now()
    print(get_minimum(list(numbers)))
    after = datetime.datetime.now()
    print(f"Linear: {(after - before).microseconds}")

    before = datetime.datetime.now()
    print(DAC_Min(list(numbers),0, len(numbers)))
    after = datetime.datetime.now()
    print(f"DAC_Min: {(after - before).microseconds}")
    '''
    5,4,3,2,1
    m = 2
    left = [5,4,3]
    right = [2,1]
        5,4,3
        m = 1
        left = [5,4]
        right = [3]
            5,4
            m=0
            left = 5
            right = 4
            return 4
    
    '''
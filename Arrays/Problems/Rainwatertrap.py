import math
#buildings = [1,0,2,1,0,1,3,2,1,2,1,0,1]
#buildings = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
buildings = [2,0,2, 1, 2]

def solution1():
    left = 0
    right = 0
    pivote = buildings[left]
    sum = 0

    while right < buildings_length:
        min = 0
        min_pos = left
        right = left + 1

        while right < buildings_length and buildings[right] <=pivote:

            if buildings[right] >=min and buildings[right] <=pivote:
                min = buildings[right]
                min_pos = right

            right+=1

        if buildings[right] >= pivote:
            min = pivote
        else:
            right = min_pos

        while left < right:
            if min >= buildings[left]:
                sum += min - buildings[left]
            left +=1

        right = second_right
        if right == buildings_length - 1:
            break

        left = right
        pivote = buildings[left]

    print(sum)
    
def solution2():
    sum = 0
    max = max_height(buildings)

    for i in range(1, max+1):
        j=0
        while j < buildings_length -1:
            left = buildings[j]
            if left == i:
                k = j+1
                while k < (buildings_length - 1) and buildings[k] < left:
                    k+=1
                if buildings[k] < left:
                    break
                while j < k:
                    sum+= i - buildings[j]
                    if buildings[j] < i:
                        buildings[j] = i
                    j+=1

                j=k
            else:
                j+=1
    return sum

def solution3():
    sum = 0
    buildings_length = len(buildings)

    for i in range(buildings_length):
        current = buildings[i]
        j, k = i -1, i+1

        max_l, max_r = current, current

        while j>=0:
            if buildings[j] > max_l:
                max_l = buildings[j]
            j-=1

        while k < buildings_length:
            if buildings[k] > max_r:
                max_r = buildings[k]
            k+=1

        sum+= min(max_l, max_r) - current

    return sum

def max_height(array):
    max=array[0]
    for i in array:
        if i >= max:
            max = i
    return max

print(solution3())
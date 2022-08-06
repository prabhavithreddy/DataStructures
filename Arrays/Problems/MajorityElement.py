def get_majority1():

    a = [3,3,4,2,4,4,2,4,4]
    #a = [1,2,1]
    #a = [1, 2, 3,4,5]
    length = len(a)
    mid = length // 2
    counter=0
    i = mid - 1
    n=0
    while i <= mid+1:
        counter = 0
        if i<=(mid+1) and a[i] == a[i+1]:
            i+=1
        else:
            for j in range(length):
                n += 1
                if a[i] == a[j]:
                    counter+=1
                if counter == (mid+1):
                    print(a[i])
                    return True
                if j == mid+1 and counter < 2:
                    break
            i+=1

    print(n)
    if counter < mid+1:
        return False

def get_majority2():

    a = [3,3,4,2,4,4,2,4,4]
    #a = [1,2,1]
    #a = [1, 2, 3,4,5]
    length = len(a)
    mid = length // 2
    r = length // 3
    counter=0
    i = 0
    n=0
    while i < length - r:
        counter = 0
        if a[i] != a[i+1] or a[i] != a[i+2] or a[i+1] != a[i+2]:
            pass
        elif a[i] == a[i+1] or a[i] == a[i+2]:
            n = a[i]
        elif a[i+1] == a[i+2]:
            n = a[i+1]
        if n>0:
            for j in range(length):
                if n == a[j]:
                    counter+=1
                if counter == (mid+1):
                    print(a[i])
                    return True
        if i + r > length:
            i+= length - r
        else:
            i+=3
    print(n)
    if counter < mid+1:
        return False

print(get_majority2())
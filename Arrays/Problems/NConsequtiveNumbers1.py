n = 85
count = 1

for level in range(2,n):
    if level > 1:
        set = []
        c = n // level
        if level == 2:
            start = 0
        elif level % 2 == 0:
            start = (level // 2) - 1
        else:
            start = level // 2
        c = c - start
        end = c + level - 1
        sum = (level/2.)*(c + end)
        if c > 0:
            if sum == n:
                count+=1
        else:
            break

print(count)
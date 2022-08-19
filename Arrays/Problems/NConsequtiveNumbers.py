n = 100
super_set = []

def combinations(n, level):
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
        if c >= 1:
            sum = 0
            while sum <= n:
                sum+= c
                set.append(c)
                if sum == n:
                    super_set.append(set)
                    break
                c += 1
            combinations(n, level + 1)
        else:
            return
    else:
        super_set.append([n])
        combinations(n, level + 1)


combinations(n, 1)
print(super_set)
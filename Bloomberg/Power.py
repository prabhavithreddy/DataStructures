d = {}


def pow(x, n):
    if n < 0:
        return 1 / pow(x, abs(n))
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        left = n // 2
        right = n - n // 2
        if left not in d:
            left_r = pow(x, n // 2)
            d[left] = left_r
        if right not in d:
            right_r = pow(x, n - n // 2)
            d[right] = right_r

        return d[left] * d[right]


print(pow(2, -2))
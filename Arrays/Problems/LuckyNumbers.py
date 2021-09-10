def is_lucky_number(a,seed, n):
    if seed > len(a):
        return True
    if n % seed == 0:
        return False
    n = n - n//seed
    return is_lucky_number(a, seed+1, n)

if __name__ == '__main__':
    n = 13
    numbers = list(range(1,n+1))
    print(is_lucky_number(numbers, 2, n))
    '''
    1. Sort and Compare consequtive 
    2. For each number check if exists in rest of the array
    3. Use dictionary for the presence of an existing element
    '''
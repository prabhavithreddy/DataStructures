def is_lucky_number(a, start, end):
    if start < end:
        if is_number_exists(a, start+1, end, a[start]):
            return False
        else:
            return is_lucky_number(a, start+1, end)

    else:
        return True

def is_number_exists(a, start, end, number):
    for i in range(start, end+1):
        if a[i] == number:
            return True
    return False

if __name__ == '__main__':
    numbers = [1,2,9,1]
    print(is_lucky_number(numbers, 0, len(numbers) - 1))
    '''
    1. Sort and Compare consequtive 
    2. For each number check if exists in rest of the array
    3. Use dictionary for the presence of an existing element
    '''
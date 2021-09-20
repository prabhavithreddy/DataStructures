number = 1234

def SumofDigits(n):
    if n < 10:
        return n
    else:
        sum = 0
        while n > 0:
            sum+= n % 10
            n = n//10
        return SumofDigits(sum)

def SumofDigitsOptimized(n):
    if n == 0:
        return 0
    elif n%9 ==0:
        return 9
    else:
        return n%9

if __name__ == '__main__':
    #print(SumofDigits(1234))
    #print(SumofDigits(5674))
    print(SumofDigitsOptimized(1234))
    print(SumofDigitsOptimized(5674))
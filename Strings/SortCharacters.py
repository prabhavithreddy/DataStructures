'''
Input : bbccdefbbaa
Output : aabbbbccdef
'''

#input = ['b','b','c','c','d','e','f','b','b','a','a']
input = ["g","e","e","k","s","f","o","r","g","e","e","k","s"]
n = len(input)
print(input)


def partition(low, high):
    pivote = input[high]
    i = low - 1
    for j in range(low, high):
        if ord(input[j]) < ord(pivote):
            i+=1
            input[i], input[j] = input[j], input[i]
    input[i+1], input[high] = pivote, input[i+1]
    return i + 1

def sort(low, high):
    if low < high:
        pi = partition(low, high)
        sort(low, pi-1)
        sort(pi+1, high)

sort(0,n-1)
print(input)
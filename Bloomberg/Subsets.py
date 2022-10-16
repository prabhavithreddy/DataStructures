s = "abc"
n = len(s)


def solution1():
    for i in range(n):
        for j in range(i, n):
            print(s[i:j + 1])

def printAllSubstrings(s, n):
    # Fix start index in outer loop.
    # Reveal new character in inner loop till end of string.
    # Print till-now-formed string.
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            print(temp)

printAllSubstrings(s, n)



# Approach 1
# Create an indexed array
# maintain the counts of each character in their respective index
# iterate the array and if count > 0 then print the chars

# Approach 2
# Using Binary Search Tree data structure

alphabets = []
for i in range(26):
    alphabets.append(0)

input = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]

for char in input:
    char_ord = ord(char) - ord('a')
    alphabets[char_ord] += 1

for index in range(26):
    a = 'a'
    count = alphabets[index]
    if count > 0:
        result = chr(ord(a) + index)
        result = result * count
        print(result, end="")

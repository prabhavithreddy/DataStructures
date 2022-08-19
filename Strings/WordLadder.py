# Input: Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}, start = TOON, target = PLEA
# Output: 7
# Explanation: TOON – POON – POIN – POIE – PLIE – PLEE – PLEA


# Write a function to detect only one character change
# start with the start word
# take a list, if prev length == current length i.e. end of the search

dictionary = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]

start = "TOON"
end = "PLEA"

result = []


def get_change(word1, word2):
    if word1 is None and word2 is None:
        return 0
    if word1 is None and word2 is not None:
        return len(word2)
    if word1 is not None and word2 is None:
        return len(word1)

    counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
        if counter > 1:
            return counter

    return counter


previous_length = 0
result.append(start)

while len(result) > previous_length:
    prev_word = result[-1]

    for i in range(len(dictionary)):
        word = dictionary[i]
        start_distance = get_change(prev_word, word)
        end_distance = get_change(word, end)

        if start_distance == 1 and end_distance == 1:
            result.append(word)
            result.append(end)
            previous_length = len(result)
            break
        elif start_distance == 1 and end_distance == 0:
            result.append(word)
            previous_length = len(result)
            break
        if start_distance == 1:
            result.append(word)
            dictionary[i] = None
            break
    previous_length += 1

if result[-1] == end:
    print(len(result))
elif get_change(result[-1], end) == 1:
    result.append(end)
    print(len(result))
else:
    print(0)

print(result)


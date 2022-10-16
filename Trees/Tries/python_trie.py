from pygtrie import CharTrie

t = CharTrie()

words = "she sells sea shells on the sea shore"
for word in words.split():
    t[word] = word

count = 0
for key in t.itervalues("sh"):
    if count == 3:
        break
    print(key)
    count+=1
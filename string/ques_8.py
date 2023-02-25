# Write a Python function that takes a list of words
# and return the longest word and the length of the longest one
l = ["This", "is", "a", "list", "of", "words"]
word = ""
length = 0
for i in l:
    if len(i) > length:
        length = len(i)
        word = i
print("longest_word = ", word)
print("longest_length = ", length)



#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def word_count(words):
    word_set = set(words)
    word_counts = {}
    for word in word_set:
        word_counts[word] = words.count(word)
    return word_counts

words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
print(word_count(words))


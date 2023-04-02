# Write a Python program to remove specific words from a given list.
def remove_word(word,remove):
    for i in remove:
        for j in word:
            if i==j:
                word.remove(i)
    return word
word=['red', 'green', 'blue', 'white', 'black', 'orange']
remove=['white', 'orange']
a=remove_word(word,remove)
print(a)

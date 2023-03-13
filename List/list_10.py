# Write a Python program to find the list of words that are longer 
# than n from a given list of words
wordlist = ['apple', 'ball', 'cat', 'dog', 'elephant']
n = 4
lwords = [i for i in wordlist if len(i) > n]
print(lwords)

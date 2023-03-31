# Write a Python program to remove duplicate words from a given list of strings
def word(l1):
    unique=list(set(l1))
    return unique
l1=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
print(word(l1))
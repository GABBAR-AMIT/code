# Write a Python program to count the number of strings from a given list of strings. 
# The string length is 2 or more and the first and last characters are the same
strings = ['anna', 'level', 'deed', 'pop', 'hello', 'wow']
count = len([s for s in strings if len(s) >= 2 and s[0] == s[-1]])
print(count)

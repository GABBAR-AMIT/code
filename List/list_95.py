# Write a Python program to sort each sublist of strings in a given list of lists.
a=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
b=list(map(sorted,a))
print(b)
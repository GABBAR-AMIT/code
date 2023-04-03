# Write a Python program to convert a given list of tuples to a list of strings.
given = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
string = [f"{i[0]} and {i[1]}" for i in given]

print("The converted list is:", string)


# Write a Python program to extract a specified column from a given nested list.
a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
b=[i.pop(1) for i in a]
print(b)
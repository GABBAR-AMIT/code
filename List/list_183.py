# Write a Python program to get the unique values in a given list of lists
a=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
b=[i for j in a for i in j]
c=set(b)
print(c)
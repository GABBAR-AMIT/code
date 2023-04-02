#  Write a Python program to find common elements in a given list of lists
lst = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
common = list(set.intersection(*map(set, lst)))
print("Common elements of the given list of lists:")
print(common)

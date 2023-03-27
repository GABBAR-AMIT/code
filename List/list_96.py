# Write a Python program to sort a given list of lists by length and value.
a= [[2, 3, 1], [5, 4], [7, 6, 8, 9], [10]]
a.sort(key=lambda b:(len(b),b))
print(a)
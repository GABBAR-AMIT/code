# Write a Python program to remove an empty tuple(s) from a list of tuples
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
a=[i for i in a if i]
print(a)
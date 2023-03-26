# Write a Python program to pack consecutive duplicates of a given list of elements into sublists
from itertools import groupby
a=[0, 0, 1, 1, 2, 3, 3, 3, 4, 4,5]
b=[list(x)for _,x in groupby(a)]
print(b)

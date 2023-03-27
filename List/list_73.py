# Write a Python program to remove consecutive (following each other continuously) 
# duplicates (elements) from a given list.
from itertools import groupby
a = [1,2,4,7,3,7,8,4,4,9,9,10,9]
b=[x for x,_ in groupby(a)]
print(b)
    
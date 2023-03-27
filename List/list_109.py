# Write a Python program to rotate a given list by a specified number 
# of items in the right or left direction
from collections import deque
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=deque(a)
b.rotate(7)
c=list(b)
print(c)


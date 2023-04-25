# Write a Python program to create a dictionary from two lists without losing duplicate values
from collections import defaultdict
a=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b=[1,2,2,3]
c=defaultdict(list)
for i,j in zip(a,b):
    c[i].append(j)
print(dict(c))
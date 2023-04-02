# Write a Python program to get all possible combinations of the elements of a given list
from itertools import combinations
a=['orange', 'red', 'green', 'blue']
l=[]
for i in range(1,len(a)+1):
    l+=combinations(a,i)
print(l)
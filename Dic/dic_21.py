# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary
import itertools
a={'1':['a','b'], '2':['c','d']}
b=[i for i in a.values()]
c=list(itertools.product(*b))
for j in c:
    print("".join(j))
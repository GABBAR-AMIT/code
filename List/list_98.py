# Write a Python program to scramble the letters of a string in a given list
import random
a=['Python', 'list', 'exercises', 'practice', 'solution']
for i in range(len(a)):
    b=list(a[i])
    random.shuffle(b)
    c="".join(b)
    a[i]=c
print(a)

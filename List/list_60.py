# Write a Python program to find a tuple, the smallest second index value from a list of tuples.
a = [(4, 8), (1, 9), (6, 9),(1, 4), (2, 6), (4, 2), (8, 10)]
b=sorted(a,key=lambda x: x[1])
c=b[0]
print(c)
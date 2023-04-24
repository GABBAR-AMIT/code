# Write a Python program to find the highest 3 values of corresponding keys in a dictionary
from heapq import nlargest
a={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
b=nlargest(3,a,key=a.get)
print(b)



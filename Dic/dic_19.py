# Write a Python program to combine two dictionary by adding values for common keys.
from collections import Counter
a = {'a': 100, 'b': 200, 'c':300}
b = {'a': 300, 'b': 200, 'd':400}
d = Counter(a) + Counter(b)
print(d)

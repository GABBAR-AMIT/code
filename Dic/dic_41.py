#  Write a Python program to drop empty items from a given dictionary.
a={'c1': 'Red', 'c2': 'Green', 'c3':None}
b={i:j for i ,j in a.items()if j is not None}
print(b)
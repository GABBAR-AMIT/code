#  Write a Python program to check if a set is a subset of another set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}

if set2.issubset(set1):
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")


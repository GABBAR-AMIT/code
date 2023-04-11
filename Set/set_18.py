# Write a Python program to check if a given set is a superset of itself and a superset of another given set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
if set1.issuperset(set1) and set1.issuperset(set2):
    print("set1 is a superset of itself and a superset of set2")
else:
    print("set1 is not a superset of itself and a superset of set2")

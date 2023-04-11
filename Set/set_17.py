#  Write a Python program to check if two given sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
if len(set1.intersection(set2)) == 0:
    print("The two sets have no elements in common")
else:
    print("The two sets have at least one element in common")

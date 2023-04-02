# Write a Python program to find the difference between two lists including duplicate elements
l1=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
l2=[1, 1, 2, 4, 5, 6]
diffrence=list(set(l1).symmetric_difference(l2))
print(diffrence)
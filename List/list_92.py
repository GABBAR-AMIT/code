#Write a Python program to check if a nested list is a subset of another nested list.
# Define two nested lists
list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[1, 2], [5, 6]]
a = all(i in list1 for i in list2)
if a:
    print("List2 is a subset of List1")
else:
    print("List2 is not a subset of List1")
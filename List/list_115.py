# Write a Python program to check if the elements of a given list are unique or not
a=[2, 4, 6, 8, 10, 12, 14]
if len(a)==len(set(a)):
    result=True
else:
    result=False
if result==True:
    print("All elements of the list are unique")
else:
    print("Not all elements of the list are unique")
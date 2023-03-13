# Write a Python program to calculate the difference between the two lists
# Take two lists as input from the user
list1 = list(input("Enter the first list: ").split())
list2 = list(input("Enter the second list: ").split())
d = [x for x in list1 if x not in list2]

print("The difference between the two lists is:", d)

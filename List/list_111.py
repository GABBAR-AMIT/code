# Write a Python program to access multiple elements at a specified index
# from a given list
a=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
Index_list=[0, 3, 5, 7, 10]
b=[a[i] for i in Index_list]
print(b)
#  Write a Python program to find the maximum and minimum values of the three given lists.
l1=[2, 3, 5, 8, 7, 2, 3]
l2=[4, 3, 9, 0, 4, 3, 9]
l3=[2, 1, 5, 6, 5, 5, 4]
max_value=max(max(l1),max(l2),max(l3))
min_value=min(min(l1),min(l2),min(l3))
print("The maximum value is:", max_value)
print("The minimum value is:", min_value)
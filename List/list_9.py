# Write a Python program to clone or copy a list.

#using list
olist = ['apple', 'orange', 'banana']
clist = list(olist)
print("Original List : ",olist)
print("Cloned List: ", clist)

# Using slicing
original_list = [1, 2, 3, 'a', 'b', 'c']
cloned_list = original_list[:]
print("Original List : ",original_list)
print("Cloned List: ", cloned_list)
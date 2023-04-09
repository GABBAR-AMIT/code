# Write a Python program to create a list with unique values filtered out
def filter_unique(lst):
    return [i for i in lst if lst.count(i) > 1]
lst = [1, 2, 2, 3, 4, 4, 5]
output_list = filter_unique(lst)
print( output_list)

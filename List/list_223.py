#  Write a Python program to create a list with non-unique values filtered out
def filter_non_unique(lst):
    return [i for i in lst if lst.count(i) == 1]
lst = [1, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9]
output_list = filter_non_unique(lst)
print(output_list)

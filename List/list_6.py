# Write a Python program to get a list, sorted in increasing order by the last 
# element in each tuple from a given list of non-empty tuples
def sort_tuple_last(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])
tuples = [(10, 20), (1, 2), (5, 1), (7, 6), (9, 8)]
print(sort_tuple_last(tuples)) 

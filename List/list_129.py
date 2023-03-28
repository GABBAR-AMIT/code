# Write a Python program to reverse each list in a given list of lists.
def reverse_lists(lst):
    reversed_lst = []
    for sublst in lst:
        sublst.reverse()
        reversed_lst.append(sublst)
    return reversed_lst
a=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Reversed lists: ", reverse_lists(a))
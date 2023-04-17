# Given two sets of numbers, write a Python program to find the
# missing numbers in the second set as compared to the first and vice versa. Use the Python set.
def missing_numbers(set_nums1, set_nums2):
    return set(set_nums1) - set(set_nums2),set(set_nums2) - set(set_nums1) 

set_nums1 = {1, 2, 3, 4, 5, 6}
set_nums2 = {3, 4, 5, 6, 7, 8}
result = missing_numbers(set_nums1, set_nums2)
print(result)
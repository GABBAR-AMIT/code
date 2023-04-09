#  Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers
def sum_of_two_lowest_negatives(nums):
    negatives = [i for i in nums if i < 0]
    sorted_negatives = sorted(negatives)
    return sorted_negatives[0] + sorted_negatives[1]

# Example usage:
nums1 = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
print("Original list elements:", nums1)
print(sum_of_two_lowest_negatives(nums1))

nums2 = [-4, 5, -2, 0, 3, -1, 4, 9]
print("Original list elements:", nums2)
print( sum_of_two_lowest_negatives(nums2))

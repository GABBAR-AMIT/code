# Write a Python program to find the third largest number from a given list of numbers.
# Use the Python set data type.
def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list of numbers:")
print(nums)
print(third_largest(nums))
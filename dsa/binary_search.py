#Binary search is efficient because it reduces the search space by half in each iteration.
# The time complexity of binary search is O(log n), where n is the number of elements 
# in the sorted list. This makes it significantly faster than linear search, 
# especially for large lists.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if the target element is not found

# Example usage:
my_list = [1, 2, 4, 6, 7, 9]
target_element = 6
result = binary_search(my_list, target_element)

if result != -1:
    print(f"The target element {target_element} is found at index {result}.")
else:
    print("The target element is not present in the list.")
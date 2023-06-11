# Linear Search: A simple algorithm that sequentially searches through a list
# until the target element is found.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not found

# Example usage:
my_list = [4, 2, 9, 6, 7, 1]
target_element = 6
result = linear_search(my_list, target_element)

if result != -1:
    print(f"The target element {target_element} is found at index {result}.")
else:
    print("The target element is not present in the list.")


#  Write a Python program to find the value of the last element in the given list that satisfies the provided testing function
def find_last(lst, test_func):
    for i in reversed(lst):
        if test_func(i):
            return i
    return None
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
test_function = lambda x: x > 5
output_item = find_last(input_list, test_function)
print(output_item)

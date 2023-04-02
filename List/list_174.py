# Write a Python program to add a number to each element in a given list of numbers.
def add_numbers(lst, x):
    new_lst = []
    for num in lst:
        new_lst.append(num + x)
    return new_lst

original_lst = [1, 2, 3, 4, 5]
x = 10
result_lst = add_numbers(original_lst, x)
print(result_lst)

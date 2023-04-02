# Write a Python program to convert a given list of strings into a list of lists
string_list = ['Red', 'Maroon', 'Yellow', 'Olive']
list_list = [[j for j in i] for i in string_list]
print(list_list)


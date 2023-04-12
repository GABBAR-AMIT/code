#Write a Python program to remove all duplicates from a given list of strings
# and return a list of unique strings. Use the Python set data type
def remove_duplicates(strings):
    unique_strings = set(strings)
    return list(unique_strings)
string_list = ['apple', 'banana', 'orange', 'berry', 'apple', 'kiwi', 'orange']
unique_list = remove_duplicates(string_list)
print(unique_list)

# Write a Python program to remove all strings from a given list of tuples
def remove(lst1):
    result =   [tuple(j for j in i if not isinstance(j, str)) for i in lst1]
    return list(result)

marks = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print("\nRemove all strings from the said list of tuples:")
print(remove(marks))

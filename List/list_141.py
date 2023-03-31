# Write a Python program to remove empty lists from a given list of lists.
def empty(list1):
    return [i for i in list1 if i]

list1 = [[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []]
a=empty(list1)
print(a)

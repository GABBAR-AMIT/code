# Write a Python program to sort one list based on another list containing the desired indexes
def sort(lst,order):
    return [lst[i] for i in order]
lst=['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
order=[5,4,3,2,1,0]
a=sort(lst,order)
print(a)
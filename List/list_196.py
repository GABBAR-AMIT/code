# Write a Python program to move a specified element in a given list.
def element(lst,el):
    lst.append(lst.pop(lst.index(el)))
    return lst
lst=['red','green','white','black','orange']
el='white'
print(element(lst,el))
lst=['red','green','white','black','orange']
el='black'
print(element(lst,el))
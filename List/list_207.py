# Write a Python program to find the common tuples between two given lists
def common (lst1,lst2):
    result=set(lst1).intersection(lst2)
    return result
lst1=[('red', 'green'), ('black', 'white'), ('orange', 'pink')] 
lst2=[('red', 'green'), ('orange', 'pink')] 
print(common(lst1,lst2))
#  Write a Python program to sort a given list of strings(numbers) numerically
def numerically(lst):
    int_list=list(map(int,lst))
    sortedlist=sorted(int_list)
    sorted_str_list=list(map(str,sortedlist))
    return sorted_str_list
lst=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
a=numerically(lst)
print(a)
    
    
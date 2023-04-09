# Write a Python program to remove all values except integer values from a given array of mixed values.
def remove(lst):
    return[i for i in lst if isinstance(i,int)]
lst= [34.67, 12, -94.89, "Python", 0, "C#"]
print(remove(lst))

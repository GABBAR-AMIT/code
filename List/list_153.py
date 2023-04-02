# Write a Python program to combine two sorted lists using the heapq module
def check(lst,ele,n):
    return lst.count(ele)>=n
lst=[0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
ele=0
n=4
occurs=check(lst,ele,n)
print("The element {} occurs at least {} times in the list {}: {}".format(ele,n,lst,occurs))
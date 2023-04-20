#  Write a Python program to convert a given list of tuples to a list of lists
def covert(lst):
    a=[list(i) for i in lst]
    return a
lst=[(1,2), (2,3), (3,4)]
num=covert(lst)
print(num)
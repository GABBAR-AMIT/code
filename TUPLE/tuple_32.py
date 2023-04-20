# Write a Python program to compute the sum of all the elements 
# of each tuple stored inside a list of tuples. 
def compute(lst):
    a=map(sum,lst)
    return list(a)
lst=[(1,2,6), (2,3,-6), (3,4), (2,2,2,2)]
num=compute(lst)
print(num)
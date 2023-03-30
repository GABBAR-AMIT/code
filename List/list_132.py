# Write a Python program to find all index positions of the maximum and minimum values
# in a given list of numbers.

def find (a):
    mx=max(a)
    mi=min(a)
    max_result=[i for i,j in enumerate(a) if j==mx]
    min_result=[i for i,j in enumerate(a) if j==mi]
    return max_result,min_result
a=[12,33,23,10,67,89,45,667,23,12,11,10,54]
result=find(a)
print(result)

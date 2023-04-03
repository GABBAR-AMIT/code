# Write a Python program to pair consecutive elements of a given list
def pair(lst):
    a=[[lst[i], lst[i + 1]] for i in range(len(lst) - 1)]
    return a
input=[1,2,3,4,5,6]
print(pair(input))
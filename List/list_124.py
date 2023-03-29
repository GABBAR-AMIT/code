# Write a Python program to find the maximum and minimum product of pairs of
# tuples within a given list.
def max_value(a):
    mx=max([abs(x*y)for x,y in a])
    mi=min([abs(x*y)for x,y in a])
    return mx,mi
a=[(2, 7), (2, 6), (1, 8), (4, 9)]
print('max and min value:',max_value(a))
    

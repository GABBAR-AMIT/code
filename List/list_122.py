# Write a Python program to find common elements in a nested list.
def common(x):
    b=set(x[0])
    for i in x[1:]:
        b.intersection_update(i)
    return sorted(b)
    
a=[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print(common(a))

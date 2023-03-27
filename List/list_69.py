# Write a Python program to remove duplicates from a list of lists.
a= [[1, 2], [3, 4], [1, 2], [5, 6], [7, 8], [5, 6],[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
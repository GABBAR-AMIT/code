#  Write a Python program to create a dictionary grouping a sequence of 
# key-value pairs into a dictionary of lists.
a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
b={}
for i,j in a:
    if i in b:
        b[i].append(j)
    else:
        b[i]=[j]
print(b)


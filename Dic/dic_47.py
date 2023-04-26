# Write a Python program to split a given dictionary of lists into lists of dictionaries.
a={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=len(a['Science'])
c=[]
for i in range(b):
    new={}
    for key in a:
        new[key]=a[key][i]
    c.append(new)
print(c)
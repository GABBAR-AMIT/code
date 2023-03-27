# Write a Python program to remove duplicate dictionary entries from a given list.
a= [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]
new=[]
for i in a:
    if i not in new:
        new.append(i)
print(new)
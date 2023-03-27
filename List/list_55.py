# Write a Python program to remove key-value pairs from a list of dictionaries.
a= [{'name': 'John', 'age': 25}, {'name': 'Mary', 'age': 26}, {'name': 'Jane', 'age': 40}]
b=[c for c in a if c['age']<30 ]
print(b)
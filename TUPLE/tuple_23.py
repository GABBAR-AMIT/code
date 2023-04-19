# Write a Python program to sort a tuple by its float element.
a=[('item1', '72.20'), ('item2', '15.10'), ('item3', '24.5')]
b=sorted(a,key=lambda x: x[1])
print(b)
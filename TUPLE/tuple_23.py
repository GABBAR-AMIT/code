# Write a Python program to sort a tuple by its float element.
a=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
b=(sorted(a,key=lambda x:float(x[1]),reverse=True))
print(b)
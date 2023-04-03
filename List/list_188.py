# Write a Python program to sort a given list of tuples by a specified element
original=[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
index=0
sort=sorted(original,key=lambda x:x[index])
print(sort)
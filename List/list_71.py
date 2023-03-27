# Write a Python program to check whether all dictionaries in a list are empty or not.
a=[{},{},{}]
b=[{1:2},{},{}]
print(all(not i for i in a))
print(all(not i for i in b))
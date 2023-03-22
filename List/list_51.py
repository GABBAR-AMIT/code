# Write a Python program to split a list every Nth element.
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=3
b=[a[i] for i in range(0,len(a),n)]
print(b)
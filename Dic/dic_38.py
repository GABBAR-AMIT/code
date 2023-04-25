# Write a Python program to match key values in two dictionaries
a={'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
for (i,j)in set(a.items()) & set(b.items()):
    print(i,j)
#  Write a Python program to convert more than one list to a nested dictionary.
a=["S001", "S002", "S003", "S004"]
b=["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
c={a[i]:b[i] for i in range(len(a))}
print(c)
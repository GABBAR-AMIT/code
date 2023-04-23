#  Write a Python program to print all distinct values in a dictionary
a=[{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
b=set(i for j in a for i in j.values())
print(b)

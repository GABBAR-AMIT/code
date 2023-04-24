# Write a Python program to print a dictionary in table format.
a = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in zip(*([key] + (value) for key, value in sorted(a.items()))):
    print(*i)

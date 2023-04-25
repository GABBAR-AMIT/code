# Write a Python program to count the number of items in a dictionary value that is a list.
a={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
b=sum(map(len,a.values()))
print(b)
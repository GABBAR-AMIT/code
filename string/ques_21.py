# Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters
a=input('Enter a string:')
count=0
for i in a[:4]:
    if i.upper()==i:
        count+=1
if count >=2:
    print(a.upper())
else:
    print("there are less then 2 char in upper case")
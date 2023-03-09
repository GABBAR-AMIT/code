#Write a Python program to find the common values
# that appear in two given strings
a=input('enter a string:')
b=input('common:')
set1=set(a)
set2=set(b)
i=set1.intersection(set2)
if len(i)>0:
    print("common char:", ", ".join(i))
else:
    print('no common char found')
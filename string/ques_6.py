# Write a Python program to add 'ing' at the end of a given string
#(length should be at least 3). If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged. 
a=input("Enter a string:")
if len(a)>=3:
    if(a.endswith('ing')):
        a+="ly"
    else:
        a+="ing"
print(a)
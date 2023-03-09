#68. Write a Python program to generate two strings from a given string. 
# For the first string, use the characters that occur only once, 
# and for the second, use the characters that occur multiple times in the said string.
a=input('the string: ')
b=''
c=''
for char in a:
    if(char not in b):
        b+=char
    else:
        c+=char
print('string without single repeatation: ',b)
print('string with all repatation: ',c)
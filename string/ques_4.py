#  Write a Python program to get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself.
a=input("enter a string:")
l=[]
for i in a:
    if i in l:
        l+=('$')
    else:
        l+=i
print("".join(l))
    
    





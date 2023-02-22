# Write a Python program to strip a set of characters from a string.

a= input("Enter a string : ")
b = ['a','e','i','o','u']
c=[]
for i in a:
    if i not in b:
        c+=i
print("string after removing vowels : ","".join(c))
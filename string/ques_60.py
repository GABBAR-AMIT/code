# Write a Python program to capitalize the first and last letters of each word in a given string
a=input("enter a string :")
b=a.split()
c=''
for i in b :
    c+=[0].upper()+i[1:-1]+i[-1].upper()
print(c)

    

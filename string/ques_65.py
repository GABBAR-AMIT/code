#Write a Python program to find all the common characters in lexicographical order from 
# two given lower case strings.
# If there are no similar letters print "No common characters"
a=input("Enter a string :")
b=input("enter the string :")
c=""
for i in a :
    if i in b:
        c+=i
if len(c)==0:
    print('no common character')
else:
    print(c)

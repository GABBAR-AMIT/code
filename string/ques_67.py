#Write a Python program to remove all consecutive duplicates of a given string.
a=input('the string: ')  
in_l= list(a)
b=[]
for i in in_l:
    if i not in  b or b[-1]!= i:#For each character in the list, if the result list is empty
        #or the last character doesn't match with the current one then append it to the result list.
        b.append(i)
print('.'.join(b)) #convert the filtered list back into a string
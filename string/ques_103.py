# Write a Python program to replace each character of a word of length five and more with a hash character (#)
a=input('the string: ')
b=a.split()
c=[]
for i in b:
    if len(i)>=5:
       d='#'*len(i)
       c.append(d)
    else:
        c.append(i)
print(' '.join(c)) 
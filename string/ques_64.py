# Write a Python program to find the maximum length of consecutive 0's in
# a given binary string.
a=input('the input: ')
b = 0
c = 0
for i in range(len(a)):
    if a[i] =='0':
        b+=1
    else:
        if c<b :
            c=b
if b>c :
    c=b
print(c)
print(b)
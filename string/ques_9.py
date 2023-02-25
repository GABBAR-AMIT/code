# Write a Python program to remove the nth index character from a nonempty string.
a=input('the string name:')
b=int(input('nth index:'))
c=a[:b]+a[b+1:]
print('the string output:',c)
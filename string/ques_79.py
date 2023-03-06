#Write a Python program to find the smallest and largest words in a given string.

s = input("The is string:")
w= s.split()
largest=small=w[0]
for i in range(0,len(w)):
    if len(largest)<len(w[i]):
        largest=w[i]
        if len(small)>len(w[i]):
         small=w[i]
print('largest number:',largest)
print('smallest number:',small)    
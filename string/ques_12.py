# Write a Python program to count the occurrences of 
# each word in a given sentence
s = input('Enter a sentence: ') # (python,the,python)
w = s.split() 
c={}
for i in w:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
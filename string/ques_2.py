# Write a Python program to count the number of characters
# (character frequency) in a string. 
a="Google:"
d={}
for i in a:
    k=d.keys()
    if a in k: # comparison that is why using "k"
        d[i]+=1 # data save that is why using "d"
    else:
        d[i]=1 # data save that is why using "d
print(d)
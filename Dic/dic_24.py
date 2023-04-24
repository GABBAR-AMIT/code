#  Write a Python program to create a dictionary from a string
# Note: Track the count of the letters from the string.
a="w3resource"
b={}
for i in a:
    b[i]=b.get(i,0)+1
print(b)
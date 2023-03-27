# Write a Python program to create a list taking alternate elements from a given list.
a=['red', 'black', 'white', 'green', 'orange']
b=[]
for i in range(0,len(a),2):
    b.append(a[i])
print(b)
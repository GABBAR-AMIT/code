# Write a Python program to generate groups of five consecutive numbers in a list.
a=[1,2,3,4,5,6,7,8,9,10,]
b=[]
for i in range(0,len(a),5):
    c=[]
    for j in range(i,i+5):
        c.append(a[j])
    b.append(c)
print(b)
    
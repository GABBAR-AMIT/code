a=[-1,-2,-3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[]
for i in range(0,len(a),5):
    c=[]
    for j in range(i,i+5):
        c.append(a[i])
    b.append(c)
print(b)
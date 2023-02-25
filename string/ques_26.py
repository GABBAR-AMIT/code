# Write a Python program to display formatted text (width=50) as output.
s=input('Enter the string:')
z=[]
n=1
u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in s:
    if i in u:
        x=u.index(i)
        z+=u[x+n]
    elif i in l:
        x=l.index(i)
        z+=l[x+n]
    else:
        print('char not available')
        break
print("".join(z))
        
        
    

# Write a Python program to create a list taking alternate elements from a given
def lis(a):
    b=a[::2]
    return(b)
    
a=['red', 'black', 'white', 'green', 'orange']

print(lis(a))
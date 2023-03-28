# Write a Python program to reverse strings in a given list of string values
def reverse(a):
    b=[]
    for i in a:
        b.append(i[::-1])
    return(b)
a=['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse(a))
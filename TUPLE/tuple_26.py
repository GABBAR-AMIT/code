# Write a Python program to calculate the product, 
# multiplying all the numbers in a given tuple
def multiplying(a):
    b=1
    for i in a:
        b*=i
    return b
a=(4, 3, 2, 2, -1, 18)
product=multiplying(a)
print(f"The product of{a}is{product}")
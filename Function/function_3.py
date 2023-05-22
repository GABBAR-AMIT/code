# Write a Python function to multiply all the numbers in a list. 
def multiply(numbs):
    a=1
    for x in numbs:
        a*=x
    return a
print(multiply((100,20,3,1)))
# Write a Python function to find the maximum of three numbers.
def maxtwo(x,y):
    if x>y:
        return x
    return y
def maxthree(x,y,z):
    return maxtwo(x,maxtwo(y,z))
print(maxthree(13,-16,56))

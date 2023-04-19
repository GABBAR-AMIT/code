#  Write a Python program to convert a given string list to a tuple
def covert(a):
    b=tuple(i for i in a if not a.isspace())
    return b

a="python 3.0"
print(covert(a))
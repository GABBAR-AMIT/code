#  Write a Python program to find the indexes of all None items in a given list
def index(x):
    result=[i for i in range (len(x)) if x[i]== None]
    return result
x=[1, None, 5, 4,None, 0, None, None]
print(index(x))
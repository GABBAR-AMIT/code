#Write a Python program to convert a given list of strings and characters to a single list of characters
def char(lst):
    a=[i for i in lst for i in i]
    return a
colors = ["red", "white", "a", "b", "black", "f"]
print(char(colors))
#Write a Python program to convert a tuple to a dictionary.
a=((5,"A"),(10,"B"))
print(dict((x,y) for x, y in a ))
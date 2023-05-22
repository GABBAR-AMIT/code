# Write a Python program to reverse a string
def string (str1):
    rstr=""
    index=len(str1)
    while index>0:
        rstr+=str1[index-1]
    return rstr
print(string('123456789'))
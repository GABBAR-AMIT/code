# Write a Python program to check if a given string contains an element that is present in a list.
def check(lst,str):
    result=[i for i in lst if (i in str)]
    return bool(result)
lst=['.com', '.edu', '.tv'] 
str="https://www.w3resource.com/python-exercises/list/"
print(check(lst,str))
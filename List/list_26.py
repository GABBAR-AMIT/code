# Write a Python program to check whether two lists are circularly identical.
a=input("first list:").split(",")
b=input("second list:").split(",")
if len(a)==len(b) and a in b:
    print("Identical")
else:
    print("non Identical")
        
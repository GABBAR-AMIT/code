#Write a Python program to capitalize the first and last letters of each word
# in a given string.
a = input("Enter the string to input : ")
b= input("enter the string to be inserted :")
mid = int(len(a)/2)
print(" the output : ", a[0:mid]+b+a[mid:])
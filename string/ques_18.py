# Write a Python function to get a string made of the first three characters
# of a specified string. If the length of the string is less than 3,
# return the original string
s=input('Enter the string :')
firstThreeChars = s[:3]
print(firstThreeChars if len(s) > 3 else s) 


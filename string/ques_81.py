#Write a Python program to determine the index of a given string at 
# which a certain substring starts. If the substring is not found in 
# given string return 'Not found'.


s=input("enter the string :")
sub=input("enter the sub string :")
if sub in s:
    print(f"the substring {sub} is found at index {s.index(sub )} ")
else:
    print("not found")
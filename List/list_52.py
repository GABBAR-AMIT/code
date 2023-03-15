#  Write a Python program to compute the difference between two lists
a=set(input("enter the elements of first list :").split())
b=set(input("enter the elements of second list :").split())
c=list(a-b)+list(b-a)
print('the diffrent between the two list:',c)
      
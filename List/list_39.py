#  Write a Python program to convert a list of multiple integers into a single integer.
a=int(input("Enter the length of the string:"))
b=[]
for i in range(a):
    b.append(int(input("enter element {}:".format(i+1))))
result=''.join(map(str,b))
print("list of integers:",b)
print("single integer:",result)
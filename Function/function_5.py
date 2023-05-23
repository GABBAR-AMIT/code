# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def factroial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    print(a)
n=int(input("enter a number:"))
factroial(n)
#  Write a Python program to read an entire text file

def filereade(fname):
    if fname == False:
        a=open(fname,'x')
    else:
        b=open(fname,'r')
        print(b.read())

i = input("Enter the name of the file : ")
filereade(i)
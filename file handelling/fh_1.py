#  Write a Python program to read an entire text file

def filereade(fname):
    if fname == True:
        b=open(fname,'r')
        print(b.read())
    else:
        a=open(fname,'x')
        

i = input("Enter the name of the file : ")
filereade(i)
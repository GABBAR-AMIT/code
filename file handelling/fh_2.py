#  Write a Python program to read first n lines of a file
def n_line(fname,n):
    if fname == True:
        a=open(fname,'r')
        l=a.readlines()
        for i in range(0,n):
            print(l[i])
    else:
        print("File not found.")
        
i = input("Enter the firl name : ")
j = int(input("Enter the number of lines : "))
n_line(i,j)
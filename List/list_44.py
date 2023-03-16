# Write a Python program to generate groups of five consecutive numbers in a list.
list=[]
#l = []
for i in range(1,11):
    if i % 5==1:
        l=[i]
        print("if : ",l)
        print("if list :", list)
    elif i % 5 !=0:
        l.append(i)
        print("elif : ", l)
        print("elif list :", list)
    else:
        l.append(i) # 1 is add from here 
        print("else : ", l)
        list.append(l)
        print("else list :", list)
print(list)
print(l)

# Write a Python program to check whether a list contains a sublist
a=[1,2,3,4,5,6,7]
sub_list=[4,5]
for i in range(len(a)):
    if a[i]==sub_list[0]:
        match=True
        for j in range(1, len(sub_list)):
            if a[i+j]!=sub_list[j]:
                match=False
                break
        if match:
            print("sublist found:",i)
            break
else:
    print('sublist not found')
    
    
main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]

if any(main_list[i:i+len(sub_list)] == sub_list for i in range(len(main_list)-len(sub_list)+1)):
    print("The list contains the given sublist")
else:
    print("The list does not contain the given sublist")

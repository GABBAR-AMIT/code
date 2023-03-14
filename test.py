# Request the user to enter the length and elements of the list
num = int(input("Enter the length of the List: "))
lst = []

for i in range(num):
    lst.append(int(input("Enter element {}:".format(i+1))))

# Convert the list of integers into a single integer
result = ''.join(map(str, lst))

print("List of integers:", lst)
print("Single integer: ", result)

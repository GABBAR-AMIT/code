# Write a Python program to count the number of substrings with the same first
# and last characters in a given string.
string = input("Enter a string: ")
count = 0

for i in range(len(string)):
    for j in range(i, len(string)):
        if string[i] == string[j]:
            count += 1
            
print(f"The number of substrings with the same first and last characters is {count}")

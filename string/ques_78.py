# . Write a Python program to count characters at the same position
# in a given string(lower and uppercase characters) as in the English alphabet
# initialize the English alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# get user input for the string to check
input_string = input("Enter a string to check: ")

# initialize the counter variable
count = 0

# loop through each character in the input string
for i in range(len(input_string)):
    # check if the current character is a letter
    if input_string[i].isalpha():
        # check if the letter is uppercase or lowercase
        if input_string[i].isupper():
            # check if the letter is at the same position as in the English alphabet
            if input_string[i].lower() == alphabet[i]:
                # increment the counter variable
                count += 1
        else:
            # check if the letter is at the same position as in the English alphabet
            if input_string[i] == alphabet[i]:
                # increment the counter variable
                count += 1

# print the final count
print("The number of characters at the same position as in the English alphabet is:", count)

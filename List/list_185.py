# Write a Python program to convert a given decimal number to a binary list
decimal = 8
binary = []
while decimal > 0:
    # Add the remainder to the list
    binary.append(decimal % 2)
    decimal //= 2
binary.reverse()

print("The binary representation is:", binary)

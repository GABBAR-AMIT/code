# Write a Python program to print four integer values - decimal, octal, 
# hexadecimal (capitalized), binary - in a single line.
num = int(input("Enter a number: "))
decimal = str(num)
octal = oct(num)
hexadecimal = hex(num).upper()
binary = bin(num)

print("Decimal: {0}, Octal: {1}, Hexadecimal: {2}, Binary: {3}".format(decimal, octal, hexadecimal, binary))

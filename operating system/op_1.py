# Write a Python program to get the name of the operating system 
# (Platform independent), information of the current operating system, 
# current working directory, print files and directories in the current directory, 
# and raise errors if the path or file name is invalid
import os

# Get the name of the operating system (Platform independent)
print("Operating System:", os.name)

# Get information of the current operating system
print("\nInformation of current operating system:", os.uname())

# Get the current working directory
print("\nCurrent Working Directory:", os.getcwd())

# Print files and directories in the current directory
print("\nList of files and directories in the current directory:")
print(os.listdir('.'))

# Test if a specified file exists or not
print("\nTest if a specified file exists or not:")
try:
    filename = 'abc.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
    print('Cannot access or problem in reading: ' + filename)

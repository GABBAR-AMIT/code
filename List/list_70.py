# Write a Python program to find items starting with a specific character from a list.

list = ['hello', 'world', 'hey', 'how', 'are', 'you']
char = 'h'
result = [i for i in list if i.startswith(char)]
print(result)

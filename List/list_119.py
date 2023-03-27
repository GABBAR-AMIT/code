#  Write a Python program to check if a substring appears in a given 
# list of string values
string_list=['red', 'black', 'white', 'green', 'orange']
substring='ack'
for i in string_list:
    if substring in i:
        print(f"Found '{substring}' in '{i}'.")
    else:
        print(f"'{substring}' not found in '{i}'.")
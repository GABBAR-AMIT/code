# Write a Python program to remove leading zeros from an IP address.
'''a=input('Enter the ip:')
b=[]
s=a.split()
for i in s:
    if i!='0':
        b.append(i)
print('.'.join(b))'''

import re

# enter the IP address here
ip_address =input("000.120.098.054:") 

# Remove leading zeros
new_ip = re.sub('\.[0]*', '.', ip_address)

print("IP address with leading zeros removed:", new_ip)
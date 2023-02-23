# 49. Write a Python program to count and display vowels in text

text = input("Please enter a string: ") 
 
vowels = 0

for i in text: 
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'): 
        vowels += 1
        
print("No. of Vowels in the string: ", vowels)


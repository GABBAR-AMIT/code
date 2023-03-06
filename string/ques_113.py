#Write a Python program that returns a string sorted alphabetically by the
# first character of a given string of words. Go to the editor
'''a=input('Entre a string :')
b=a.split()
c=''
for i in a:
    c=b.sorted()
print'''

string = input("Enter a string of words: ")
words_list = string.split()

sorted_words = sorted(words_list, key=lambda x: x[0])

result = " ".join(sorted_words)

print(result)


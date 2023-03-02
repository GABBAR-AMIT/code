string = input("Enter the string: ") 
words = string.split(' ')[::-1] #  why slicing here?

string_rev = [] #created a empyt list for fillig the words in reverse order
for word in words: 
    string_rev.append(word) 
  
print("Reversed String:") 
print(" ".join(string_rev))
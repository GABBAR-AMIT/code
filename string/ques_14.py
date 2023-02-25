#  Write a Python program that accepts a comma-separated sequence of words 
# as input and prints the distinct words in sorted form (alphanumerically)
w = input("Enter separated by commas: ") 
word = w.split(',') 
print(','.join(sorted(list(set(word))))) 
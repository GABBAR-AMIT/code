# Write a Python function that checks whether a passed string is a palindrome or not.
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
# e.g., madam or nurses run.
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
    
word = "madam"
if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

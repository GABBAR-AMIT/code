#  Write a Python program to randomize the order of the values of a list, returning a new list
import random
def random_list(lst):
    new_lst=lst.copy()
    random.shuffle(new_lst)
    return new_lst
lst=[1, 2, 3, 4, 5, 6]
randomized=random_list(lst)
print(randomized)
# Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists
def max_min(lst):
    all = [] 
    for i in lst:
        curr_sum = sum(i)
        all.append(curr_sum) 
    max_sum = max(all)
    min_sum = min(all) 
    return max_sum, min_sum
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_sum, min_sum = max_min(lst)
print("The maximum sum of a sublist is:", max_sum)
print("The minimum sum of a sublist is:", min_sum)

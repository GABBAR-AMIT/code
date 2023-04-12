#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs
lst = [1, 2, 3, 4, 5]
target_sum = 7
result = find_pairs(lst, target_sum)
print(result) 

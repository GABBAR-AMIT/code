#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value
def find_pairs(nums, target_val):
    nums_set = set(nums)
    pairs = []
    for n in nums_set:
        complement = target_val - n
        if complement in nums_set:
            pairs.append({n, complement})
    return pairs

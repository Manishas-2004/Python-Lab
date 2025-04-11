# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_max_min(lst):
    max_num = lst[0]
    min_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num
print(find_max_min([1, 2, 3, 4, 5]))  # Output: (5, 1)

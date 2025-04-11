# 1. Write a Python program to sum all the items in a list.

def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total
print(sum_list([1, 2, 3, 4, 5]))  

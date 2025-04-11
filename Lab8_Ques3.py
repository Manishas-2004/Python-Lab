#3. Write a Python program to find duplicate values from a list and display those.

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates
print(find_duplicates([1, 2, 3, 4, 4, 5, 1]))

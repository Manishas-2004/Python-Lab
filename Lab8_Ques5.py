# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red

def reverse_traverse(lst):
    for i in range(len(lst)-1, -1, -1):
        print(f"Index: {i}, Element: {lst[i]}")
colors = ['red', 'green', 'white', 'black']
reverse_traverse(colors)


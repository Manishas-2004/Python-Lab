# 2.Write a Python program to print the multiplication table of a given number using a for loop.

num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

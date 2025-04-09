# 1. Print a Pyramid Pattern of Stars:
#Write a program to print a pyramid pattern using stars (*).

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

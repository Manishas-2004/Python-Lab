# 2. Count Even and Odd Numbers
# Write a program to count the even and odd numbers in a list.

numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 3. Calculate the Sum of Even Numbers
# Write a program to calculate the sum of all even numbers in a given range.

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
even_sum = 0
even_numbers = []
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
        even_numbers.append(str(num))
print(f"Output: {even_sum} ({' + '.join(even_numbers)})")

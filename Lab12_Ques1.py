#1.Write a program that asks the user for a list index and prints the value at that index from a predefined list. Handle the IndexError and ValueError exceptions.

my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index to retrieve from the list: "))
    print(f"The value at index {index} is {my_list[index]}")
except IndexError:
    print("Error: Index is out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")

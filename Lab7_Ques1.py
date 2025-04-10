# 1.Write a Python program to generate an invoice for a customer using their name, product, and price details.


name = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price: "))
print("\n----- Invoice -----")
print(f"Customer Name: {name}")
print(f"Product: {product}")
print(f"Price: ${price:.2f}")

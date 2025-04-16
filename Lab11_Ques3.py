#3.Build a simple inventory system where each item and its quantity is stored in a dictionary. Ask the user to enter an item name and quantity to sell.
#Update the dictionary and show the remaining stock or a message if there's not enough.

inventory = {
    "apple": 10,
    "banana": 15,
    "mango": 5
}
item = input("Enter item to sell: ").lower()
quantity = int(input("Enter quantity: "))
if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"Sold {quantity} {item}(s). Remaining stock: {inventory[item]}")
    else:
        print("Not enough stock.")
else:
    print("Item not found.")

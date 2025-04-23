#3.You have a dictionary. Ask the user to enter a key and display the corresponding value. Handle the KeyError.


my_dict = {
    "apple": "A sweet red fruit",
    "banana": "A yellow fruit",
    "carrot": "An orange vegetable"
}
try:
    key = input("Enter a key: ")
    value = my_dict[key]
    print(f"The value for '{key}' is: {value}")
except KeyError:
    print("KeyError: The key you entered does not exist in the dictionary.")

#4.Create a contact book using a dictionary where the name is the key and phone number is the value. Allow the user to input a name and phone number.
#If the name exists, update the number; otherwise, insert a new contact.

contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210"
}
name = input("Enter contact name: ")
phone = input("Enter phone number: ")

if name in contacts:
    contacts[name] = phone
    print("Contact updated.")
else:
    contacts[name] = phone
    print("New contact added.")
print(contacts)

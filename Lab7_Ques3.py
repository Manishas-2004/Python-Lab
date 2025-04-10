# 3.Write a program that removes extra spaces from a user-entered message.


message = input("Enter a message with extra spaces: ")
cleaned_message = ' '.join(message.split())
print(f"Cleaned message: {cleaned_message}")

# 5.Check if a password contains at least 1 uppercase letter, 1 lowercase letter, 1 digit, and is at least 8 characters long.


password = input("Enter your password: ")
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
long_enough = len(password) >= 8
if has_upper and has_lower and has_digit and long_enough:
    print("Password is valid.")
else:
    print("Password is invalid.")

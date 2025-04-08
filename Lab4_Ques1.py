#1 Write a program that takes a person's age and prints the ticket price:
#Age < 5: Free
#Age 5-18: ₹100
#Age 19-60: ₹200
#Age > 60: ₹150


age = int(input("Enter your age: "))
if age < 5:
    print("Ticket Price: Free")
elif 5 <= age <= 18:
    print("Ticket Price: ₹100")
elif 19 <= age <= 60:
    print("Ticket Price: ₹200")
else:  
    print("Ticket Price: ₹150")

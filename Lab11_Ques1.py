#1.Create a dictionary with student names as keys and their marks as values.
#Allow the user to input a name and display the student's marks. If the student doesn't exist, show an appropriate message.

students = {
    "Manisha": 85,
    "Gokul": 92,
    "Vaibhavi": 78
}
name = input("Enter student name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")

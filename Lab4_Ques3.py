# 3. Write a program to take marks as input and print grade:
#≥90: A
#≥80: B
#≥70: C
#≥60: D
#<60: F

# Input marks
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

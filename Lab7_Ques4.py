# 4.Take a feedback string and count how many times the word “good” appears in it (case-insensitive).


feedback = input("Enter your feedback: ")
count = feedback.lower().count("good")
print(f"The word 'good' appears {count} time(s).")

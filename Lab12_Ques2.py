#2. Create a program to validate exam scores entered by the user. Use a custom exception to handle invalid scores.


class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return "Score is valid!"
try:
    score_input = float(input("Enter exam score: "))
    message = validate_score(score_input)
    print(message)
except InvalidScoreError as e:
    print(f"InvalidScoreError: {e}")
except ValueError:
    print("ValueError: Please enter a valid number.")

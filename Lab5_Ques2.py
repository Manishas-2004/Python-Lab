#2. Function to Count Occurrences of a Character in a String
#Write a function count_char_occurrences(s, char) that counts how many times a specific character char appears in the string s.


def count_char_occurrences(s, char):
  """
  Counts how many times a specific character appears in a string.
  Args:
    s: The input string.
    char: The character to count.
  Returns:
    The count of occurrences of char in s.
  """
  count = 0
  for c in s:
    if c == char:
      count += 1
  return count
input_string = "hello"
char_to_count = "l"
occurrence_count =count_char_occurrences(input_string, char_to_count)
print(f"Input string: '{input_string}'")
print(f"Character to count: '{char_to_count}'")
print(f"Count of Occurences:{occurrence_count}")

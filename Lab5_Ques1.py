#1. Function to Remove Specific Character from a String
#Write a function remove_char(s, char) that removes all occurrences of a specific character from a string.

def remove_char(s, char):
  """
  Removes all occurrences of a specific character from a string.
  Args:
    s: The input string.
    char: The character to remove.
  Returns:
    The string without the specified character.
  """
  new_string = ""
  for c in s:
    if c != char:
      new_string += c
  return new_string
input_string = "hello"
char_to_remove = "l"
output_string = remove_char(input_string, char_to_remove)
print(f"Input string: '{input_string}'")
print(f"Character to remove: '{char_to_remove}'")
print(f"Output string: '{output_string}'")

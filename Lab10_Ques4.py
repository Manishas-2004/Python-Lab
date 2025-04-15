#4. Check for Duplicate Words in a Sentence
#Problem4: Check whether a sentence has duplicate words.
#sentence = "the sky is blue and the grass is green"

sentence = "the sky is blue and the grass is green"
words = sentence.split()
has_duplicates = len(words) != len(set(words))
print("Has duplicates:", has_duplicates)

#2.Given a list of names, group them into a dictionary where the key is the first letter of each name and the value is a list of names that start with that letter.

names = ["Anushree", "Manjula", "Praveen", "Anshika", "Heama", "Manisha"]
grouped_names = {}
for name in names:
    first_letter = name[0]
    grouped_names.setdefault(first_letter, []).append(name)
print(grouped_names)

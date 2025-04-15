#Problem5: A warehouse is supposed to have items A–E. Find out which ones are missing.
#expected_items = {"A", "B", "C", "D", "E"}
#available_items = {"A", "C", "E"}


expected_items = {"A", "B", "C", "D", "E"}
available_items = {"A", "C", "E"}
missing_items = expected_items - available_items
print(missing_items)

#Problem1: You are given a list of customer IDs with duplicates. Remove the duplicates.

#customer_ids = [101, 102, 103, 101, 104, 102]

customer_ids = [101, 102, 103, 101, 104, 102]
unique_customer_ids = list(set(customer_ids))
print(unique_customer_ids)

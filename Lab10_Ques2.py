#Problem2: Two stores have customer records. Find customers who shopped at both stores.

#store1_customers = {"Alice", "Bob", "Charlie", "David"}
#store2_customers = {"Eve", "Bob", "David", "Frank"}


store1_customers = {"Alice", "Bob", "Charlie", "David"}
store2_customers = {"Eve", "Bob", "David", "Frank"}
common_customers = store1_customers & store2_customers
print(common_customers)
